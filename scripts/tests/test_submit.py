import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cf_submit as submit

class SubmitTests(unittest.TestCase):
    def test_only_accepted_can_reach_git(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(submit, 'LOCAL', Path(directory)), patch.object(submit, 'accepted_push') as push:
            for verdict in ['WRONG_ANSWER', 'TIME_LIMIT_EXCEEDED', 'COMPILATION_ERROR', 'RUNTIME_ERROR', 'FAILED']:
                with self.assertRaises(ValueError):
                    submit.finish_verdict({}, verdict)
                push.assert_not_called()
            submit.finish_verdict({}, 'OK', 'message')
            push.assert_called_once_with({'verifiedVerdict': 'OK'}, 'message')

    def test_exact_account_problem_and_new_id(self):
        state = dict(baseline=100, contest='4', index='A', handle='example')
        def row(number, index='A', handle='example'):
            return dict(id=number, problem=dict(contestId=4, index=index), author=dict(members=[dict(handle=handle)]))
        rows = [row(99), row(101, index='B'), row(102, handle='someone'), row(103)]
        self.assertEqual([r['id'] for r in submit.candidates(rows, state)], [103])

    def test_edited_source_never_pushes(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(submit, 'ROOT', Path(directory)), patch.object(submit, 'git') as git:
            source = Path(directory) / 'main.cpp'
            source.write_text('changed')
            with self.assertRaisesRegex(ValueError, 'Source changed'):
                submit.accepted_push(dict(source='main.cpp', sha256=submit.digest(b'original')), '')
            git.assert_not_called()

    def test_missing_statement_never_stages_or_pushes(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(submit, 'ROOT', Path(directory)), patch.object(submit, 'git', side_effect=['main', 'head', '']) as git:
            source = Path(directory) / 'main.cpp'
            source.write_bytes(b'original')
            sha = submit.digest(b'original')
            state = dict(source='main.cpp', sha256=sha, branch='main', head='head', verifiedVerdict='OK', verifiedSourceHash=sha)
            with self.assertRaisesRegex(ValueError, 'statement is missing'):
                submit.accepted_push(state, '')
            self.assertEqual(git.call_count, 3)

    def test_changed_head_never_stages(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(submit, 'ROOT', Path(directory)), patch.object(submit, 'git', side_effect=['main', 'different-head']) as git:
            source = Path(directory) / 'main.cpp'
            source.write_bytes(b'original')
            state = dict(source='main.cpp', sha256=submit.digest(b'original'), branch='main', head='old-head')
            with self.assertRaisesRegex(ValueError, 'HEAD changed'):
                submit.accepted_push(state, '')
            self.assertEqual(git.call_count, 2)

if __name__ == '__main__':
    unittest.main()
