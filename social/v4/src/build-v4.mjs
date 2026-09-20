// Positiva · social v4 · editorial (mymind) + práctico (pixieset) + comunidad (pic-time)
import { chromium } from 'playwright';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve } from 'node:path';

const ROOT = resolve(import.meta.dirname, '..');
const font = (f) => `file://${ROOT}/fonts/${f}`;
const img = (f) => `file://${ROOT}/img/${f}`;
mkdirSync(`${ROOT}/out4`, { recursive: true });

const C = { papel: '#F1F0EC', sala: '#0E0E0D', tinta: '#171614', tinta60: '#6E6D67', ambar: '#C98A2B', luz: '#EDECE8', luz60: '#9C9B95', graso: '#E0402A' };

const ICON = (fill, dot = C.ambar) => `<svg viewBox="-2 -2 56 59" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" fill="${fill}" d="M12 0 H40 A12 12 0 0 1 52 12 V29 A12 12 0 0 1 40 41 H12 A12 12 0 0 1 0 29 V12 A12 12 0 0 1 12 0 Z M10 10 H42 V31 H10 Z"/><path fill="${fill}" d="M0 20 H10 V50 A5 5 0 0 1 5 55 A5 5 0 0 1 0 50 Z"/><circle cx="26" cy="20.5" r="3.8" fill="${dot}"/></svg>`;
const LOCK = (ink, dot = C.ambar, pos = 'left:80px;bottom:80px') => `<div class="lock" style="${pos};color:${ink}">${ICON(ink, dot)}<b>Positiva<i style="color:${dot}">.</i></b></div>`;

const CSS = `
@font-face{font-family:'Instrument Sans';font-weight:400 700;src:url(${font('instrument.woff2')}) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:300 400;src:url(${font('playfair.woff2')}) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:300 400;src:url(${font('playfair-italic.woff2')}) format('woff2')}
@font-face{font-family:'Space Mono';font-weight:700;src:url(${font('spacemono-700.woff2')}) format('woff2')}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{position:relative;font-family:'Instrument Sans',sans-serif;-webkit-font-smoothing:antialiased}
.pf{font-family:'Playfair Display',serif;font-weight:300;letter-spacing:-.02em;line-height:1.02}
.pf em{font-style:italic;font-weight:400}
.sans{font-family:'Instrument Sans',sans-serif;font-weight:400;line-height:1.3}
.lock{position:absolute;display:flex;align-items:center;gap:18px;z-index:5}
.lock svg{height:52px;width:auto}
.lock b{font-family:'Space Mono',monospace;font-weight:700;font-size:30px;letter-spacing:.22em;text-transform:uppercase}
.lock b i{font-style:normal}
.abs{position:absolute}
`;

