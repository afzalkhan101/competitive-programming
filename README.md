<div align="center">
<h1>📚 Your Practice Path</h1>
<p><strong>500 offline Codeforces problems · VS Code dashboard · Sequential unlock</strong></p>
<p>Read → Code → Sample Test → Manual Submit → Verify Accepted → GitHub Push</p>
</div>

## ১. প্রথমবার কীভাবে শুরু করবে

VS Code-এ <strong>competitive-programming</strong> folder খোলো। Installed <strong>Your Practice Path</strong> extension dashboard খুলবে। না দেখালে <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> চেপে <code>Developer: Reload Window</code>, তারপর <code>Practice: Open Dashboard</code> চালাও। Folder trusted থাকতে হবে।

VS Code terminal খুলে চালাও:

```sh
cd /Users/laptopheaven/competitive-programming
source ~/.zshrc
cf dashboard
```

<strong>README সুন্দরভাবে পড়তে:</strong> এই ফাইল খোলা অবস্থায় <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> চাপো। Markdown preview-তে headings, tables ও HTML অংশ render হবে; HTML extension হিসেবে rename করার দরকার নেই।

## ২. Problem-এর sequence ও lock

<table>
<tr><th>Order</th><th>Category</th><th>Problems</th></tr>
<tr><td>001–100</td><td>Basics</td><td>100</td></tr>
<tr><td>101–200</td><td>Number Theory</td><td>100</td></tr>
<tr><td>201–300</td><td>Algorithms</td><td>100</td></tr>
<tr><td>301–400</td><td>DSA</td><td>100</td></tr>
<tr><td>401–500</td><td>Mixed Practice</td><td>100</td></tr>
</table>

প্রতিটি category সহজ থেকে কঠিন rating অনুযায়ী সাজানো। শুরুতে শুধু <strong>Problem 001: 4A — Watermelon</strong> unlocked। তার পরের সব problem <strong>🔒 Locked</strong> থাকবে। প্রথমটির <strong>সঠিক submission-এর Accepted verdict ও source match যাচাই</strong> হলে 002 unlock হবে ও সামনে আসবে; একইভাবে 003…500। শুধু sample PASS বা নিজে Submit চাপলে unlock হবে না।

Accepted হওয়ার পর GitHub push ব্যর্থ হলেও যাচাইকৃত acceptance local-এ থাকে ও পরের problem unlocked থাকে। পুরোনো Accepted problem আবার পড়া ও practice করা যায়। Dashboard, <code>cf open</code>, <code>runcode</code>, <code>testcode</code> এবং নতুন submission preparation sequence lock মেনে চলে। Files local disk-এ থাকে—Explorer দিয়ে সরাসরি পড়া বা আলাদা compiler চালানো আটকানোর ব্যবস্থা এটি নয়।

## ৩. প্রতিদিনের পুরো workflow

### Step 1 — Dashboard খোলো

```sh
cf dashboard
```

বর্তমান unfinished problem দেখবে। <strong>Read Full Statement</strong> চাপলে solution-এর পাশে statement preview খুলবে। <strong>Open Solution</strong> চাপলে <code>main.cpp</code> খুলবে। Category ও topic-এর animated badges দেখাবে—যেমন Basics, Math, Brute Force। Motion কমানোর system preference থাকলে animation বন্ধ থাকে।

```sh
cf next           # sequence-এর প্রথম unfinished problem খোলে
cf open 4A        # নির্দিষ্ট unlocked problem খোলে, local library থেকে
```

### Step 2 — Code লিখে save করো

প্রথম problem-এর solution: <code>problems/4A/main.cpp</code>। <kbd>Cmd</kbd> + <kbd>S</kbd> দিয়ে save করো। Curriculum source save করলে সেই unlocked problem active হয়। Dashboard-এর Run/Test/Submit buttons চালানোর আগে open files save করে। Terminal commands চালানোর আগে তোমাকে save করতে হবে।

### Step 3 — নিজের input দিয়ে চালাও

```sh
runcode
```

