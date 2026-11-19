"""Manual Codeforces submission, exact verdict verification, Accepted-only Git push."""
from contextlib import contextmanager
import fcntl
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request
from urllib.parse import urlencode
import webbrowser

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / '.cf-local'

def save(path, data):
    LOCAL.mkdir(mode=0o700, exist_ok=True)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(data, indent=2))
    temp.chmod(0o600)
    temp.replace(path)

@contextmanager
def lock():
    LOCAL.mkdir(mode=0o700, exist_ok=True)
    with (LOCAL / 'submit.lock').open('w') as file:
        try:
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('Another submission watcher is running. Use that terminal or stop it first.') from None
        try:
            yield
        finally:
            fcntl.flock(file, fcntl.LOCK_UN)

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args], text=True).strip()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def normalized(text):
    return text.replace('\r\n', '\n').rstrip('\n')

def clipboard_command(read=False):
    import shutil
    pairs = [('pbcopy', 'pbpaste'), ('wl-copy', 'wl-paste')]
    for copy, paste in pairs:
        cmd = paste if read else copy
        if shutil.which(cmd):
            return [cmd, '--no-newline'] if cmd == 'wl-paste' else [cmd]
    if shutil.which('xclip'):
        return ['xclip', '-selection', 'clipboard'] + (['-o'] if read else [])
    raise ValueError('No clipboard utility found. macOS: pbcopy/pbpaste; Linux/WSL: install wl-clipboard or xclip in a desktop session.')


def setup(handle):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', handle):
        raise ValueError('Invalid Codeforces handle.')
    save(LOCAL / 'config.json', {'handle': handle})
    print(f'Handle set: {handle}. Submit manually in your normal browser; no automation login required.')