const posts = [
  // 1 · Lanzamiento — foto real protagonista
  { file: 'post-1-lanzamiento', body: `
    <img src="${img('boda.jpg')}" class="abs" style="left:-1320px;top:0;height:1350px;width:auto">
    <div class="abs" style="inset:0;background:linear-gradient(to top, rgba(14,14,13,1) 0%, rgba(14,14,13,1) 9%, rgba(14,14,13,.55) 40%, rgba(14,14,13,0) 70%)"></div>
    <div class="abs" style="inset:0;background:linear-gradient(to bottom, rgba(14,14,13,.45) 0%, rgba(14,14,13,0) 30%)"></div>
    ${LOCK(C.luz, C.ambar, 'left:80px;top:80px')}
    <div class="abs pf" style="left:80px;right:80px;bottom:250px;font-size:176px;color:${C.luz}">Ya está<br><em style="color:${C.ambar}">aquí.</em></div>
    <div class="abs sans" style="left:80px;right:80px;bottom:96px;font-size:44px;color:${C.luz};line-height:1.25">Galerías de fotos y vídeo<br>con tu marca. Gratis, sin tarjeta.</div>
  ` },

  // 2 · Cita de oficio (mymind) — ámbar + foto real impresa
  { file: 'post-2-cita-oficio', body: `
    <div class="abs" style="inset:0;background:${C.ambar}"></div>
    <div class="abs pf" style="left:80px;right:80px;top:96px;font-size:92px;color:${C.tinta};font-weight:400;line-height:1.06">«Tus primeras diez mil fotografías serán las peores.»</div>
    <div class="abs pf" style="left:80px;top:520px;font-size:44px;color:${C.tinta};font-style:italic;font-weight:400">Henri Cartier-Bresson</div>
    <div class="abs" style="left:80px;right:80px;top:600px;height:560px;background:${C.papel};padding:22px;box-shadow:0 24px 60px rgba(0,0,0,.18)">
      <div style="width:100%;height:100%;background:url(${img('venice.jpg')}) center/cover"></div>
    </div>
    ${LOCK(C.tinta, C.tinta, 'right:80px;bottom:70px')}
  ` },

  // 3 · Definición — papel, tipográfico
  { file: 'post-3-definicion', body: `
    <div class="abs" style="inset:0;background:${C.papel}"></div>
    <div class="abs pf" style="left:80px;right:80px;top:200px;font-size:150px;color:${C.tinta};font-weight:400">Positiva <em style="color:${C.ambar};font-size:96px;font-weight:300">(adj.)</em></div>
    <div class="abs pf" style="left:80px;right:80px;top:470px;font-size:74px;color:${C.tinta};line-height:1.16">Dicho de una entrega: hacerla <em>una vez</em>, con tu marca, y no reenviarla <em>nunca</em>.</div>
    <div class="abs sans" style="left:80px;right:80px;bottom:200px;font-size:40px;color:${C.tinta60}">Así entendemos el trabajo terminado.</div>
    ${LOCK(C.tinta)}
  ` },

  // 4 · Práctico (pixieset) — sala, el problema concreto
  { file: 'post-4-enlace-caducado', body: `
    <div class="abs" style="inset:0;background:${C.sala}"></div>
    ${LOCK(C.luz, C.ambar, 'left:80px;top:80px')}
    <div class="abs pf" style="left:80px;right:80px;top:260px;font-size:132px;color:${C.luz}">¿Todavía usas enlaces que <em style="color:${C.graso}">caducan?</em></div>
    <div class="abs" style="left:80px;top:760px;width:700px;background:${C.graso};border-radius:22px;padding:34px 44px;transform:rotate(-2.5deg);box-shadow:0 30px 60px rgba(0,0,0,.45);display:flex;align-items:center;gap:26px">
      <div style="width:52px;height:52px;border-radius:50%;border:5px solid ${C.luz};display:flex;align-items:center;justify-content:center;color:${C.luz};font-weight:700;font-size:32px">!</div>
      <div class="sans" style="font-size:40px;font-weight:700;color:${C.luz};letter-spacing:.02em">El enlace ha caducado</div>
    </div>
    <div class="abs pf" style="left:80px;right:80px;bottom:96px;font-size:60px;color:${C.ambar};font-style:italic;font-weight:400;line-height:1.12">En Positiva el enlace es siempre el mismo.</div>
  ` },

  // 5 · Comunidad (pic-time) — galería real, papel
  { file: 'post-5-entregado-con', body: `
    <div class="abs" style="inset:0;background:${C.papel}"></div>
    <div class="abs pf" style="left:80px;right:80px;top:96px;font-size:110px;color:${C.tinta}">Entregado<br>con <em style="color:${C.ambar}">Positiva.</em></div>
    <div class="abs" style="left:80px;right:80px;top:430px;height:640px;border-radius:14px;overflow:hidden;box-shadow:0 30px 70px rgba(23,22,20,.22);background:#fff">
      <img src="${img('galeria-aitana.jpg')}" style="width:100%;height:auto;display:block">
    </div>
    <div class="abs sans" style="left:80px;right:80px;bottom:190px;font-size:40px;color:${C.tinta60}">Quiero Wedding Studio · Aitana y David · Valencia</div>
    ${LOCK(C.tinta)}
  ` },

  // 6 · Postura — sala, tipográfico
  { file: 'post-6-sin-ilimitado', body: `
    <div class="abs" style="inset:0;background:${C.sala}"></div>
    ${LOCK(C.luz, C.ambar, 'left:80px;top:80px')}
    <div class="abs pf" style="left:80px;right:80px;top:330px;font-size:160px;color:${C.luz}">Sin<br>ilimitado.</div>
    <div class="abs pf" style="left:80px;right:80px;top:700px;font-size:120px;color:${C.ambar};font-style:italic;font-weight:400">Porque es mentira.</div>
    <div class="abs sans" style="left:80px;right:80px;bottom:96px;font-size:42px;color:${C.luz60};line-height:1.3">Autor · 250 GB · foto y vídeo con tu marca<br><span style="color:${C.luz}">89 € al año.</span> Y te decimos cuánto cuesta cada giga.</div>
  ` },
];

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
for (const p of posts) {
  const h = `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${p.body}</body></html>`;
  writeFileSync(`${ROOT}/src/v4-${p.file}.html`, h);
  await page.goto(`file://${ROOT}/src/v4-${p.file}.html`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `${ROOT}/out4/${p.file}.png` });
  console.log('ok', p.file);
}
await browser.close();
