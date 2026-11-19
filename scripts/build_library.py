#!/usr/bin/env python3
"""Build the offline curriculum from cached Open R1 statement/example rows."""
import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parent.parent
DATASET = 'https://huggingface.co/datasets/open-r1/codeforces'
TEMPLATE = '''#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <numeric>
#include <map>
#include <set>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Write your solution here.

    return 0;
}
'''
GROUPS = [
    ('basics', 'Basics', {'implementation', 'math', 'strings', 'brute force'}, 800, 1100),
    ('number-theory', 'Number Theory', {'number theory'}, 800, 1900),
    ('algorithms', 'Algorithms', {'greedy', 'binary search', 'two pointers', 'sortings', 'dp'}, 900, 1900),
    ('dsa', 'DSA', {'data structures', 'trees', 'graphs', 'dfs and similar', 'dsu', 'shortest paths'}, 1000, 2100),
    ('mixed', 'Mixed Practice', {'combinatorics', 'geometry', 'bitmasks', 'constructive algorithms', 'strings', 'games'}, 900, 1900),
]

def select(rows):
    selected, used = [], set()
    for group, title, tags, low, high in GROUPS:
        eligible = [r for r in rows if r.get('rating') and low <= r['rating'] <= high
                    and tags.intersection(r.get('tags') or []) and 'interactive' not in (r.get('tags') or [])
                    and r.get('input_mode') == 'stdio' and not r.get('interaction_format')
                    and r.get('description') and r.get('input_format') and r.get('output_format') and r.get('examples')
                    and all(isinstance(e.get('input'), str) and isinstance(e.get('output'), str) for e in r['examples'])
                    and not (set([r['id'], *(r.get('aliases') or [])]) & used)]
        # A rating ladder, with an even spread of topics at each level.
        chosen = []
        if group == 'basics':
            for pid in ['4/A', '71/A', '231/A', '158/A', '50/A', '282/A', '263/A']:
                row = next((r for r in eligible if r['id'] == pid), None)
                if row:
                    chosen.append(row)
        levels = sorted({r['rating'] for r in eligible})
        quotas = {level: 100 // len(levels) + (i < 100 % len(levels)) for i, level in enumerate(levels)}
        ids = {r['id'] for r in chosen}
        for rating in levels:
            bucket = sorted((r for r in eligible if r['rating'] == rating), key=lambda r: (int(r['contest_id']), r['index']))
            want = max(0, quotas[rating] - sum(r['rating'] == rating for r in chosen))
            for row in bucket:
                aliases = set([row['id'], *(row.get('aliases') or [])])
                local_aliases = {a for r in chosen for a in [r['id'], *(r.get('aliases') or [])]}
                if row['id'] not in ids and not (aliases & (used | local_aliases)) and want:
                    chosen.append(row); ids.add(row['id']); want -= 1
        for row in sorted(eligible, key=lambda r: (r['rating'], int(r['contest_id']), r['index'])):
            if len(chosen) >= 100: break
            if not set([row['id'], *(row.get('aliases') or [])]) & (used | {a for r in chosen for a in [r['id'], *(r.get('aliases') or [])]}):
                chosen.append(row)
        if len(chosen) != 100:
            raise ValueError(f'{title}: expected 100 usable unique rows, got {len(chosen)}')
        chosen.sort(key=lambda r: (r['rating'], 0 if r['id'] == '4/A' else 1, int(r['contest_id']), r['index']))
        for row in chosen:
            used.update([row['id'], *(row.get('aliases') or [])])
            selected.append((group, title, row))
    return selected

def build(cache):
    rows = [r for file in sorted(cache.glob('train-*.json')) for r in json.loads(file.read_text())]
    chosen = select(rows)
    entries = []
    for number, (group, category, row) in enumerate(chosen, 1):
        pid = row['id'].replace('/', '')
        folder = ROOT / 'problems' / pid
        folder.mkdir(parents=True, exist_ok=True)
        source = folder / 'main.cpp'
        if not source.exists(): source.write_text(TEMPLATE)
        sample_dir = folder / 'samples'; sample_dir.mkdir(exist_ok=True)
        # Keep statements reproducible and preserve old manual summaries separately.
        statement = folder / 'problem.md'
        if statement.exists() and not (folder / 'metadata.json').exists():
            shutil.copy2(statement, folder / 'previous-description.md')
        url = f'https://codeforces.com/problemset/problem/{row["contest_id"]}/{row["index"]}'
        text = '<a class="practice-back" href="vscode://local.codeforces-practice/dashboard">← Back to Dashboard</a>\n\n'
        text += f'# {pid} · {row["title"]}\n\n[Codeforces problem]({url}) · Rating {row["rating"]}\n\nTime: {row["time_limit"]} seconds · Memory: {row["memory_limit"]} MB\n\n'
        badges = f'<span class="practice-tag category-tag" data-category="{html.escape(group, quote=True)}">{html.escape(category)}</span>'
        badges += ''.join(f'<span class="practice-tag">{html.escape(tag)}</span>' for tag in row['tags'])
        text += f'<!-- practice-tags:start -->\n<div class="practice-tags" aria-label="Category and topic tags">{badges}</div>\n<!-- practice-tags:end -->\n\n'
        for heading, field in [('Problem', 'description'), ('Input', 'input_format'), ('Output', 'output_format')]:
            text += f'## {heading}\n\n{row[field]}\n\n'
        hashes = []
        for i, example in enumerate(row['examples'], 1):
            inp, out = example['input'], example['output']
            # No generated tests or guessed outputs: preserve the dataset's statement examples.
            (sample_dir / f'{i}.in').write_text(inp)
            (sample_dir / f'{i}.out').write_text(out)
            hashes.append({'input': hashlib.sha256(inp.encode()).hexdigest(), 'output': hashlib.sha256(out.encode()).hexdigest()})
            text += f'## Sample {i}\n\nInput\n\n```text\n{inp.rstrip()}\n```\n\nOutput\n\n```text\n{out.rstrip()}\n```\n\n'
        if row.get('note'): text += f'## Note\n\n{row["note"]}\n\n'
        text += f'---\nOffline statement and original statement examples from [Open R1 Codeforces dataset]({DATASET}), CC BY 4.0. Original problem by its Codeforces authors. Dataset snapshot; corrections on Codeforces may be newer. No editorials, solutions, generated checkers, or generated tests included.\n'
        statement.write_text(text)
        meta = {'id': pid, 'order': number, 'category': group, 'categoryName': category, 'title': row['title'],
                'rating': row['rating'], 'tags': row['tags'], 'url': url, 'source': f'problems/{pid}/main.cpp',
                'statement': f'problems/{pid}/problem.md', 'samples': len(row['examples']), 'sampleHashes': hashes,
                'dataset': DATASET, 'datasetId': row['id'], 'aliases': row.get('aliases') or [],
                'offline': True, 'timeLimit': row['time_limit'], 'memoryLimit': row['memory_limit']}
        (folder / 'metadata.json').write_text(json.dumps(meta, indent=2))
        entries.append(meta)
    (ROOT / 'practice' / 'catalog.json').write_text(json.dumps({'version': 1, 'categories': [{'id': g, 'name': n, 'count': 100} for g,n,*_ in GROUPS], 'problems': entries}, indent=2))
    print('Created', len(entries), 'problems:', dict(Counter(p['category'] for p in entries)), flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser();parser.add_argument('--cache', type=Path, default=ROOT/'build/problem-rows')
    build(parser.parse_args().cache)