C++17 দিয়ে compile হবে, তারপর input লিখবে। প্রয়োজনমতো <kbd>Ctrl</kbd> + <kbd>D</kbd> দিয়ে input শেষ বা <kbd>Ctrl</kbd> + <kbd>C</kbd> দিয়ে program বন্ধ করো। Compile error হলে program চলবে না।

```sh
runcode problems/4A/main.cpp   # unlocked file নির্দিষ্ট করে চালানো
```

### Step 4 — Official sample examples দিয়ে test করো

```sh
testcode
testcode problems/4A/main.cpp
testcode --timeout 5
```

প্রতিটি original sample input-এ program চালিয়ে expected sample output-এর সঙ্গে মেলায়। Sample files-এর hash যাচাই হয়; sample বদলে বা মুছে ফেললে test থামে। Default timeout প্রতি sample-এ 3 seconds; এটা Codeforces judge-এর time limit নয়।

<table>
<tr><th>Result</th><th>করণীয়</th></tr>
<tr><td>PASS</td><td>সব sample pass হলে submit করতে পারো; hidden tests বাকি।</td></tr>
<tr><td>FAIL</td><td>Expected/Actual output দেখো, code ঠিক করে save ও test করো।</td></tr>
<tr><td>TIMEOUT</td><td>Infinite loop, input handling বা slow logic পরীক্ষা করো।</td></tr>
<tr><td>Compile/runtime error</td><td>Error ঠিক করে আবার test করো।</td></tr>
</table>

<strong>সীমা:</strong> whitespace পার্থক্য উপেক্ষা করা হয়, কিন্তু floating-point tolerance বা custom checker reproduce হয় না। একাধিক সঠিক output থাকা problem-এ valid output-ও sample-এর সঙ্গে না মিলতে পারে। Sample PASS মানে Accepted নয়।

### Step 5 — Manual submission শুরু করো

```sh
push this
# নিজের commit message চাইলে:
push this "Solve Watermelon"
```

এটা প্রথমে Git state ও সব stored sample পরীক্ষা করে, saved source-এর snapshot রাখে, code clipboard-এ copy করে এবং <strong>সাধারণ browser</strong>-এ submit page খোলে। Codeforces handle <code>afzalkhan101</code> configured আছে। Browser-এ ওই account-এ login করো, <strong>GNU C++17</strong> বেছে copied code paste করো এবং <strong>Submit</strong> চাপো। Website submission manual; automation browser-এর login/CAPTCHA ব্যবহার করা হচ্ছে না।

তারপর terminal যখন চাইবে, <strong>সেই নতুন submission-এর link বা numeric ID</strong> paste করে Enter চাপো। Pending অবস্থায় code, branch বা Git HEAD বদলাবে না।

### Step 6 — Verdict, source verification ও push

Watcher exact submission ID, account, problem ও submission time যাচাই করে verdict দেখে। Accepted হলে server-side submitted source-এর সঙ্গে saved snapshot মেলায়। তারপর:

<ul>
<li><strong>Accepted + source match:</strong> পরের problem unlock ও সামনে আসে। Solution এবং statement একসঙ্গে commit হয়ে GitHub-এ push হয়।</li>
<li><strong>WA/TLE/compile error:</strong> unlock বা push হয় না। Code ঠিক করে আবার চেষ্টা করো।</li>
<li><strong>API/source blocked:</strong> verification শেষ না হওয়া পর্যন্ত unlock বা push হয় না।</li>
</ul>

প্রতি successful push-এ একই commit-এ যায় (portable progress backup-সহ):

```text
problems/4A/main.cpp       ← তোমার accepted solution
problems/4A/problem.md     ← statement, constraints, samples ও attribution
practice/state.json        ← portable progress ও পরের active problem
```

Statement missing/empty হলে commit থামে। অন্য problem, credentials বা unrelated file automatic commit হয় না।

## ৪. Cloudflare/source verification আটকে গেলে

Codeforces source page login বা Cloudflare দিয়ে আটকাতে পারে। তখন Accepted দেখা গেলেও source যাচাই ছাড়া push হবে না। Error-এ দেওয়া <strong>exact submission page</strong> সাধারণ browser-এ খোলো। সেখান থেকে <strong>শুধু submitted source code</strong> copy করে চালাও:

