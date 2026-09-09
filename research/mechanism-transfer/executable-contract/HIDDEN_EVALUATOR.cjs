const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { JSDOM } = require('jsdom');

const dir = path.resolve(process.argv[2]);
if (!dir) throw new Error('candidate directory required');

function boot() {
  let html = fs.readFileSync(path.join(dir, 'index.html'), 'utf8');
  html = html.replace(/<script\s+src=["']app\.js["']\s*><\/script>/i, '');
  const dom = new JSDOM(html, {
    url: 'https://hidden-contract.test/',
    runScripts: 'outside-only',
    pretendToBeVisual: true,
  });
  dom.window.scrollTo = () => {};
  dom.window.eval(fs.readFileSync(path.join(dir, 'app.js'), 'utf8'));
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
    plant: `Hidden Plant ${suffix}`,
    condition: `Hidden Condition ${suffix}`,
    intended: `Hidden Action ${suffix}`,
    objective: `Hidden Objective ${suffix}`,
    expected: `Hidden Expected ${suffix}`,
    confidence: '73',
    alternatives: `Hidden Alternative ${suffix}`,
    rationale: `Hidden Rationale ${suffix}`,
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

function gate(name, fn) {
  try {
    const detail = fn();
    return { name, pass: true, detail: detail || null };
  } catch (error) {
    return { name, pass: false, detail: String(error && error.message || error) };
  }
}

const gates = [];

gates.push(gate('H1_DRAFT_ROUNDTRIP_VARIATION', () => {
  const dom = boot();
  const values = fillDecision(dom, 'unseen-947');
  let d = dom.window.document;
  const edit = d.getElementById('edit');
  if (!edit) throw new Error('did not reach COMMIT');
  click(edit);
  d = dom.window.document;
  for (const [id, value] of Object.entries(values)) {
    const el = d.getElementById(id);
    if (!el) throw new Error(`missing ${id} after roundtrip`);
    if (String(el.value) !== String(value)) throw new Error(`${id} lost on roundtrip`);
  }
}));

gates.push(gate('H2_TEMPORAL_BOUNDARY', () => {
  const dom = boot();
  commitToResult(dom, 'unseen-time-383');
  let d = dom.window.document;
  const form = d.getElementById('result-form');
  const date = d.getElementById('observationDate');
  date.value = '2001-02-03';
  submit(dom.window, form);
  d = dom.window.document;
  const err = d.getElementById('result-error');
  if (!d.getElementById('result-form') || !err || err.hidden) throw new Error('unseen past observationDate accepted');

  const sameDay = new Date().toISOString().slice(0, 10);
  d.getElementById('observationDate').value = sameDay;
  submit(dom.window, d.getElementById('result-form'));
  d = dom.window.document;
  if (!d.getElementById('close-reveal')) throw new Error('same-day boundary rejected');
}));

gates.push(gate('H3_VALIDATOR_DISCRIMINATION_VARIATION', () => {
  const dom = boot();
  let d = dom.window.document;
  const validation = d.querySelector('[data-view="validation"]');
  if (!validation) throw new Error('validation navigation missing');
  click(validation);
  d = dom.window.document;
  const items = [...d.querySelectorAll('.validation-item')];
  if (items.length < 2) throw new Error('validation controls missing');
  const passed = items.filter(item => item.querySelector('.pass')).length;
  if (passed !== items.length) throw new Error(`${passed}/${items.length} controls correctly classified`);
}));

gates.push(gate('H4_STATE_TOPOLOGY', () => {
  const dom = boot();
  commitToResult(dom, 'unseen-topology-611');
  let d = dom.window.document;
  d.getElementById('observationDate').value = new Date().toISOString().slice(0, 10);
  submit(dom.window, d.getElementById('result-form'));
  d = dom.window.document;
  const close = d.getElementById('close-reveal');
  if (!close) throw new Error('did not reach REVEAL');
  click(close);
  d = dom.window.document;
  if (!d.getElementById('new-decision')) throw new Error('EXPLORE new-decision action absent');
  if (!d.querySelector('.records')) throw new Error('EXPLORE records surface absent');
}));

gates.push(gate('H5_CAPTURE_REGRESSION', () => {
  const dom = boot();
  let d = dom.window.document;
  if (d.querySelector('.record') || d.querySelector('.summary-card')) throw new Error('history visible in DECIDE');
  fillDecision(dom, 'unseen-capture-229');
  d = dom.window.document;
  if (d.querySelector('.record') || d.querySelector('.summary-card')) throw new Error('history visible in COMMIT');
  const text = d.getElementById('app').textContent;
  if (/שיפור נראה לעין|החמרה נראית לעין/.test(text)) throw new Error('prior outcome content leaked into COMMIT');
}));

gates.push(gate('H6_SYNTAX', () => {
  const js = fs.readFileSync(path.join(dir, 'app.js'), 'utf8');
  new vm.Script(js);
  return 'JavaScript parses';
}));

const result = {
  candidate: path.basename(dir),
  behavioral_failures: gates.filter(g => !g.pass).length,
  gates,
};
console.log(JSON.stringify(result, null, 2));
process.exit(result.behavioral_failures === 0 ? 0 : 1);
