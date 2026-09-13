#!/usr/bin/env node
/**
 * Regenera los <lastmod> de public/sitemap.xml con la fecha real del último
 * commit que tocó cada página (o el mtime si el fichero aún no está en git).
 *
 * No cambia el conjunto de URLs ni las prioridades: solo las fechas.
 * Además avisa de descuadres: URLs sin fichero y páginas sin URL.
 *
 *   node scripts/gen-sitemap.mjs          → reescribe public/sitemap.xml
 *   node scripts/gen-sitemap.mjs --check  → solo informa, no escribe
 */
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(import.meta.dirname, '..');
const PUBLIC = path.join(ROOT, 'public');
const SITEMAP = path.join(PUBLIC, 'sitemap.xml');
// Copias del mismo sitemap que también hay que mantener al día (ver más abajo).
const ALIASES = ['sitemap-2026-09.xml'];
const ORIGIN = 'https://positiva.studio';
const CHECK = process.argv.includes('--check');

// Carpetas que nunca contienen páginas
const SKIP_DIRS = new Set(['assets', 'fonts', 'img', 'js', 'video', 'soporte-assets']);

const fileFor = (urlPath) => {
  const rel = urlPath.replace(/^\/|\/$/g, '');
  return path.join(PUBLIC, rel, 'index.html');
};

const gitDate = (file) => {
  try {
    const out = execFileSync('git', ['log', '-1', '--format=%ad', '--date=short', '--', file], {
      cwd: ROOT, encoding: 'utf8',
    }).trim();
    if (out) return out;
  } catch {}
  return new Date(fs.statSync(file).mtime).toISOString().slice(0, 10);
};

// ── 1. Leer sitemap actual y reescribir lastmod ──────────────────────────
let xml = fs.readFileSync(SITEMAP, 'utf8');
const locs = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
const missing = [];
let changed = 0;

xml = xml.replace(
  /<loc>([^<]+)<\/loc>(\s*)<lastmod>([^<]+)<\/lastmod>/g,
  (full, loc, ws, old) => {
    const file = fileFor(loc.replace(ORIGIN, ''));
    if (!fs.existsSync(file)) { missing.push(loc); return full; }
    const next = gitDate(file);
    if (next !== old) changed++;
    return `<loc>${loc}</loc>${ws}<lastmod>${next}</lastmod>`;
  },
);

// ── 2. Detectar páginas publicadas que no están en el sitemap ────────────
const inSitemap = new Set(locs.map((l) => l.replace(ORIGIN, '')));
const orphans = [];
const walk = (dir, base = '') => {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    if (SKIP_DIRS.has(e.name) || e.name.startsWith('.') || e.name.startsWith('_')) continue;
    const url = `${base}/${e.name}/`;
    if (fs.existsSync(path.join(dir, e.name, 'index.html')) && !inSitemap.has(url)) orphans.push(url);
    walk(path.join(dir, e.name), `${base}/${e.name}`);
  }
};
walk(PUBLIC);

// ── 3. Informe ───────────────────────────────────────────────────────────
console.log(`URLs en el sitemap: ${locs.length}`);
console.log(`lastmod actualizados: ${changed}`);
if (missing.length) console.log(`\n⚠️  URLs sin fichero (${missing.length}):\n  ` + missing.join('\n  '));
if (orphans.length) console.log(`\n⚠️  Páginas fuera del sitemap (${orphans.length}):\n  ` + orphans.join('\n  '));

if (CHECK) { console.log('\n--check: no se ha escrito nada.'); process.exit(0); }
fs.writeFileSync(SITEMAP, xml);
// Copia con nombre fechado: se añadió el 13/09/2026 porque Google tenía cacheada
// una versión del 14 de agosto de sitemap.xml y no la refrescaba. Ambas se
// escriben a la vez para que no puedan divergir sin que nadie se entere.
for (const alias of ALIASES) fs.writeFileSync(path.join(PUBLIC, alias), xml);
console.log(`\npublic/sitemap.xml reescrito (y ${ALIASES.join(', ')}).`);