```sh
cf watch YOUR_SUBMISSION_ID --source-clipboard
```

<strong>এটি user-assisted source check:</strong> clipboard-এ Codeforces submission-এর code থাকতে হবে, local editor-এর code নয়। Account/problem/time/Accepted API checks এখানেও বাধ্যতামূলক। বিকল্প হিসেবে source ও submission link-সহ saved submission HTML দেওয়া যায়:

```sh
cf watch YOUR_SUBMISSION_ID --html "/path/to/submission.html"
```

Codeforces API-ও blocked থাকলে অপেক্ষা করে retry করো; blocked checks এড়িয়ে push হবে না।

## ৫. Recovery ও troubleshooting

<table>
<tr><th>সমস্যা</th><th>সমাধান</th></tr>
<tr><td>command not found</td><td><code>source ~/.zshrc</code> চালাও। Command এই folder বা subfolder থেকেই ব্যবহার করো।</td></tr>
<tr><td>Dashboard নেই/পুরোনো দেখাচ্ছে</td><td>Command Palette → Developer: Reload Window → Practice: Open Dashboard।</td></tr>
<tr><td>Locked</td><td>প্রথম unfinished problem-এর Accepted ও source verification শেষ করো; sample PASS যথেষ্ট নয়।</td></tr>
<tr><td>Terminal বন্ধ/timeout/interruption</td><td><code>push this</code> আবার চালাও। Pending check resume করে; নিজে আবার submit করে না।</td></tr>
<tr><td>GitHub push failed</td><td>SSH/network ঠিক করে <code>push this</code> দিয়ে retry করো। একই accepted commit ব্যবহার করবে।</td></tr>
<tr><td>Source changed</td><td>Pending snapshot-এর version restore করো; অথবা <code>cf cancel</code> করে নতুন attempt শুরু করো।</td></tr>
<tr><td>Already running</td><td>অন্য terminal-এর watcher শেষ করো বা Ctrl+C দিয়ে থামাও। একসঙ্গে দুটো watcher চলে না।</td></tr>
<tr><td>Other changes staged / unpushed commits</td><td>নিজের staged/unpushed কাজ আলাদাভাবে ম্যানেজ করো। Workflow সেগুলো স্বয়ংক্রিয়ভাবে মুছে বা publish করে না।</td></tr>
<tr><td>Wrong handle</td><td><code>cf setup YOUR_HANDLE</code>; browser account-ও একই হতে হবে।</td></tr>
</table>

```sh
cf cancel          # local pending tracking archive/clear; submission বা commit delete করে না
cf status          # catalogue ও local progress JSON
cf setup afzalkhan101
```

## ৬. Files, offline access ও privacy

<details>
<summary><strong>Folder layout দেখো</strong></summary>

```text
practice/catalog.json       500 problem-এর sequence, category ও metadata
problems/ID/main.cpp        solution
problems/ID/problem.md      local statement ও sample examples
problems/ID/samples/        original sample input/output
problems/ID/metadata.json   provenance ও sample hashes
scripts/                   CLI, sample runner, verification ও Git flow
vscode-practice/           dashboard extension
.cf-local/                 ignored progress, active problem ও pending snapshots
build/                     ignored compiled binaries ও development artifacts
```

</details>

৫০০টি statement ও sample local-এ আছে; পড়া, লেখা ও test-এর জন্য internet লাগে না। Codeforces submit/verification এবং GitHub push-এর জন্য internet প্রয়োজন। Login password terminal-এ দেওয়া লাগে না। <code>.cf-local/</code> private; share/commit করবে না। Progress local-এ থাকে; portable backup <code>practice/state.json</code>-এ থাকে। Accepted push-এ এই backup-ও যায়। নতুন clone local progress না পেলে backup থেকে sequence restore করে।

