import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import cf_submit as submission
import practice

ROOT = Path(__file__).resolve().parents[2]

class LibraryTests(unittest.TestCase):
    def test_complete_unique_offline_library(self):
        catalog = json.loads((ROOT/'practice/catalog.json').read_text())
        self.assertEqual(len(catalog['problems']),500)
        aliases = set()
        for category in catalog['categories']:
            entries = [p for p in catalog['problems'] if p['category']==category['id']]
            self.assertEqual(len(entries),100)
            self.assertEqual([p['rating'] for p in entries], sorted(p['rating'] for p in entries))
        for p in catalog['problems']:
            ids = {p['datasetId'], *p['aliases']}
            self.assertFalse(ids & aliases, p['id'])
            aliases |= ids
            self.assertTrue((ROOT/p['source']).is_file())
            text = (ROOT/p['statement']).read_text()
            self.assertIn('## Input',text)
            self.assertIn('## Output',text)
            self.assertGreater(len(text),300)
            folder = (ROOT/p['source']).parent/'samples'
            self.assertEqual(len(list(folder.glob('*.in'))),p['samples'])
            for i, hashes in enumerate(p['sampleHashes'],1):
                for suffix,key in [('.in','input'),('.out','output')]:
                    self.assertEqual(hashlib.sha256((folder/f'{i}{suffix}').read_bytes()).hexdigest(),hashes[key])

    def test_resume_and_next_are_persistent(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(practice,'LOCAL',Path(tmp)):
            first = practice.next_problem()
            practice.select(first['id'])
            self.assertEqual(practice.active_source(), ROOT/first['source'])
            practice.mark(first['id'],status='accepted')
            self.assertNotEqual(practice.next_problem()['id'],first['id'])
            practice.mark(first['id'],samplesPassed=True)
            self.assertEqual(practice.progress()[first['id']]['status'],'accepted')

    def test_sequence_lock_and_accept_unlock(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(practice, 'LOCAL', Path(tmp)):
            first, second, third = practice.catalog()['problems'][:3]
            practice.select(first['id'])
            for entry in [second, third]:
                with self.assertRaisesRegex(ValueError, 'Locked'):
                    practice.select(entry['id'])
                with self.assertRaisesRegex(ValueError, 'Locked'):
                    practice.require_source_unlocked(ROOT / entry['source'])
            practice.mark(first['id'], samplesPassed=True)
            with self.assertRaisesRegex(ValueError, 'Locked'):
                practice.select(second['id'])
            practice.accept(first['id'], 123)
            self.assertEqual(practice.active_source(), ROOT / second['source'])
            practice.select(first['id'])  # accepted problems remain available for review
            practice.select(second['id'])
            with self.assertRaisesRegex(ValueError, 'Locked'):
                practice.select(third['id'])


    def test_portable_state_restores_without_private_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'practice').mkdir()
            (root/'practice/catalog.json').write_text((ROOT/'practice/catalog.json').read_text())
            with patch.object(practice,'ROOT',root), patch.object(practice,'LOCAL',root/'private'):
                practice.write(practice.LOCAL/'config.json', {'handle':'example','secret':'never-export'})
                practice.mark('4A',status='accepted',submission=789,cookie='never-export')
                practice.select('9A')
                state_file=practice.export_state()
                saved=json.loads(state_file.read_text())
                self.assertNotIn('never-export',state_file.read_text())
                self.assertEqual(saved['active']['id'],'9A')
                import shutil
                shutil.rmtree(practice.LOCAL)
                self.assertEqual(practice.progress()['4A']['status'],'accepted')
                self.assertEqual(practice.next_problem()['id'],'9A')


class WatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.local = self.root/'private';self.local.mkdir()
        self.source = self.root/'problems/4A/main.cpp';self.source.parent.mkdir(parents=True)
        self.source.write_text('int main(){}\n')
        self.state = dict(handle='example',contest='4',index='A',source='problems/4A/main.cpp',sha256=submission.digest(self.source.read_bytes()),preparedAt=int(time.time()),submission=123,branch='main',head='head')
        (self.local/'pending.json').write_text(json.dumps(self.state))
        (self.local/'submitted-source.cpp').write_bytes(self.source.read_bytes())
        self.row = dict(id=123,problem=dict(contestId=4,index='A'),author=dict(members=[dict(handle='example')]),creationTimeSeconds=int(time.time()),verdict='OK')
        self.patches = [patch.object(submission,'ROOT',self.root),patch.object(submission,'LOCAL',self.local),patch.object(practice,'accept')]
        for p in self.patches:p.start()
    def tearDown(self):
        for p in self.patches:p.stop()
        self.tmp.cleanup()
    def test_wrong_account_never_pushes(self):
        self.row['author']['members'][0]['handle']='wrong'
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission,'accepted_push') as push:
            with self.assertRaisesRegex(ValueError,'account/problem'):
                submission.watch('123')
            push.assert_not_called()
    def test_old_accepted_submission_never_pushes(self):
        self.row['creationTimeSeconds']=self.state['preparedAt']-60
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission,'accepted_push') as push:
            with self.assertRaisesRegex(ValueError,'predates'):
                submission.watch('123')
            push.assert_not_called()
    def test_source_mismatch_never_pushes(self):
        html=self.root/'submission.html';html.write_text('<a href="/contest/4/submission/123">123</a><pre id="program-source-text">different code</pre>')
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission,'accepted_push') as push:
            with self.assertRaisesRegex(ValueError,'does not match'):
                submission.watch('123',str(html))
            push.assert_not_called()
    def test_matching_source_and_exact_accepted_submission_reach_git(self):
        html=self.root/'submission.html';html.write_text('<a href="/contest/4/submission/123">123</a><pre id="program-source-text">int main(){}\n</pre>')
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission,'accepted_push') as push:
            submission.watch('123',str(html))
            push.assert_not_called()
            saved=json.loads((self.local/'pending.json').read_text())
            self.assertEqual(saved['verifiedSourceHash'],self.state['sha256'])
            self.assertEqual(saved['verifiedVerdict'],'OK')
    def test_cloudflare_never_pushes(self):
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission.urllib.request,'urlopen',side_effect=OSError('403')),patch.object(submission,'accepted_push') as push:
            with self.assertRaisesRegex(ValueError,'source verification is blocked'):
                submission.watch('123')
            push.assert_not_called()
    def test_wrong_answer_never_commits(self):
        self.row['verdict']='WRONG_ANSWER'
        with patch.object(submission,'api',return_value=[self.row]),patch.object(submission,'accepted_push') as push,patch.object(practice,'mark'):
            with self.assertRaisesRegex(ValueError,'WRONG_ANSWER'):
                submission.watch('123')
            push.assert_not_called()
            self.assertFalse((self.local/'pending.json').exists())
    def test_invalid_submission_url(self):
        with self.assertRaises(ValueError):
            submission.parse_submission('https://evil.example/123','4')
        with self.assertRaises(ValueError):
            submission.parse_submission('https://codeforces.com/contest/5/submission/123','4')

