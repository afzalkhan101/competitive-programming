"""Local curriculum state shared by the CLI and VS Code dashboard."""
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / '.cf-local'

def read(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default

def write(path, value):
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, indent=2))
    temp.replace(path)

def catalog():
    return read(ROOT / 'practice/catalog.json', {'categories': [], 'problems': []})

def backup():
    return read(ROOT / 'practice/state.json', {})

def progress():
    return dict(backup().get('progress', {}), **read(LOCAL / 'progress.json', {}))

def export_state():
    # Explicit whitelist: never export cookies, credentials, snapshots or absolute paths.
    allowed = {'status', 'submission', 'samplesPassed', 'testedHash', 'updatedAt', 'verdict'}
    data = {pid: {k: v for k, v in fields.items() if k in allowed} for pid, fields in progress().items()}
    active = read(LOCAL / 'active.json', backup().get('active', {}))
    entry = problem(active.get('id', ''))
    config = read(LOCAL / 'config.json', {})
    value = {'version': 1, 'handle': config.get('handle', backup().get('handle', 'afzalkhan101')),
             'progress': data, 'active': {'id': entry['id'], 'source': entry['source']} if entry else {}}
    write(ROOT / 'practice/state.json', value)
    return ROOT / 'practice/state.json'

def problem(pid):
    return next((p for p in catalog()['problems'] if p['id'] == pid.upper()), None)

def next_problem():
    done = progress()
    return next((p for p in catalog()['problems'] if done.get(p['id'], {}).get('status') != 'accepted'), None)

def require_unlocked(pid):
    entry = problem(pid)
    if entry is None:
        return
    frontier = next_problem()
    if frontier and entry['order'] > frontier['order']:
        raise ValueError(f'Locked: solve {frontier["id"]} (#{frontier["order"]}) and verify Accepted first.')

def require_source_unlocked(source):
    relative = Path(source).resolve().relative_to(ROOT.resolve()) if Path(source).resolve().is_relative_to(ROOT.resolve()) else None
    if relative and len(relative.parts) == 3 and relative.parts[0] == 'problems':
        require_unlocked(relative.parts[1])

def accept(pid, submission):
    mark(pid, status='accepted', submission=submission, pushed=False)
    following = next_problem()
    if following:
        select(following['id'])


def select(pid):
    entry = problem(pid)
    if entry is None:
        raise ValueError('Problem is not in the local curriculum.')
    require_unlocked(pid)
    write(LOCAL / 'active.json', {'id': entry['id'], 'source': entry['source']})
    return entry

def active_source():
    active = read(LOCAL / 'active.json', backup().get('active', {}))
    source = ROOT / active.get('source', '')
    if source.is_file() and source.resolve().is_relative_to(ROOT.resolve()):
        require_source_unlocked(source)
        return source
    return None

def mark(pid, **fields):
    data = progress()
    data[pid] = dict(data.get(pid, {}), **fields, updatedAt=time.time())
    write(LOCAL / 'progress.json', data)

def test_result(source, ok):
    metadata = source.parent / 'metadata.json'
    if metadata.exists():
        entry = read(metadata)
        import hashlib
        mark(entry['id'], samplesPassed=ok, testedHash=hashlib.sha256(source.read_bytes()).hexdigest())

def status():
    data = catalog()
    data['progress'] = progress()
    data['active'] = read(LOCAL / 'active.json', backup().get('active', {}))
    data['next'] = next_problem()
    return data