Statement ও original <code>examples</code>: <a href="https://huggingface.co/datasets/open-r1/codeforces">Open R1 Codeforces dataset</a>, CC BY 4.0; original problems Codeforces authors-এর। Dataset snapshot বলে formatting বা নতুন corrections live page থেকে ভিন্ন হতে পারে। Generated tests/checkers, editorials বা solutions যোগ করা হয়নি। Duplicate aliases ও interactive/file-I/O problems বাদ দেওয়া হয়েছে। Category tags overlap করতে পারে, problem repeat হয় না। GitHub tags-এর text দেখায়; animation VS Code preview/dashboard-এ হয়।

## ৭. Reinstall ও developer checks

Daily commands-এর জন্য Python 3, C++17 compiler, VS Code ও Git/SSH প্রয়োজন। macOS-এ <code>pbcopy/pbpaste</code>; Linux/WSL desktop-এ <code>wl-clipboard</code> বা <code>xclip</code> প্রয়োজন। Native Windows-এর বদলে WSL ব্যবহার করো; WSL clipboard/browser integration নিজে configure করতে হতে পারে। Python standard library দিয়েই daily CLI চলে; <code>.venv</code> activate করা বাধ্যতামূলক নয়।

```sh
python3 scripts/package_extension.py
code --install-extension build/codeforces-practice-1.3.0.vsix --force
python3 -m unittest discover -s scripts/tests -v
node --check vscode-practice/extension.js
node --check vscode-practice/media/dashboard.js
```

Shell setup পুনরায় লাগলে <code>~/.zshrc</code>-তে loader line থাকতে হবে:

```sh
source /Users/laptopheaven/competitive-programming/scripts/terminal.zsh
```

<blockquote>নিয়ম: Save → Run → Test → Manual Submit → Exact Accepted + Source Check → Next Unlock + Solution/Statement Push। যাচাই ব্যর্থ হলে automatic push হয় না।</blockquote>


## ৮. নতুন PC-তে clone করে আগের workflow চালাও

আগে VS Code (PATH-এ `code` command), Git, Python 3.10+, এবং `g++` C++17 compiler install করো। macOS/Linux bash বা zsh supported; native Windows setup নয়—WSL ব্যবহার করতে হবে। Codeforces browser login ও GitHub SSH key এই PC-তে আলাদাভাবে configure করো। Password, SSH private key বা browser cookies repo-তে থাকে না।

```sh
git clone git@github.com:afzalkhan101/competitive-programming.git
cd competitive-programming
python3 scripts/setup.py
```

Setup শেষের নির্দেশ অনুযায়ী shell reload করো:

```sh
source ~/.zshrc     # zsh হলে
# অথবা bash হলে: source ~/.bashrc
code .
```

VS Code-এ প্রয়োজনে **Developer: Reload Window**, তারপর **Practice: Open Dashboard**। Shell setup clone-এর বর্তমান location ব্যবহার করে; পুরোনো PC-এর absolute path লাগে না। `cf open`, `runcode`, `testcode`, `push this` আগের মতো চলবে। Python `.venv`, downloaded packages বা build binaries copy করার দরকার নেই। Local statement ও samples সব Git-এ আছে।

<strong>কী restore হবে:</strong> 500 problems, code, statements, samples, tags, lock sequence, backed-up acceptance/progress, configured handle ও last backed-up active problem। <strong>কী restore হবে না:</strong> browser login, SSH credentials, running process, private pending submission বা uncommitted/unsynced edits। নতুন PC-তে নতুন করে login করতে হবে।

প্রতি Accepted solution push-এ `practice/state.json`-ও update/push হয়। Accepted হওয়ার আগেই PC বদলালে unsolved code ও active selection backup করতে:

```sh
cf backup
# Changed files review করে explicit Git backup:
git status
git add -A
git commit -m "Back up practice work"
git push origin HEAD
```

এই explicit Git backup Codeforces submission করে না। `.cf-local`, `.venv`, `build` ও credentials ignore-ই থাকবে। নতুন PC-তে clone-এর বদলে পুরোনো checkout update করলে আগে নিজের local কাজ commit/backup করে `git pull --ff-only` করো। Local progress থাকলে সেটি backup-এর ওপর priority পায়; একাধিক PC-তে একই সময়ে practice চালালে local progress conflict নিজে review করতে হবে।
