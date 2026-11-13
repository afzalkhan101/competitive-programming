#!/usr/bin/env python3
"""Local Codeforces workspace, sample runner, and browser submission workflow."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent.parent

class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []
    def find(self, cls):
        result = [self] if cls in self.attrs.get('class', '').split() else []
        for child in self.children:
            if isinstance(child, Node):
                result.extend(child.find(cls))
        return result
    def text(self):
        if self.tag == 'br':
            return '\n'
        value = ''.join(c.text() if isinstance(c, Node) else c for c in self.children)
        if self.tag == 'div' and 'test-example-line' in self.attrs.get('class', ''):
            return value + '\n'
        return value

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.current = Node()
    def handle_starttag(self, tag, attrs):
        child = Node(tag, attrs, self.current)
        self.current.children.append(child)
        if tag not in {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'base', 'embed', 'param', 'col'}:
            self.current = child
    def handle_endtag(self, tag):
        node = self.current
        while node.parent:
            if node.tag == tag:
                self.current = node.parent
                return
            node = node.parent
    def handle_data(self, data):
        self.current.children.append(data)

def descendants(node, tag):
    result = [node] if node.tag == tag else []
    for c in node.children:
        if isinstance(c, Node):
            result.extend(descendants(c, tag))
    return result

def markdown(node):
    if isinstance(node, str):
        return node.replace('$$$', '$')
    value = ''.join(markdown(c) for c in node.children)
    if node.tag == 'br':
        return '\n'
    if node.tag == 'img':
        src = node.attrs.get('src', '')
        if src.startswith('/'):
            src = 'https://codeforces.com' + src
        return f"![{node.attrs.get('alt', 'diagram')}]({src})"
    if node.tag in {'p', 'div', 'ul', 'ol', 'table', 'tr'}:
        return '\n\n' + value.strip() + '\n\n'
    if node.tag == 'li':
        return '\n- ' + value.strip()
    if node.tag in {'b', 'strong'}:
        return '**' + value + '**'
    if node.tag == 'a':
        return f"[{value}]({node.attrs.get('href', '')})"
    return value

def parse_problem(html):
    parser = Parser()
    parser.feed(html)
    statements = parser.root.find('problem-statement')
    if not statements:
        raise ValueError('No problem statement found. Save the actual problem page as HTML after it loads in your browser.')
    statement = statements[0]
    titles = statement.find('title')
    title = titles[0].text().strip() if titles else 'Problem'
    sample_blocks = statement.find('sample-test')
    pairs = []
    for block in sample_blocks:
        inputs, outputs = block.find('input'), block.find('output')
        if len(inputs) != len(outputs):
            raise ValueError('Incomplete sample input/output pairs.')
        for inp, out in zip(inputs, outputs):
            a, b = descendants(inp, 'pre'), descendants(out, 'pre')
            if not a or not b:
                raise ValueError('Sample format not recognized.')
            pairs.append((a[0].text().strip('\r\n') + '\n', b[0].text().strip('\r\n') + '\n'))
    if not pairs:
        raise ValueError('No samples found; no files were created.')
    return title, re.sub(r'\n{3,}', '\n\n', markdown(statement)).strip(), pairs

def identifier(value):
    match = re.fullmatch(r'(\d+)([A-Za-z]\d*)', value)
    if not match:
        match = re.fullmatch(r'https://codeforces.com/(?:problemset/problem/(\d+)/|contest/(\d+)/problem/)([A-Za-z]\d*)/?', value)
        if not match:
            raise ValueError('Use a problem ID such as 4A or a Codeforces problem URL.')
        return (match[1] or match[2]), match[3].upper()
    return match[1], match[2].upper()

def open_problem(args):
    contest, index = identifier(args.problem)
    from practice import require_unlocked
    require_unlocked(contest + index)
    from practice import problem, select
    entry = problem(contest + index)
    if entry and not args.html:
        select(entry['id'])
        print(f'Offline problem ready: {entry["id"]} · {entry["title"]}')
        if not args.no_editor and shutil.which('code'):
            subprocess.run(['code', '--reuse-window', '--open-url', 'vscode://local.codeforces-practice/open?id=' + entry['id']], check=False)
        return
    url = f'https://codeforces.com/problemset/problem/{contest}/{index}'
    if args.html:
        html = Path(args.html).read_text(encoding='utf-8')
    else:
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(request, timeout=25) as response:
                html = response.read().decode('utf-8')
        except (urllib.error.URLError, TimeoutError) as exc:
            raise ValueError(f'Download failed: {exc}\nOpen {url} in your browser, save the loaded page as HTML, then run:\ncf open {contest}{index} --html "/path/to/saved.html"') from exc
    title, body, samples = parse_problem(html)
    folder = ROOT / 'problems' / f'{contest}{index}'
    folder.mkdir(parents=True, exist_ok=True)
    # Keep existing statements and sample sets intact on repeat opens.
    statement = folder / 'problem.md'
    if not statement.exists():
        statement.write_text(f'# {contest}{index} · {title}\n\n[Original problem]({url})\n\n{body}\n', encoding='utf-8')
    sample_dir = folder / 'samples'
    if not sample_dir.exists():
        sample_dir.mkdir()
        for n, (inp, out) in enumerate(samples, 1):
            (sample_dir / f'{n}.in').write_text(inp, encoding='utf-8')
            (sample_dir / f'{n}.out').write_text(out, encoding='utf-8')
    source = folder / 'main.cpp'
    if not source.exists():
        source.write_text('#include <iostream>\n#include <vector>\n#include <algorithm>\n#include <string>\nusing namespace std;\n\nint main() {\n    ios::sync_with_stdio(false);\n    cin.tie(nullptr);\n\n    // Write your solution here.\n\n    return 0;\n}\n', encoding='utf-8')
    state = ROOT / 'build' / 'cf-active.json'
    state.parent.mkdir(exist_ok=True)
    state.write_text(json.dumps({'source': str(source)}))
    print(f'Ready: {folder.relative_to(ROOT)} ({len(samples)} samples)')
    print('Edit main.cpp, save, then run testcode. Samples do not cover hidden tests.')
    if not args.no_editor and shutil.which('code'):
        subprocess.run(['code', '--reuse-window', str(ROOT), str(source), str(statement)], check=False)
        print('For side-by-side statement preview: select problem.md and press Cmd+K, then V.')

def test(args):
    if args.source:
        source = Path(args.source).resolve()
    else:
        from runcode import selected_source
        source = selected_source()
    from practice import require_source_unlocked
    require_source_unlocked(source)
    samples = source.parent / 'samples'
    inputs = sorted(samples.glob('*.in'))
    if not inputs:
        raise ValueError(f'No samples for {source}. Use cf open first or specify testcode problems/4A/main.cpp.')
    metadata_path = source.parent / 'metadata.json'
    if metadata_path.exists():
        import hashlib
        metadata = json.loads(metadata_path.read_text())
        if len(inputs) != metadata['samples']:
            raise ValueError('Sample set differs from the stored original examples. Restore the sample files before testing.')
        for i, hashes in enumerate(metadata['sampleHashes'], 1):
            for suffix, key in [('.in', 'input'), ('.out', 'output')]:
                file = samples / (str(i) + suffix)
                if not file.exists() or hashlib.sha256(file.read_bytes()).hexdigest() != hashes[key]:
                    raise ValueError(f'Original sample was modified or is missing: {file}')
    for inp in inputs:
        if not inp.with_suffix('.out').is_file():
            raise ValueError(f'Missing expected output: {inp.with_suffix(".out")}')
    build = ROOT / 'build' / 'testcode'
    build.mkdir(parents=True, exist_ok=True)
    binary = build / 'program'
    compile_result = subprocess.run(['g++', '-std=c++17', '-Wall', '-Wextra', str(source), '-o', str(binary)])
    if compile_result.returncode:
        from practice import test_result
        test_result(source, False)
        return compile_result.returncode
    passed = 0
    print(f'Testing {source.relative_to(ROOT) if source.is_relative_to(ROOT) else source}')
    for inp in inputs:
        expected = inp.with_suffix('.out').read_text()
        start = time.monotonic()
        try:
            with inp.open() as stdin, (build / 'stdout').open('w+') as stdout, (build / 'stderr').open('w+') as stderr:
                result = subprocess.run([str(binary)], stdin=stdin, stdout=stdout, stderr=stderr, timeout=args.timeout, cwd=source.parent)
                stdout.seek(0)
                actual = stdout.read(65536)
                stdout.seek(0, 2)
                too_large = stdout.tell() > 65536
                stderr.seek(0)
                error = stderr.read(2000)
            ok = result.returncode == 0 and not too_large and actual.split() == expected.split()
            print(f'{inp.stem}: {"PASS" if ok else "FAIL"} ({time.monotonic()-start:.3f}s)')
            if ok:
                passed += 1
            else:
                print(f'Expected:\n{expected[:2000]}Actual:\n{actual[:2000]}')
                if result.returncode:
                    print(f'Exit code: {result.returncode}\n{error}')
                if too_large:
                    print('Output exceeds 64 KiB display/comparison limit.')
        except subprocess.TimeoutExpired:
            print(f'{inp.stem}: TIMEOUT ({args.timeout}s)')
    from practice import test_result
    test_result(source, passed == len(inputs))
    print(f'{passed}/{len(inputs)} samples passed. Hidden tests run on Codeforces.')
    return 0 if passed == len(inputs) else 1

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    opening = commands.add_parser('open', help='Download a problem or import saved HTML')
    opening.add_argument('problem')
    opening.add_argument('--html', help='Import a problem page saved by your browser')
    opening.add_argument('--no-editor', action='store_true')
    testing = commands.add_parser('test', help='Compile and compare sample outputs')
    testing.add_argument('source', nargs='?')
    testing.add_argument('--timeout', type=float, default=3)
    configuring = commands.add_parser('setup', help='Set your Codeforces handle; no automated browser login')
    configuring.add_argument('handle')
    submitting = commands.add_parser('submit', help='Submit latest problem and push only after Accepted')
    submitting.add_argument('message', nargs='?', default='')
    commands.add_parser('backup', help='Export portable progress/active problem without private credentials')
    commands.add_parser('cancel', help='Cancel pending local submission tracking')
    commands.add_parser('status', help='Show curriculum progress')
    commands.add_parser('next', help='Select the first unfinished problem')
    commands.add_parser('dashboard', help='Open the VS Code practice dashboard')
    watching = commands.add_parser('watch', help='Verify an exact manual submission and push after Accepted')
    watching.add_argument('submission', nargs='?')
    watching.add_argument('--html', help='Saved submission page containing server-side source')
    watching.add_argument('--source-clipboard', action='store_true', help='Read source copied from your Codeforces submission page')
    watching.add_argument('--timeout', type=float, default=600)
    args = parser.parse_args()
    if getattr(args, 'timeout', 1) <= 0:
        parser.error('--timeout must be positive')
    try:
        if args.command == 'backup':
            import practice
            print(practice.export_state())
            return
        if args.command == 'cancel':
            import cf_submit
            return cf_submit.cancel()
        if args.command == 'watch':
            import cf_submit
            return cf_submit.watch(args.submission, args.html, args.source_clipboard, args.timeout)
        if args.command == 'status':
            import practice
            data = practice.status()
            print(json.dumps(data, indent=2))
            return
        if args.command == 'next':
            import practice
            entry = practice.next_problem()
            if entry:
                args.problem, args.html, args.no_editor = entry['id'], None, False
                return open_problem(args)
            print('All 500 problems Accepted!')
            return
        if args.command == 'dashboard':
            subprocess.run(['code', '--reuse-window', '--open-url', 'vscode://local.codeforces-practice/dashboard'], check=True)
            return
        if args.command in {'setup', 'submit'}:
            import cf_submit
            return cf_submit.setup(args.handle) if args.command == 'setup' else cf_submit.submit(args.message)
        return open_problem(args) if args.command == 'open' else test(args)
    except (ValueError, OSError, subprocess.CalledProcessError, ImportError) as exc:
        print(exc, file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
