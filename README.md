<div align="center">
<h1>📚 Your Practice Path</h1>
<p><strong>500 offline Codeforces problems · VS Code dashboard · Step-by-step practice</strong></p>
<p>Read → Code → Run/Test → Manual Submit → নিজে Accepted দেখো → push this</p>
</div>

## শুরু করো

VS Code-এ এই folder খোলো। Terminal-এ:

```sh
source ~/.zshrc
cf dashboard
```

Dashboard না এলে Command Palette → **Developer: Reload Window**, তারপর **Practice: Open Dashboard**। এই README সুন্দর HTML/Markdown preview-তে পড়তে <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> চাপো।

## প্রতিদিনের workflow

<table>
<tr><th>ধাপ</th><th>করণীয়</th></tr>
<tr><td>১. Read</td><td>Dashboard-এর <strong>Read Full Statement</strong> দিয়ে description ও samples পড়ো।</td></tr>
<tr><td>২. Code</td><td><strong>Open Solution</strong> দিয়ে main.cpp-তে solution লিখে Cmd+S দিয়ে save করো।</td></tr>
<tr><td>৩. Run</td><td><code>runcode</code> চালাও; নিজের input দাও।</td></tr>
<tr><td>৪. Test</td><td><code>testcode</code> চালাও; original sample input/output দিয়ে পরীক্ষা হবে।</td></tr>
<tr><td>৫. Submit</td><td>Dashboard-এর <strong>Submit</strong> button বা <code>submit</code> চালাও। Code clipboard-এ copy হবে, সাধারণ browser-এ Codeforces submit page খুলবে।</td></tr>
<tr><td>৬. Verdict</td><td>Browser-এ GNU C++17 বেছে code paste করে Submit চাপো। Accepted হয়েছে কি না <strong>তুমি নিজে দেখবে</strong>।</td></tr>
<tr><td>৭. Push</td><td>Accepted হলে terminal-এ <code>push this</code> চালাও। Solution, statement ও progress GitHub-এ commit/push হবে।</td></tr>
</table>

<strong>সহজ manual workflow:</strong> কোনো submission ID দিতে হবে না। কোনো API polling, snapshot comparison বা Cloudflare source verification default flow-তে নেই। <code>push this</code> Codeforces verdict পরীক্ষা করে না—তুমি Accepted দেখে command দিচ্ছো ধরে নেয়।

```sh
cf open 4A
# solution লিখে save করো
runcode
testcode
submit
# browser-এ paste, Submit এবং Accepted নিজে দেখো
push this
# অথবা custom commit message:
push this "Solve Watermelon"
```

## Commands

| Command | কাজ |
| --- | --- |
| `cf dashboard` | VS Code dashboard |
| `cf next` | প্রথম unfinished problem |
| `cf open 4A` | unlocked local problem খোলে |
| `runcode` | active problem compile/run; তুমি input দেবে |
| `runcode problems/4A/main.cpp` | নির্দিষ্ট unlocked source চালায় |
| `testcode` | active problem-এর সব original sample test |
| `testcode --timeout 5` | প্রতি sample-এ ৫ সেকেন্ড timeout |
| `submit` | code copy ও browser submit page; কোনো automatic submission নয় |
| `push this` | active solution, statement ও portable progress commit/push |
| `cf backup` | portable state export করে; নিজে Git push করে না |
| `cf status` | catalogue ও progress JSON |
| `cf setup afzalkhan101` | handle configure করে; browser login আলাদা |

Dashboard-এর Run/Test/Submit buttons আগে open files save করে। Terminal commands-এর আগে নিজে save করো। Unlocked curriculum source save করলে সেটি active হয়। Input শেষ করতে প্রয়োজনমতো Ctrl+D, program থামাতে Ctrl+C।

## Sample test-এর নিয়ম

প্রতিটি stored original sample input-এ code চালিয়ে expected sample output-এর সঙ্গে মিলিয়ে PASS/FAIL দেখায়। Missing/modified sample hash ধরা হয়। Compile error হলে execution হয় না; default timeout প্রতি sample-এ ৩ সেকেন্ড।

<strong>Sample PASS মানে Accepted নয়।</strong> Hidden tests শুধু Codeforces চালায়। Comparison whitespace উপেক্ষা করে; floating-point tolerance বা special checker reproduce করে না। Alternative valid output sample-এর সঙ্গে না-ও মিলতে পারে। Submit button sample PASS বাধ্যতামূলক করে না—তুমি কখন submit করবে ঠিক করবে।

## Sequence ও progress

<table>
<tr><th>Order</th><th>Category</th><th>Count</th></tr>
<tr><td>001–100</td><td>Basics</td><td>100</td></tr>
<tr><td>101–200</td><td>Number Theory</td><td>100</td></tr>
<tr><td>201–300</td><td>Algorithms</td><td>100</td></tr>
<tr><td>301–400</td><td>DSA</td><td>100</td></tr>
<tr><td>401–500</td><td>Mixed Practice</td><td>100</td></tr>
</table>

