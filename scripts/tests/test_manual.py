import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import manual_workflow as manual
import practice
import cf_submit

class ManualTests(unittest.TestCase):
    def test_submit_copies_and_opens_without_api_or_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'main.cpp';source.write_text('int main(){}')
            with patch.object(manual,'current_problem',return_value=(source,'problems/4A/main.cpp','4','A')),patch.object(manual,'archive_pending'),patch.object(cf_submit,'clipboard_command',return_value=['pbcopy']),patch.object(manual.subprocess,'run') as run,patch.object(manual.webbrowser,'open') as browser,patch.object(cf_submit,'api') as api,patch.object(cf_submit,'git') as git:
                manual.submit()
                browser.assert_called_once_with('https://codeforces.com/problemset/submit?contestId=4&problemIndex=A')
                run.assert_called_once_with(['pbcopy'],input=b'int main(){}',check=True)
                api.assert_not_called();git.assert_not_called()

    def test_manual_push_and_failed_push_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'repo';remote=Path(tmp)/'remote.git';local=root/'.cf-local'
            def run(*args):return subprocess.check_output(args,stderr=subprocess.STDOUT,text=True).strip()
            run('git','init','--bare',str(remote));run('git','init','-b','main',str(root))
            def git(*args):return run('git','-C',str(root),*args)
            git('config','user.name','Test');git('config','user.email','test@example.invalid')
            (root/'.gitignore').write_text('.cf-local/\n');git('add','.gitignore');git('commit','-m','Initial');git('remote','add','origin',str(remote))
            source=root/'problems/4A/main.cpp';source.parent.mkdir(parents=True);source.write_text('int main(){}\n');(source.parent/'problem.md').write_text('# Statement\n')
            (root/'practice').mkdir();(root/'practice/catalog.json').write_text(json.dumps({'problems':[{'id':'4A','order':1,'source':'problems/4A/main.cpp'},{'id':'9A','order':2,'source':'problems/9A/main.cpp'}]}))
            with patch.object(manual,'ROOT',root),patch.object(practice,'ROOT',root),patch.object(practice,'LOCAL',local),patch.object(cf_submit,'ROOT',root),patch.object(manual,'current_problem',return_value=(source,'problems/4A/main.cpp','4','A')),patch.object(cf_submit,'api') as api:
                practice.select('4A')
                original=subprocess.run
                def fail_push(args,**kwargs):
                    if args[0]=='git' and 'push' in args:raise subprocess.CalledProcessError(1,args)
                    return original(args,**kwargs)
                with patch.object(manual.subprocess,'run',side_effect=fail_push):
                    with self.assertRaises(subprocess.CalledProcessError):manual.push()
                head=git('rev-parse','HEAD');self.assertEqual(practice.read(local/'active.json')['id'],'4A')
                manual.push();self.assertEqual(head,git('rev-parse','HEAD'))
                self.assertEqual(practice.read(local/'active.json')['id'],'9A')
                files=run('git','--git-dir',str(remote),'ls-tree','-r','--name-only','main')
                for path in ['problems/4A/main.cpp','problems/4A/problem.md','practice/state.json']:self.assertIn(path,files)
                api.assert_not_called()

if __name__=='__main__':unittest.main()
