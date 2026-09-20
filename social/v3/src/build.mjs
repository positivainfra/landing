// Positiva · social v3 · generador de posts 1080×1350
import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

const ROOT = resolve(import.meta.dirname, '..');
const font = (f) => `file://${ROOT}/fonts/${f}`;
const img = (f) => `file://${ROOT}/img/${f}`;

const ICON = (fill, dot='#C98A2B') => `<svg viewBox="-2 -2 56 59" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" fill="${fill}" d="M12 0 H40 A12 12 0 0 1 52 12 V29 A12 12 0 0 1 40 41 H12 A12 12 0 0 1 0 29 V12 A12 12 0 0 1 12 0 Z M10 10 H42 V31 H10 Z"/><path fill="${fill}" d="M0 20 H10 V50 A5 5 0 0 1 5 55 A5 5 0 0 1 0 50 Z"/><circle cx="26" cy="20.5" r="3.8" fill="${dot}"/></svg>`;

const C = { papel: '#F1F0EC', sala: '#0E0E0D', tinta: '#171614', ambar: '#C98A2B', luz: '#EDECE8', graso: '#E0402A' };

const CSS = `
@font-face{font-family:'Instrument Sans';font-weight:400 700;src:url(${font('instrument.woff2')}) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:300 400;src:url(${font('playfair.woff2')}) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:300 400;src:url(${font('playfair-italic.woff2')}) format('woff2')}
@font-face{font-family:'Space Mono';font-weight:700;src:url(${font('spacemono-700.woff2')}) format('woff2')}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:'Instrument Sans',sans-serif;-webkit-font-smoothing:antialiased}
.bg{position:absolute;inset:0}
.h{position:absolute;left:72px;right:72px;top:118px;font-weight:700;text-transform:uppercase;letter-spacing:-.045em;line-height:.86;z-index:2}
.h .big{display:block;font-size:var(--hs,236px)} .h .big .ln{display:block;white-space:nowrap}
.sub{display:block;font-family:'Playfair Display',serif;font-style:italic;font-weight:400;text-transform:none;letter-spacing:-.02em;line-height:1.02;margin-top:26px;font-size:var(--ss,96px)}
.photo{position:absolute;bottom:0;z-index:1}
.photo img{display:block}
.lock{position:absolute;left:72px;bottom:72px;display:flex;align-items:center;gap:20px;z-index:3}
.lock svg{height:54px;width:auto}
.lock b{font-family:'Space Mono',monospace;font-weight:700;font-size:30px;letter-spacing:.22em;text-transform:uppercase}
.lock b i{font-style:normal;color:var(--dot,#C98A2B)}
.url{position:absolute;right:72px;bottom:72px;font-family:'Space Mono',monospace;font-weight:700;font-size:30px;letter-spacing:.06em;z-index:3}
.grain{position:absolute;inset:0;z-index:4;pointer-events:none;opacity:.14;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
`;

// ── Posts ─────────────────────────────────────────────────────────
const posts = [
  { file: 'post-1-lanzamiento', bg: C.ambar, ink: C.tinta, sub: C.papel, icon: C.tinta,
    h: 'Ya está<br>aquí.', s: 'Gratis. Sin tarjeta.',
    photo: { src: 'pepe-cut.png', w: 540, right: 10, bottom: -90 } },
  { file: 'post-2-caducado', bg: C.sala, ink: C.luz, sub: C.ambar, icon: C.luz,
    h: 'El enlace<br>ha<br>caducado.', s: 'Nunca más.',
    photo: { src: 'manolo-cut.png', w: 540, right: 20, bottom: -90 } },
  { file: 'post-3-definicion', bg: C.papel, ink: C.tinta, sub: C.ambar, icon: C.tinta,
    h: 'Positiva', s: '(adj.) Entregar una vez.<br>No reenviar nunca.', ss: 92, bigicon: true,
     },
  { file: 'post-4-foto-video', bg: C.ambar, ink: C.tinta, sub: C.papel, icon: C.tinta,
    h: 'Foto y<br>vídeo.', s: 'Mismo sitio.<br>Mismo enlace.', frames: true },
  { file: 'post-5-tu-web', bg: C.sala, ink: C.luz, sub: C.ambar, icon: C.luz,
    h: 'Tu<br>web.', s: 'Sin hacer una web.', cap: 255,
    browser: true },
  { file: 'post-6-sin-ilimitado', bg: C.papel, ink: C.tinta, sub: C.ambar, icon: C.tinta,
    h: 'Sin<br>ilimitado.', s: 'Porque es mentira.', tarifa: true },
];

