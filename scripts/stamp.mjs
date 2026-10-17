#!/usr/bin/env node
/**
 * stamp.mjs — propaga los parciales comunes (nav y footer) a todas las páginas.
 *
 * Fuente única:
 *   partials/chrome-nav.html    → bloque <!-- pv:nav --> … <!-- /pv:nav -->
 *   partials/chrome-footer.html → bloque <!-- pv:footer --> … <!-- /pv:footer -->
 *
 * Uso:  npm run stamp
 *
 * Reglas:
 *   · Cada página de PAGES debe contener ambos marcadores (error si faltan).
 *   · Lo que haya entre marcadores se sobrescribe SIEMPRE: no edites ahí.
 *   · Para añadir una página nueva: pon los marcadores en su HTML y súmala a PAGES.
 *   · /soporte/ también se estampa (nav y pie); su CONTENIDO sigue siendo del flujo de soporte.
 */
import { readFileSync, writeFileSync, globSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');

// Las páginas comerciales (home, producto, casos, comparativas) las escribe
// scripts/new-web/gen.py con el nav ya puesto: NO van aquí.
const PAGES = [
  'public/novedades/index.html',
  'public/aviso-legal/index.html',
  'public/privacidad/index.html',
  'public/terminos/index.html',
  'public/legal/extension/index.html',
];

// /notas/ (el blog) se estampa igual: índice y artículos.
for (const f of globSync('public/notas/**/index.html', { cwd: ROOT })) PAGES.push(f);

// /soporte/ se estampa también (decisión de Rodrigo, 02/09/2026): sus páginas
// llevan los mismos marcadores. El glob las recoge aunque el otro flujo añada artículos.
for (const f of globSync('public/soporte/es/**/index.html', { cwd: ROOT })) PAGES.push(f);

const nav = readFileSync(resolve(ROOT, 'partials/chrome-nav.html'), 'utf8').trim();
const footer = readFileSync(resolve(ROOT, 'partials/chrome-footer.html'), 'utf8').trim();

const stamp = (html, tag, content, file) => {
  const re = new RegExp(`<!-- pv:${tag} -->[\\s\\S]*?<!-- /pv:${tag} -->`);
  if (!re.test(html)) throw new Error(`${file}: falta el marcador pv:${tag}`);
  return html.replace(re, `<!-- pv:${tag} -->\n${content}\n<!-- /pv:${tag} -->`);
};

let changed = 0;
for (const page of PAGES) {
  const path = resolve(ROOT, page);
  const before = readFileSync(path, 'utf8');
  let after = stamp(before, 'nav', nav, page);
  after = stamp(after, 'footer', footer, page);
  // Capa visual de la web: docs.css encima de su CSS propio y positiva.js (nav, menú, CTA).
  // Idempotente: solo se añade si falta. El «saltar» viejo sobra: el nav trae el suyo.
  after = after.replace(/\s*<a class="saltar" href="#contenido">[^<]*<\/a>/, '');
  if (!after.includes('href="/docs.css"')) after = after.replace('</head>', '<link rel="stylesheet" href="/docs.css">\n</head>');
  if (!after.includes('src="/positiva.js"')) after = after.replace('</body>', '<script src="/positiva.js" defer></script>\n</body>');
  if (after !== before) { writeFileSync(path, after); changed++; console.log(`✓ ${page}`); }
  else console.log(`· ${page} (sin cambios)`);
}
console.log(`\n${changed} página(s) actualizada(s) de ${PAGES.length}.`);
