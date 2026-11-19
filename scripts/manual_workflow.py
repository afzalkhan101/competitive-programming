"""Manual browser submission and user-requested GitHub push, without verdict polling."""
from pathlib import Path
import subprocess
import time
import webbrowser

ROOT = Path(__file__).resolve().parent.parent

def current_problem():
    from runcode import selected_source
    from practice import require_source_unlocked
    source = selected_source().resolve()
    if not source.is_relative_to(ROOT.resolve()):
        raise ValueError('Select a problem in this repository first.')
    relative = source.relative_to(ROOT)
    if len(relative.parts) != 3 or relative.parts[0] != 'problems':
        raise ValueError('Select a problem first: cf open 4A')
    require_source_unlocked(source)
    from cf import identifier
    contest, index = identifier(relative.parts[1])
    return source, str(relative), contest, index

def archive_pending():
    local = ROOT / '.cf-local'
    pending = local / 'pending.json'
    if pending.exists():
        pending.rename(local / f'legacy-pending-{time.time_ns()}.json')

def submit():
    source, _, contest, index = current_problem()
    data = source.read_bytes()
    if not data.strip():
        raise ValueError('Save your code before submitting.')
    archive_pending()
    from cf_submit import clipboard_command
    try:
        subprocess.run(clipboard_command(), input=data, check=True)
        print('Code copied to clipboard.')
    except (OSError, ValueError, subprocess.CalledProcessError):
        print('Clipboard unavailable. Copy your saved code from VS Code.')
    url = f'https://codeforces.com/problemset/submit?contestId={contest}&problemIndex={index}'
    webbrowser.open(url)
    print(f'{contest}{index}: {url}')
    print('Choose GNU C++17, paste your code and Submit. Check the verdict yourself.')
    print('After Accepted, run push this. No ID or source verification is required.')

def push(message=''):
    source, relative, contest, index = current_problem()
    statement = source.parent / 'problem.md'
    if not statement.is_file() or not statement.read_text().strip():
        raise ValueError('Restore problem.md before pushing.')
    from cf_submit import git
    if git('diff', '--cached', '--name-only'):
        raise ValueError('Other changes are staged. Commit or unstage them before pushing this problem.')
    branch = git('branch', '--show-current')
    if not branch:
        raise ValueError('Check out a Git branch first.')
    archive_pending()
    import practice
    # The user checks Accepted on Codeforces before explicitly invoking this command.
    # This is a manual completion record, not an API-verified verdict.
    if practice.progress().get(contest + index, {}).get('acceptance') != 'user-confirmed':
        practice.mark(contest + index, status='accepted', acceptance='user-confirmed', pushed=False)
    backup = practice.export_state()
    paths = [relative, str(statement.relative_to(ROOT)), str(backup.relative_to(ROOT))]
    git('add', '--', *paths)
    changed = subprocess.run(['git','-C',str(ROOT),'diff','--cached','--quiet','--',*paths]).returncode
    if changed not in (0, 1):
        raise ValueError('Could not inspect staged changes; nothing pushed.')
    if changed:
        git('commit','-m', message or f'Solve {contest}{index} (manually accepted)','--',*paths)
    subprocess.run(['git','-C',str(ROOT),'push','origin',f'HEAD:refs/heads/{branch}'],check=True)
    practice.mark(contest + index, pushed=True)
    following = practice.next_problem()
    if following:
        practice.select(following['id'])
    print(f'{contest}{index}: solution, statement and progress pushed to GitHub.')
