#!/usr/bin/env python3
"""Install this clone's dashboard and restore portable practice state."""
import argparse
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import os

ROOT = Path(__file__).resolve().parent.parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shell', choices=['zsh', 'bash'], default=Path(os.environ.get('SHELL', '/bin/zsh')).name if Path(os.environ.get('SHELL', '/bin/zsh')).name in {'zsh','bash'} else 'bash')
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        sys.exit('Python 3.10 or later is required.')
    missing = [cmd for cmd in ['git','g++','code'] if not shutil.which(cmd)]
    if missing:
        sys.exit('Install required commands first: ' + ', '.join(missing) + '. For VS Code enable its code command in PATH.')
    import practice
    state = practice.backup()
    config = practice.LOCAL/'config.json'
    if not config.exists():
        practice.write(config, {'handle':state.get('handle','afzalkhan101')})
    if not (practice.LOCAL/'active.json').exists():
        entry = practice.problem(state.get('active',{}).get('id','')) or practice.next_problem()
        if entry:
            try: practice.select(entry['id'])
            except ValueError:
                next_entry=practice.next_problem()
                if next_entry:practice.select(next_entry['id'])
    subprocess.run([sys.executable,str(ROOT/'scripts/package_extension.py')],check=True)
    version=json.loads((ROOT/'vscode-practice/package.json').read_text())['version']
    subprocess.run(['code','--install-extension',str(ROOT/f'build/codeforces-practice-{version}.vsix'),'--force'],check=True)
    rc = Path.home()/('.zshrc' if args.shell=='zsh' else '.bashrc')
    loader = 'source ' + shlex.quote(str(ROOT/'scripts/terminal.zsh'))
    text=rc.read_text() if rc.exists() else ''
    lines = text.splitlines()
    # Update a loader pointing at an old checkout rather than leaving two conflicting paths.
    lines=[line for line in lines if not (line.strip().startswith(('source ', '. ')) and 'scripts/terminal.zsh' in line and 'competitive-programming' in line)]
    if loader not in lines:
        lines.extend(['', '# Competitive programming practice', loader])
    rc.write_text('\n'.join(lines)+'\n')
    print(f'Setup complete. Run: source {shlex.quote(str(rc))}')
    print('Then: cf dashboard (reload the VS Code window if needed).')
    print('Codeforces browser login and GitHub SSH authentication must be configured separately on this PC.')

if __name__=='__main__':main()
