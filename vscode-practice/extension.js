const vscode = require('vscode');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
let panel;
function activate(context) {
  const folder = (vscode.workspace.workspaceFolders || []).find(f => fs.existsSync(path.join(f.uri.fsPath, 'practice/catalog.json')));
  if (!folder) return;
  const root = folder.uri.fsPath;
  const local = path.join(root, '.cf-local');
  const read = (p, fallback) => { try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return fallback; } };
  const catalog = read(path.join(root, 'practice/catalog.json'), {problems: [], categories: []});
  const find = id => catalog.problems.find(p => p.id === id);
  const backup = () => read(path.join(root,'practice/state.json'), {});
  const progress = () => ({...(backup().progress || {}), ...read(path.join(local, 'progress.json'), {})});
  const next = () => catalog.problems.find(p => progress()[p.id]?.status !== 'accepted');
  const unlocked = p => p && (!next() || p.order <= next().order);
  const active = () => find(read(path.join(local, 'active.json'), backup().active || {}).id);
  const select = p => {
    if (!unlocked(p)) throw new Error(`Locked: get verified Accepted for ${next().id} first.`);
    fs.mkdirSync(local, {recursive: true, mode: 0o700});
    fs.writeFileSync(path.join(local, 'active.json.tmp'), JSON.stringify({id:p.id, source:p.source}));
    fs.renameSync(path.join(local, 'active.json.tmp'), path.join(local, 'active.json'));
  };
  const status = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 50);
  status.command = 'practice.dashboard';
  status.tooltip = 'Open Your Practice Path';
  context.subscriptions.push(status);
  function refresh() {
    const done = progress();
    const accepted = catalog.problems.filter(p => done[p.id]?.status === 'accepted').length;
    status.text = `$(book) Practice ${accepted}/${catalog.problems.length}`;
    status.show();
    panel?.webview.postMessage({type:'state', ...catalog, progress:done, active:unlocked(active())?active()?.id:undefined, next:next()?.id});
  }
  async function openProblem(p, statement) {
    if (!p) return;
    select(p);
    const source = vscode.Uri.file(path.join(root, p.source));
    const groups = vscode.window.tabGroups.all;
    const sourceGroup = groups.find(g => g.tabs.some(t => t.input instanceof vscode.TabInputText && t.input.uri.toString() === source.toString()));
    const descriptionGroup = groups.find(g => g.tabs.some(t => t.input instanceof vscode.TabInputWebview && t.input.viewType.includes('markdown.preview')));
    const oldSolutions = groups.flatMap(g => g.tabs).filter(t =>
      !t.isDirty && t.input instanceof vscode.TabInputText &&
      t.input.uri.toString() !== source.toString() &&
      catalog.problems.some(item => vscode.Uri.file(path.join(root, item.source)).toString() === t.input.uri.toString()));
    if (oldSolutions.length) await vscode.window.tabGroups.close(oldSolutions, true);
    panel?.dispose();
    await vscode.window.showTextDocument(source, {viewColumn:sourceGroup?.viewColumn || vscode.ViewColumn.One, preview:false});
    await vscode.commands.executeCommand('markdown.showPreview', vscode.Uri.file(path.join(root, p.statement)), {
      viewColumn: descriptionGroup?.viewColumn || vscode.ViewColumn.Beside,
      locked: true,
      preserveFocus: true
    });
    refresh();
  }
  const quote = s => "'" + s.replace(/'/g, "'\\''") + "'";
  async function terminal(action, p) {
    if (!vscode.workspace.isTrusted) return;
    // Never send an unsaved buffer to compilation or a submission snapshot.
    if (!(await vscode.workspace.saveAll(false))) return;
    if (p) select(p);
    const term = vscode.window.terminals.find(t => t.name === 'Practice') || vscode.window.createTerminal({name:'Practice', cwd:root});
    const py = fs.existsSync(path.join(root, '.venv/bin/python')) ? path.join(root,'.venv/bin/python') : 'python3';
    const commands = {test:[path.join(root,'scripts/cf.py'),'test'], run:[path.join(root,'scripts/runcode.py')], submit:[path.join(root,'scripts/cf.py'),'submit']};
    if (!commands[action]) return;
    term.show();
    term.sendText([py,...commands[action]].map(quote).join(' '));
  }
  function dashboard() {
    if (panel) { panel.reveal(vscode.ViewColumn.One); refresh(); return; }
    panel = vscode.window.createWebviewPanel('practice.dashboard','Your Practice Path',vscode.ViewColumn.One,{enableScripts:true, retainContextWhenHidden:true, localResourceRoots:[vscode.Uri.joinPath(context.extensionUri,'media')]});
    const nonce = crypto.randomBytes(16).toString('hex');
    const asset = f => panel.webview.asWebviewUri(vscode.Uri.joinPath(context.extensionUri,'media',f));
    panel.webview.html = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src ${panel.webview.cspSource}; script-src 'nonce-${nonce}';"><link rel="stylesheet" href="${asset('dashboard.css')}"><link rel="stylesheet" href="${asset('tags.css')}"></head><body><main><header><div class="eyebrow">LOCAL PRACTICE · CODEFORCES</div><h1>Your Practice Path<span>500</span></h1><p>One problem at a time. Pick up where you left off.</p></header><section id="categories" aria-label="Categories"></section><section class="progress"><div><strong id="done">0 / 500</strong><span>Accepted</span><span id="offline"></span></div><progress id="bar" max="500" value="0"></progress></section><section id="next"></section><section class="library"><div class="toolbar"><h2>Your sequence</h2><input id="search" type="search" placeholder="Search name, ID or topic…" aria-label="Search problems"><select id="filter" aria-label="Status"><option value="all">All problems</option><option value="unfinished">Unfinished</option><option value="accepted">Accepted</option></select></div><div class="tablewrap"><table><thead><tr><th>Order</th><th>Problem</th><th>Rating</th><th>Status</th><th>Actions</th></tr></thead><tbody id="rows"></tbody></table></div><p id="empty" hidden>No matching problems.</p></section><footer>Statements and original samples are stored locally. Samples are not hidden tests.<br>Submit in your browser → check Accepted yourself → run push this to publish.</footer></main><script nonce="${nonce}" src="${asset('dashboard.js')}"></script></body></html>`;
    panel.webview.onDidReceiveMessage(async message => {
      try {
        if (message.type === 'ready') return refresh();
        const p = find(message.id);
        if (!p) return;
        if (message.type === 'statement') await openProblem(p, true);
        else if (message.type === 'solution') await openProblem(p, false);
        else if (['test','run','submit'].includes(message.type)) await terminal(message.type,p);
      } catch (e) { vscode.window.showErrorMessage(`Practice: ${e.message}`); }
    },null,context.subscriptions);
    panel.onDidDispose(() => {panel = undefined;},null,context.subscriptions);
  }
  context.subscriptions.push(vscode.commands.registerCommand('practice.dashboard',dashboard));
  context.subscriptions.push(vscode.commands.registerCommand('practice.next',() => openProblem(next(),true).catch(e => vscode.window.showErrorMessage(e.message))));
  context.subscriptions.push(vscode.window.registerUriHandler({handleUri: async uri => {
    if (uri.path === '/dashboard') dashboard();
    if (uri.path === '/open') { try { await openProblem(find(new URLSearchParams(uri.query).get('id')),true); } catch(e) {vscode.window.showErrorMessage(e.message);} }
  }}));
  context.subscriptions.push(vscode.workspace.onDidSaveTextDocument(doc => {
    const rel = path.relative(root,doc.uri.fsPath).split(path.sep).join('/');
    const p = catalog.problems.find(p => p.source === rel);
    if (p && unlocked(p)) {select(p);refresh();}
  }));
  const watcher = vscode.workspace.createFileSystemWatcher(new vscode.RelativePattern(root,'.cf-local/{progress,active}.json'));
  watcher.onDidChange(refresh);watcher.onDidCreate(refresh);watcher.onDidDelete(refresh);
  context.subscriptions.push(watcher);
  refresh();
  if (vscode.workspace.getConfiguration('practice').get('openOnStartup',true)) dashboard();
  else openProblem(active() || next(), true).catch(e => vscode.window.showErrorMessage(`Practice: ${e.message}`));
}
module.exports = {activate};
