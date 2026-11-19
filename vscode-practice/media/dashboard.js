const vscode = acquireVsCodeApi();
let data = null;
let category = 'all';
const $ = id => document.getElementById(id);
const escape = value => String(value ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const button = (type,id,label,cls='secondary') => `<button class="${cls}" data-action="${type}" data-id="${escape(id)}">${label}</button>`;
function tags(problem, compact=false) {
  return `<div class="practice-tags${compact?' compact':''}" aria-label="Category and topic tags"><span class="practice-tag category-tag" data-category="${escape(problem.category)}">${escape(problem.categoryName)}</span>${problem.tags.map(tag=>`<span class="practice-tag">${escape(tag)}</span>`).join('')}</div>`;
}
function render() {
  if (!data) return;
  const accepted = p => data.progress[p.id]?.status === 'accepted';
  const done = data.problems.filter(accepted).length;
  $('done').textContent = `${done} / ${data.problems.length}`;
  $('bar').max = data.problems.length;
  $('bar').value = done;
  $('offline').textContent = `${data.problems.filter(p=>p.offline).length} offline · ${Math.round(done/data.problems.length*100)}% complete`;
  const symbols = ['⌘','∑','↗','▤','◎'];
  $('categories').innerHTML = data.categories.map((c,i)=>`<button class="category ${category===c.id?'active':''}" data-category="${c.id}"><span class="symbol">${symbols[i]}</span><b>${escape(c.name)}</b><small>${data.problems.filter(p=>p.category===c.id && accepted(p)).length} / ${c.count} Accepted</small></button>`).join('');
  const frontier = data.problems.find(p=>p.id===data.next);
  const locked = p => frontier && p.order > frontier.order;
  const active = data.problems.find(p=>p.id === data.active && !accepted(p) && !locked(p));
  const next = active || data.problems.find(p=>p.id === data.next);
  if (next) {
    const result = data.progress[next.id];
    $('next').innerHTML = `<div class="hero"><div class="label">${active?'CONTINUE':'UP NEXT'} · ${String(next.order).padStart(3,'0')} / 500</div><h2>${escape(next.id)} · ${escape(next.title)}</h2>${tags(next)}<p>${escape(next.categoryName)} · Rating ${next.rating} · ${next.samples} original sample${next.samples===1?'':'s'}<br>${result?.samplesPassed?'Previous saved version passed samples. Save and test changes again.':'Read the statement, write your solution, then test the official samples.'}</p><div class="mini">${button('run',next.id,'Run')}${button('test',next.id,'Test samples')}${button('submit',next.id,'Submit')}</div></div><div class="buttons">${button('statement',next.id,'Read Full Statement','primary')}${button('solution',next.id,'Open Solution')}</div>`;
  } else $('next').innerHTML = '<div class="hero"><div class="label">COMPLETE</div><h2>500 problems Accepted.</h2><p>Your practice path is complete. You can revisit any problem below.</p></div>';
  const query = $('search').value.toLowerCase();
  const filter = $('filter').value;
  const rows = data.problems.filter(p=>(category==='all'||p.category===category) && `${p.id} ${p.title} ${p.categoryName} ${p.tags.join(' ')}`.toLowerCase().includes(query) && (filter==='all'||(filter==='accepted'?accepted(p):!accepted(p))));
  $('rows').innerHTML = rows.map(p=>{
    const state = data.progress[p.id];
    const label = locked(p)?'🔒 Locked':accepted(p)?'Accepted':p.id===next?.id?'Next':state?.status==='attempted'?'Attempted':'To do';
    const cls = locked(p)?'locked':accepted(p)?'accepted':p.id===next?.id?'next':state?.status==='attempted'?'attempted':'';
    return `<tr class="${p.id===next?.id?'current':''}"><td>${String(p.order).padStart(3,'0')}</td><td><span class="title">${escape(p.id)} · ${escape(p.title)}</span>${tags(p,true)}</td><td>${p.rating}</td><td><span class="pill ${cls}">${label}</span></td><td class="rowactions">${locked(p)?'<button disabled title="Get Accepted on the previous problems first">Locked</button>':button('statement',p.id,'Read','')+button('solution',p.id,'Code','')}</td></tr>`;
  }).join('');
  $('empty').hidden = rows.length !== 0;
}
document.addEventListener('click',event=>{
  const target = event.target.closest('button');
  if (!target) return;
  if (target.dataset.category) {category=category===target.dataset.category?'all':target.dataset.category;render();}
  else if (target.dataset.action) vscode.postMessage({type:target.dataset.action,id:target.dataset.id});
});
$('search').addEventListener('input',render);
$('filter').addEventListener('change',render);
window.addEventListener('message', event=>{if(event.data.type==='state'){data=event.data;render();}});
vscode.postMessage({type:'ready'});
