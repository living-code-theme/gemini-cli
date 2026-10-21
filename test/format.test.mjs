import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { resolveAll } from '../scripts/palette.mjs';
import { keys, hexColors, assertContrast } from './helpers.mjs';
const fixture = JSON.parse(await readFile(new URL('./fixtures/upstream.json', import.meta.url)));
const read = path => readFile(new URL('../' + path, import.meta.url), 'utf8');

for (const f of resolveAll()) test(f.name + ': standalone Gemini custom theme groups', async () => {
  const t = JSON.parse(await read('themes/' + f.slug + '.json'));
  keys(t, ['name', 'type', ...Object.keys(fixture.groups)]);
  assert.equal(t.name, f.name); assert.equal(t.type, 'custom');
  for (const [key, children] of Object.entries(fixture.groups)) keys(t[key], children);
  keys(t.background.diff, ['added', 'removed']);
  hexColors(Object.fromEntries(Object.entries(t).filter(([key]) => !['name', 'type'].includes(key))));
  assert.equal(t.text.primary, f.r('fg')); assert.equal(t.text.link, f.r('link'));
  assert.equal(t.status.error, f.r('error')); assert.equal(t.status.success, f.r('success'));
  assert.equal(t.ui.comment, f.r('comment'));
  assert.equal(t.ui.gradient.length, 3);
  for (const bg of [t.background.primary, t.background.diff.added, t.background.diff.removed]) assertContrast(t.text.primary, bg);
});