শুরুতে 001 খোলা; পরেরগুলো locked। এই manual mode-এ <code>push this</code> দেওয়াকে তোমার <strong>Accepted confirmation</strong> হিসেবে record করা হয়, API-verified verdict হিসেবে নয়। Successful push-এর পর পরের problem সামনে আসে। GitHub push ব্যর্থ হলেও তোমার manual completion record local-এ থাকে; আগে আগের problem-এর push retry শেষ করো। শুধু sample PASS বা Submit button click completion record করে না। পুরোনো completed problem আবার পড়া যায়। Files disk-এ থাকার কারণে Explorer বা আলাদা compiler দিয়ে সরাসরি খোলা আটকানো হয় না।

Category ও original topic tags dashboard ও statement preview-তে animated badges হিসেবে দেখায়। Reduced-motion preference থাকলে animation বন্ধ থাকে; GitHub-এ badge text দেখা যায়।

## GitHub-এ কী যায়

```text
problems/4A/main.cpp       solution
problems/4A/problem.md     statement, constraints, samples ও attribution
practice/state.json       portable progress
```

এই তিনটি path commit হয়; unrelated staged changes থাকলে আগে নিজে commit/unstage করতে হবে। Existing local commits সাধারণ Git push-এর অংশ হিসেবে publish হতে পারে। Browser cookies, password, SSH key, `.venv`, build output ও `.cf-local` Git-এ যায় না। GitHub SSH authentication লাগবে।

## সমস্যা হলে

| সমস্যা | করণীয় |
| --- | --- |
| `command not found` / পুরোনো push flow | `source ~/.zshrc` চালাও; এই clone-এর ভেতর থেকে command দাও |
| Dashboard পুরোনো | Developer: Reload Window → Practice: Open Dashboard |
| Locked | আগের problem Accepted দেখে `push this` দিয়ে completion record করো |
| Clipboard নেই | VS Code থেকে code নিজে copy করো; submit page তবু খুলবে |
| GitHub push failed | SSH/network ঠিক করে আগের problem-এর `push this` retry করো |
| Other changes staged | নিজের staged changes আলাদাভাবে commit/unstage করো |
| Source verification/snapshot-এর পুরোনো error | নতুন flow-তে লাগে না; shell reload করো। `cf submit` পুরোনো pending record archive করে |

পুরোনো `cf watch`/verification helpers compatibility-এর জন্য code-এ থাকতে পারে; এই workflow-তে সেগুলো ব্যবহার করতে হবে না।

## নতুন PC-তে restore

Python 3.10+, Git, C++17 `g++`, VS Code-এর `code` command install করো। macOS বা Linux bash/zsh supported। Linux/WSL clipboard-এর জন্য `wl-clipboard` বা `xclip` desktop setup লাগে; native Windows setup নয়।

```sh
git clone git@github.com:afzalkhan101/competitive-programming.git
cd competitive-programming
python3 scripts/setup.py
source ~/.zshrc         # bash হলে source ~/.bashrc
code .
```

GitHub SSH ও Codeforces browser login নতুন PC-তে আলাদাভাবে configure করো। Setup dashboard install ও portable progress restore করবে। Clone-এর location বদলালেও commands কাজ করে। Pending process, unsynced edits বা login credentials restore হয় না।

Accepted হওয়ার আগেই সব বর্তমান কাজ backup করতে:

```sh
cf backup
git status
git add -A
git commit -m "Back up practice work"
git push origin HEAD
```

## Files ও provenance

<details>
<summary><strong>Folder layout</strong></summary>

```text
practice/catalog.json       500 problem-এর sequence
practice/state.json         portable progress ও active selection
problems/ID/main.cpp        solution
problems/ID/problem.md      local statement
problems/ID/samples/        original sample input/output
problems/ID/metadata.json   provenance ও sample hashes
scripts/                   CLI ও setup
vscode-practice/           local dashboard
.cf-local/                 ignored private local state
build/                     ignored binaries/artifacts
```

</details>

Statement ও original examples: [Open R1 Codeforces dataset](https://huggingface.co/datasets/open-r1/codeforces), CC BY 4.0; original problems Codeforces authors-এর। Dataset snapshot বলে live statement-এর নতুন corrections/formatting ভিন্ন হতে পারে। Generated tests, editorials ও solutions যোগ করা হয়নি। Duplicate aliases ও interactive/file-I/O problems বাদ দেওয়া হয়েছে।

## Developer checks

```sh
python3 -m unittest discover -s scripts/tests -v
python3 scripts/package_extension.py
code --install-extension build/codeforces-practice-1.6.0.vsix --force
```

Statement preview-এর উপরে **← Back to Dashboard** button দিয়ে dashboard-এ ফেরা যায়। Preview toolbar-এর back-arrow command-ও একই dashboard খোলে।
