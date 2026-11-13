#!/usr/bin/env python3
"""Compile and run the most recently saved C++ source in this repository."""
from pathlib import Path
import os
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
if len(sys.argv) > 2:
    sys.exit('Usage: runcode [source.cpp]')
if len(sys.argv) == 2:
    source = Path(sys.argv[1]).resolve()
    if not source.is_file() or source.suffix not in {'.cpp', '.cc', '.cxx'}:
        sys.exit('Choose an existing C++ source file.')
else:
    sources = [p for p in root.rglob('*') if p.suffix in {'.cpp', '.cc', '.cxx'}
               and p.is_file() and not any(part.startswith('.') or part in {'build', 'bin', 'dist'} for part in p.relative_to(root).parts)
               and p.name != 'tempCodeRunnerFile.cpp']
    if not sources:
        sys.exit('No C++ source files found.')
    source = max(sources, key=lambda p: (p.stat().st_mtime_ns, str(p)))
build = root / 'build' / 'runcode'
build.mkdir(parents=True, exist_ok=True)
binary = build / 'program'
print(f'Compiling {source.name}', flush=True)
result = subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', str(source), '-o', str(binary)])
if result.returncode:
    sys.exit(result.returncode)
print('Running (enter input below):', flush=True)
os.execv(str(binary), [str(binary)])