function html(p) {
  const photo = p.photo ? `<div class="photo" style="${p.photo.left != null ? `left:${p.photo.left}px` : `right:${p.photo.right}px`};bottom:${p.photo.bottom}px"><img src="${img(p.photo.src)}" style="width:${p.photo.w}px"></div>` : '';
  const frames = p.frames ? `
    <div style="position:absolute;left:72px;top:720px;width:600px;height:360px;background:${C.tinta};z-index:1"></div>
    <div style="position:absolute;left:372px;top:900px;width:636px;height:320px;background:${C.papel};border:6px solid ${C.tinta};z-index:1;display:flex;align-items:center;justify-content:center">
      <div style="width:0;height:0;border-top:70px solid transparent;border-bottom:70px solid transparent;border-left:120px solid ${C.tinta};margin-left:24px"></div>
    </div>` : '';
  const browserG = p.browser ? `
    <div style="position:absolute;left:72px;right:72px;top:730px;height:450px;border:6px solid ${C.luz};z-index:1;background:${C.sala}">
      <div style="height:84px;border-bottom:6px solid ${C.luz};display:flex;align-items:center;padding:0 28px;gap:16px">
        <span style="width:22px;height:22px;border-radius:50%;background:${C.luz}"></span><span style="width:22px;height:22px;border-radius:50%;background:${C.luz}"></span><span style="width:22px;height:22px;border-radius:50%;background:${C.ambar}"></span>
        <span style="margin-left:24px;font-family:'Space Mono',monospace;font-weight:700;font-size:34px;color:${C.luz};letter-spacing:.02em">tunombre.positiva.studio</span>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:18px;padding:28px">
        <div style="height:135px;background:${C.luz};opacity:.9"></div><div style="height:135px;background:${C.luz};opacity:.9"></div><div style="height:135px;background:${C.ambar}"></div>
        <div style="height:135px;background:${C.ambar}"></div><div style="height:135px;background:${C.luz};opacity:.9"></div><div style="height:135px;background:${C.luz};opacity:.9"></div>
      </div>
    </div>` : '';
  const bigicon = p.bigicon ? `<div style="position:absolute;left:72px;bottom:60px;height:560px;z-index:1">${ICON(C.tinta).replace('<svg ','<svg style="height:560px;width:auto" ')}</div>` : '';
  const tarifa = p.tarifa ? `
    <div style="position:absolute;left:72px;right:72px;bottom:230px;z-index:2;font-weight:700;letter-spacing:-.03em;line-height:.95">
      <div style="font-size:150px;color:${C.tinta}">250 GB</div>
      <div style="font-size:150px;color:${C.ambar}">89 €<span style="font-size:72px;letter-spacing:0"> / AÑO</span></div>
    </div>` : '';
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head>
<body style="background:${p.bg};--dot:${p.bg===C.ambar?p.icon:"#C98A2B"};--hs:${p.hs}px;--ss:${p.ss || 96}px">
  <div class="h" style="color:${p.ink}"><span class="big">${p.h.split("<br>").map(l=>`<span class="ln">${l}</span>`).join("")}</span><span class="sub" style="color:${p.sub}">${p.s}</span></div>
  ${photo}${frames}${browserG}${bigicon}${tarifa}
  ${p.bigicon?"":`<div class="lock" style="color:${p.icon}">${ICON(p.icon, p.bg===C.ambar?p.icon:"#C98A2B")}<b>Positiva<i>.</i></b></div>`}
  ${p.photo?"":`<div class="url" style="color:${p.icon}">positiva.studio</div>`}
  <div class="grain"></div>
</body></html>`;
}

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
for (const p of posts) {
  const h = html(p);
  writeFileSync(`${ROOT}/src/${p.file}.html`, h);
  await page.goto(`file://${ROOT}/src/${p.file}.html`, { waitUntil: 'load' });
  await page.evaluate(async (cap) => { await document.fonts.ready;
    const big=document.querySelector('.big'); const lines=[...big.querySelectorAll('.ln')]; const W=940;
    let lo=80, hi=cap; while(hi-lo>1){ const m=(lo+hi)/2; big.style.fontSize=m+'px'; const w=Math.max(...lines.map(l=>l.scrollWidth)); if(w<=W) lo=m; else hi=m; }
    big.style.fontSize=lo+'px'; }, p.cap || 320);
  await page.screenshot({ path: `${ROOT}/out/${p.file}.png`, type: 'png' });
  console.log('ok', p.file);
}
await browser.close();
