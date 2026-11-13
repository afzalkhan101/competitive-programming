import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cf import parse_problem, identifier

class ImportTests(unittest.TestCase):
    def test_line_wrappers_and_breaks(self):
        html = '''<div class="problem-statement"><div class="header"><div class="title">A. Example</div></div><p>Use &lt; and $$$x$$$.</p><div class="sample-test"><div class="input"><pre><div class="test-example-line">2</div><div class="test-example-line">4 6</div></pre></div><div class="output"><pre>YES<br>NO</pre></div></div></div>'''
        title, body, pairs = parse_problem(html)
        self.assertEqual(title, 'A. Example')
        self.assertIn('$x$', body)
        self.assertEqual(pairs, [('2\n4 6\n', 'YES\nNO\n')])
    def test_reject_challenge(self):
        with self.assertRaises(ValueError):
            parse_problem('<html>Access denied</html>')
    def test_identifiers(self):
        for value in ['4a', 'https://codeforces.com/problemset/problem/4/A', 'https://codeforces.com/contest/4/problem/A']:
            self.assertEqual(identifier(value), ('4', 'A'))
        with self.assertRaises(ValueError):
            identifier('../../oops')

if __name__ == '__main__':
    unittest.main()