class GitIntegrationTests(unittest.TestCase):
    def test_only_verified_source_is_pushed_and_retry_is_safe(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory);repo=base/'repo';remote=base/'remote.git';local=base/'private'
            def run(*args):return subprocess.check_output(args,stderr=subprocess.STDOUT,text=True).strip()
            run('git','init','--bare',str(remote));run('git','init','-b','main',str(repo))
            with patch.object(submission,'ROOT',repo),patch.object(submission,'LOCAL',local),patch.object(practice,'ROOT',repo), patch.object(practice,'LOCAL',local):
                submission.git('config','user.name','Workflow Test');submission.git('config','user.email','test@example.invalid')
                (repo/'README').write_text('initial')
                submission.git('add','README');submission.git('commit','-m','initial');submission.git('remote','add','origin',str(remote));submission.git('push','-u','origin','main')
                (repo/'practice').mkdir()
                (repo/'practice/catalog.json').write_text(json.dumps({'problems':[{'id':'4A','order':1,'source':'problems/4A/main.cpp'}]}))
                source=repo/'problems/4A/main.cpp';source.parent.mkdir(parents=True);source.write_text('int main(){}\n')
                (source.parent/'problem.md').write_text('# Watermelon\n\nProblem statement and sample.\n')
                (repo/'unrelated.cpp').write_text('// untouched')
                sha=submission.digest(source.read_bytes())
                state=dict(source='problems/4A/main.cpp',sha256=sha,branch='main',head=submission.git('rev-parse','HEAD'),contest='4',index='A',submission=123,verifiedSourceHash=sha)
                submission.save(local/'pending.json',state)
                # Simulate a failed first network push, then retry the exact accepted commit.
                original_run=subprocess.run
                def fail_push(args,**kwargs):
                    if args[0]=='git' and 'push' in args:raise subprocess.CalledProcessError(1,args)
                    return original_run(args,**kwargs)
                with patch.object(submission.subprocess,'run',side_effect=fail_push):
                    with self.assertRaises(subprocess.CalledProcessError):submission.finish_verdict(state,'OK')
                committed=submission.git('rev-parse','HEAD')
                saved=json.loads((local/'pending.json').read_text())
                submission.accepted_push(saved)
                self.assertEqual(submission.git('rev-parse','HEAD'),committed)
                files=run('git','--git-dir',str(remote),'ls-tree','-r','--name-only','main')
                self.assertIn('problems/4A/main.cpp',files);self.assertIn('problems/4A/problem.md',files);self.assertNotIn('unrelated.cpp',files)
                self.assertEqual(run('git','--git-dir',str(remote),'show','main:problems/4A/problem.md'), '# Watermelon\n\nProblem statement and sample.')
                self.assertFalse((local/'pending.json').exists())
                backup=json.loads(run('git','--git-dir',str(remote),'show','main:practice/state.json'))
                self.assertEqual(backup['progress']['4A']['status'],'accepted')
                self.assertEqual(backup['progress']['4A']['submission'],123)

if __name__=='__main__':unittest.main()
