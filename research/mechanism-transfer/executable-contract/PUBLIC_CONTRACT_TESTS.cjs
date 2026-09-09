const fs = require('fs');
const { JSDOM } = require('jsdom');

function boot() {
  let html = fs.readFileSync('index.html', 'utf8');
  html = html.replace(/<script\s+src=["']app\.js["']\s*><\/script>/i, '');
  const dom = new JSDOM(html, {
    url: 'https://public-contract.test/',
    runScripts: 'outside-only',
    pretendToBeVisual: true,
  });
  dom.window.scrollTo = () => {};
  dom.window.eval(fs.readFileSync('app.js', 'utf8'));
  return dom;
}

function submit(win, form) {
  form.dispatchEvent(new win.Event('submit', { bubbles: true, cancelable: true }));
}

function click(el) {
  el.dispatchEvent(new el.ownerDocument.defaultView.MouseEvent('click', { bubbles: true, cancelable: true }));
}

function fillDecision(dom, suffix) {
  const d = dom.window.document;
  const values = {
    plant: `Public Plant ${suffix}`,
    condition: `Public Condition ${suffix}`,
    intended: `Public Action ${suffix}`,
    objective: `Public Objective ${suffix}`,
    expected: `Public Expected ${suffix}`,
    confidence: '61',
    alternatives: `Public Alternative ${suffix}`,
    rationale: `Public Rationale ${suffix}`,
  };
  for (const [id, value] of Object.entries(values)) {
    const el = d.getElementById(id);
    if (!el) throw new Error(`missing field ${id}`);
    el.value = value;
  }
  submit(dom.window, d.getElementById('decision-form'));
  return values;
}

function commitToResult(dom, suffix) {
  fillDecision(dom, suffix);
  let d = dom.window.document;
  const freeze = d.getElementById('freeze');
  if (!freeze) throw new Error('did not reach COMMIT');
  click(freeze);
  d = dom.window.document;
  const result = d.getElementById('result');
  if (!result) throw new Error('did not reach WAIT_RESULT');
  click(result);
}

const results = [];
function test(name, fn) {
  try {
    fn();
    results.push({ name, pass: true });
  } catch (error) {
    results.push({ name, pass: false, error: String(error && error.message || error) });
  }
}

test('P1_DRAFT_ROUNDTRIP', () => {
  const dom = boot();
  const values = fillDecision(dom, 'roundtrip');
  let d = dom.window.document;
  const edit = d.getElementById('edit');
  if (!edit) throw new Error('did not reach COMMIT');
  click(edit);
  d = dom.window.document;
  for (const [id, value] of Object.entries(values)) {
    const el = d.getElementById(id);
    if (!el) throw new Error(`missing field after edit ${id}`);
    if (String(el.value) !== String(value)) throw new Error(`${id} was not preserved`);
  }
});

test('P2_ACTUAL_TEMPORAL_SUBSTRATE', () => {
  const dom = boot();
  commitToResult(dom, 'chronology');
  let d = dom.window.document;
  d.getElementById('observationDate').value = '1990-01-01';
  submit(dom.window, d.getElementById('result-form'));
  d = dom.window.document;
  const error = d.getElementById('result-error');
  if (!d.getElementById('result-form') || !error || error.hidden) {
    throw new Error('past observationDate was not rejected');
  }
  d.getElementById('observationDate').value = new Date().toISOString().slice(0, 10);
  submit(dom.window, d.getElementById('result-form'));
  d = dom.window.document;
  if (!d.getElementById('close-reveal')) throw new Error('same-day observationDate was not accepted');
});

test('P3_VALIDATOR_DISCRIMINATION', () => {
  const dom = boot();
  let d = dom.window.document;
  const validation = d.querySelector('[data-view="validation"]');
  if (!validation) throw new Error('validation navigation missing');
  click(validation);
  d = dom.window.document;
  const items = [...d.querySelectorAll('.validation-item')];
  if (items.length < 2) throw new Error('public validation controls missing');
  for (const item of items) {
    if (!item.querySelector('.pass')) throw new Error(`control not correctly classified: ${item.textContent.trim().replace(/\s+/g, ' ')}`);
  }
});

test('P4_REACHED_STATE_TOPOLOGY', () => {
  const dom = boot();
  commitToResult(dom, 'topology');
  let d = dom.window.document;
  d.getElementById('observationDate').value = new Date().toISOString().slice(0, 10);
  submit(dom.window, d.getElementById('result-form'));
  d = dom.window.document;
  const close = d.getElementById('close-reveal');
  if (!close) throw new Error('did not reach REVEAL');
  click(close);
  d = dom.window.document;
  if (!d.getElementById('new-decision') || !d.querySelector('.records')) {
    throw new Error('REVEAL close did not reach EXPLORE');
  }
});

for (const result of results) {
  console.log(`${result.pass ? 'PASS' : 'FAIL'} ${result.name}${result.error ? ` — ${result.error}` : ''}`);
}
const failed = results.filter(r => !r.pass).length;
console.log(`PUBLIC_CONTRACT_RESULT ${results.length - failed}/${results.length} passed`);
process.exit(failed === 0 ? 0 : 1);