def api(handle):
    url = 'https://codeforces.com/api/user.status?' + urlencode({'handle': handle, 'from': 1, 'count': 1000})
    request = urllib.request.Request(url, headers={'User-Agent': 'LocalCodeforcesPractice/1.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data.get('status') != 'OK':
        raise ValueError(f'Codeforces API error: {data.get("comment", "unknown")}')
    return data['result']

def candidates(rows, state):
    return [r for r in rows if r['id'] > state.get('baseline', 0)
            and str(r.get('problem', {}).get('contestId')) == state['contest']
            and r.get('problem', {}).get('index') == state['index']
            and any(m.get('handle', '').lower() == state['handle'].lower() for m in r.get('author', {}).get('members', []))]

def collect_submission(state, timeout):
    print(f'Waiting for your manual {state["contest"]}{state["index"]} submission; ID will be detected automatically…', flush=True)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        matches = [row for row in candidates(api(state['handle']), state)
                   if row.get('creationTimeSeconds', 0) >= state['preparedAt']]
        if len(matches) > 1:
            raise ValueError('Multiple new submissions match. Specify the exact one with cf watch SUBMISSION_ID; nothing pushed.')
        if matches:
            print(f'Detected submission #{matches[0]["id"]}', flush=True)
            return matches[0]['id']
        time.sleep(3)
    raise ValueError('No new submission detected before timeout. Run push this again to resume; no automatic resubmission occurs.')


def parse_submission(value, contest):
    if re.fullmatch(r'\d+', value):
        return int(value)
    match = re.fullmatch(r'https://codeforces\.com/(?:contest/(\d+)/submission/|problemset/submission/(\d+)/)(\d+)/?', value)
    if not match or (match[1] or match[2]) != contest:
        raise ValueError('Enter the exact submission ID or a Codeforces submission URL for this contest.')
    return int(match[3])

def extract_source(html):
    from cf import Parser, Node
    parser = Parser();parser.feed(html)
    def visit(node):
        if node.attrs.get('id') == 'program-source-text':
            return node.text()
        for child in node.children:
            if isinstance(child, Node):
                text = visit(child)
                if text is not None: return text
        return None
    source = visit(parser.root)
    if source is None:
        raise ValueError('Server-side source is unavailable in this page (login or Cloudflare may block it).')
    return source

def accepted_push(state, message=''):
    source = ROOT / state['source']
    if digest(source.read_bytes()) != state['sha256']:
        raise ValueError('Source changed since submission. Restore the submitted version before retrying; nothing pushed.')
    if git('branch', '--show-current') != state['branch']:
        raise ValueError('Branch changed since submission. Nothing pushed.')
    if not state.get('commit'):
        if git('rev-parse', 'HEAD') != state['head']:
            raise ValueError('HEAD changed since submission. Nothing committed or pushed.')
        if git('diff', '--cached', '--name-only'):
            raise ValueError('Other changes are staged. Unstage them before retrying.')
        if state.get('verifiedVerdict') != 'OK' or state.get('verifiedSourceHash') != state['sha256']:
            raise ValueError('Accepted verdict and matching submitted source are required before pushing.')
        statement = source.parent / 'problem.md'
        if not statement.is_file() or not statement.read_text().strip():
            raise ValueError('Problem statement is missing or empty. Restore problem.md before pushing.')
        statement_path = str(statement.relative_to(ROOT))
        statement_hash = digest(statement.read_bytes())
        paths = [state['source'], statement_path]
        if (ROOT / 'practice/catalog.json').exists():
            import practice
            paths.append(str(practice.export_state().relative_to(ROOT)))
        git('add', '--', *paths)
        staged = subprocess.check_output(['git', '-C', str(ROOT), 'show', ':' + state['source']])
        if digest(staged) != state['sha256']:
            git('reset', '--', *paths)
            raise ValueError('File changed during staging. Nothing committed.')
        staged_statement = subprocess.check_output(['git', '-C', str(ROOT), 'show', ':' + statement_path])
        if digest(staged_statement) != statement_hash:
            git('reset', '--', *paths)
            raise ValueError('Statement changed during staging. Nothing committed.')
        if git('diff', '--cached', '--name-only'):
            git('commit', '-m', message or f'Solve {state["contest"]}{state["index"]} (Accepted #{state["submission"]})', '--', *paths)
        state['statement'] = statement_path
        state['statementHash'] = statement_hash
        state['commit'] = git('rev-parse', 'HEAD')
        save(LOCAL / 'pending.json', state)
    if git('rev-parse', 'HEAD') != state['commit']:
        raise ValueError('HEAD changed after acceptance. Resolve Git state before retrying.')
    if not state.get('statement') or not state.get('statementHash'):
        raise ValueError('Pending commit has no verified statement. Nothing pushed; inspect the pending commit before retrying.')
    for path, expected in [(state['source'], state['sha256']), (state['statement'], state['statementHash'])]:
        committed = subprocess.check_output(['git', '-C', str(ROOT), 'show', state['commit'] + ':' + path])
        if digest(committed) != expected:
            raise ValueError('Committed solution or statement differs from the verified files. Nothing pushed.')
    subprocess.run(['git', '-C', str(ROOT), 'push', 'origin', f'{state["commit"]}:refs/heads/{state["branch"]}'], check=True)
    save(LOCAL / 'last-accepted.json', state)
    (LOCAL / 'pending.json').unlink(missing_ok=True)
    import practice
    practice.mark(state['contest'] + state['index'], status='accepted', submission=state['submission'], commit=state['commit'], pushed=True)
    print('Accepted solution and problem statement pushed to GitHub. Dashboard progress updated.')

def finish_verdict(state, verdict, message=''):
    if verdict == 'OK':
        if state.get('sha256') and state.get('verifiedSourceHash') == state['sha256']:
            import practice
            practice.accept(state['contest'] + state['index'], state['submission'])
        state['verifiedVerdict'] = 'OK'
        save(LOCAL / 'pending.json', state)
        accepted_push(state, message)
        return
    save(LOCAL / 'last-rejected.json', dict(state, verdict=verdict))
    (LOCAL / 'pending.json').unlink(missing_ok=True)
    import practice
    if state.get('contest') and state.get('index'):
        practice.mark(state['contest'] + state['index'], status='attempted', verdict=verdict)
    raise ValueError(f'{verdict}: nothing committed or pushed. Fix the code and try again.')

def preflight():
    branch = git('branch', '--show-current')
    if not branch:
        raise ValueError('Check out a Git branch first.')
    if git('diff', '--cached', '--name-only'):
        raise ValueError('Unstage other changes first; only the accepted solution will be committed.')
    subprocess.run(['git', '-C', str(ROOT), 'fetch', 'origin', branch], check=True)
    if git('rev-list', '--count', f'origin/{branch}..HEAD') != '0':
        raise ValueError('Existing unpushed commits found. Handle those separately before submitting.')
    return branch

def submit(message=''):
    from manual_workflow import submit as manual_submit
    return manual_submit()


def watch(submission=None, html=None, source_clipboard=False, timeout=600):
    with lock():
        return _watch(submission, html, source_clipboard, timeout)

def _watch(submission, html, source_clipboard, timeout, message='', push_after=False):
    pending = LOCAL / 'pending.json'
    if not pending.exists():
        raise ValueError('No prepared submission. Run push this first.')
    state = json.loads(pending.read_text())
    if digest((ROOT / state['source']).read_bytes()) != state['sha256']:
        raise ValueError('Local source changed after preparation; nothing pushed. Restore the saved snapshot or cf cancel.')
    if state.get('commit'):
        if push_after:
            return accepted_push(state, message or state.get('message', ''))
        print('Verified commit ready. Run push this to publish it.')
        return
    if submission:
        number = parse_submission(submission, state['contest'])
        if state.get('submission') and state['submission'] != number:
            raise ValueError('A different submission is already pending. Finish it or run cf cancel.')
        state['submission'] = number
    if not state.get('submission'):
        state['submission'] = collect_submission(state, timeout)
    save(pending, state)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        rows = api(state['handle'])
        row = next((r for r in rows if r['id'] == state['submission']), None)
        if row is None or row not in candidates(rows, state):
            raise ValueError('Exact submission/account/problem not found. Nothing pushed.')
        if row.get('creationTimeSeconds', 0) < state['preparedAt'] - 5:
            raise ValueError('This submission predates the saved snapshot. Submit the current solution; nothing pushed.')
        verdict = row.get('verdict')
        print(f'#{state["submission"]}: {verdict or "IN_QUEUE"}', flush=True)
        if verdict and verdict != 'TESTING':
            if verdict != 'OK':
                return finish_verdict(state, verdict)
            break
        time.sleep(3)
    else:
        raise ValueError('Judging timed out. Run cf watch to resume without resubmitting.')
    url = f'https://codeforces.com/contest/{state["contest"]}/submission/{state["submission"]}'
    if state.get('verifiedSourceHash') != state['sha256']:
        if source_clipboard:
            source = subprocess.check_output(clipboard_command(read=True)).decode('utf-8')
            method = 'user-copied source from exact submission page'
        else:
            try:
                if html:
                    content = Path(html).read_text()
                    # Saved pages must identify the exact submission, not just include a code block.
                    if not re.search(r'(?:submission/|submission-id=[\"\x27])' + str(state['submission']) + r'\b', content):
                        raise ValueError('Saved HTML does not identify the pending submission.')
                    method = 'saved submission page (user supplied)'
                else:
                    request = urllib.request.Request(url, headers={'User-Agent': 'LocalCodeforcesPractice/1.0'})
                    with urllib.request.urlopen(request, timeout=30) as response:
                        content = response.read().decode('utf-8')
                    method = 'public submission source'
                source = extract_source(content)
            except (OSError, ValueError) as exc:
                raise ValueError(f'Accepted, but source verification is blocked: {exc}\nNothing pushed. Open {url}, copy ONLY the submitted source code, then run:\ncf watch {state["submission"]} --source-clipboard\nThis fallback relies on you copying the exact submission source, not your local editor.') from exc
        snapshot = (LOCAL / 'submitted-source.cpp').read_text()
        if normalized(source) != normalized(snapshot):
            raise ValueError('Submitted source does not match the saved snapshot. Nothing pushed.')
        state['verifiedSourceHash'] = state['sha256']
        state['sourceVerification'] = method
        save(pending, state)
    if push_after:
        finish_verdict(state, 'OK', message or state.get('message', ''))
    else:
        state['verifiedVerdict'] = 'OK'
        save(pending, state)
        import practice
        practice.accept(state['contest'] + state['index'], state['submission'])
        print(f'Submission #{state["submission"]}: Accepted, source matched. Ready to push. Run: push this')

def push_ready(message=''):
    from manual_workflow import push
    return push(message)


def cancel():
    with lock():
        pending = LOCAL / 'pending.json'
        if pending.exists():
            save(LOCAL / 'cancelled-submission.json', json.loads(pending.read_text()))
            pending.unlink()
        print('Pending watcher cancelled. Codeforces submissions and Git commits were not removed.')
