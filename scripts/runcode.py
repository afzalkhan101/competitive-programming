#!/usr/bin/env python3
"""Compile and run the most recently saved C++ source."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent

def latest_source(root=ROOT):
    sources = [p for p in root.rglob('*') if p.suffix in {'.cpp', '.cc', '.cxx'}
               and p.is_file() and not any(part.startswith('.') or part in {'build', 'bin', 'dist'} for part in p.relative_to(root).parts)
               and p.name != 'tempCodeRunnerFile.cpp']
    if not sources:
        raise ValueError('No C++ source files found.')
    return max(sources, key=lambda p: (p.stat().st_mtime_ns, str(p)))

def selected_source():
    from practice import active_source
    return active_source() or latest_source()


def main():
    if len(sys.argv) > 2:
        sys.exit('Usage: runcode [source.cpp]')
    try:
        source = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else selected_source()
        from practice import require_source_unlocked
        require_source_unlocked(source)
        if not source.is_file() or source.suffix not in {'.cpp', '.cc', '.cxx'}:
            sys.exit('Choose an existing C++ source file.')
        build = ROOT / 'build' / 'runcode'
        build.mkdir(parents=True, exist_ok=True)
        binary = build / 'program'
        print(f'Compiling {source.name}', flush=True)
        result = subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', str(source), '-o', str(binary)])
        if result.returncode:
            return result.returncode
        print('Running (enter input below):', flush=True)
        os.execv(str(binary), [str(binary)])
    except (OSError, ValueError) as exc:
        sys.exit(str(exc))

if __name__ == '__main__':
    sys.exit(main())
