# -*- coding: utf-8 -*-
# Generador puntual de los 3 casos de uso (bodas, agencias, freelance).
# Comparte base CSS/JS con las páginas de producto y deja los marcadores pv:nav / pv:footer.
import json

BASE_CSS = """
@font-face{font-family:'Playfair Display';font-style:normal;font-weight:300 400;font-display:swap;src:url(/fonts/playfair.woff2) format('woff2')}
@font-face{font-family:'Playfair Display';font-style:italic;font-weight:300 400;font-display:swap;src:url(/fonts/playfair-italic.woff2) format('woff2')}
@font-face{font-family:'Instrument Sans';font-style:normal;font-weight:400 700;font-display:swap;src:url(/fonts/instrument.woff2) format('woff2')}
@font-face{font-family:'IBM Plex Mono';font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/ibmplexmono-400.woff2) format('woff2')}
@font-face{font-family:'IBM Plex Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/ibmplexmono-700.woff2) format('woff2')}
@font-face{font-family:'Space Mono';font-style:normal;font-weight:700;font-display:swap;src:url(/fonts/spacemono-700.woff2) format('woff2')}
:root{
  --pv-papel:#F1F0EC; --pv-luz:#FFFFFF; --pv-bandeja:#E6E5E0; --pv-sala:#0E0E0D; --pv-sala-2:#1A1A18;
  --pv-tinta:#171614; --pv-tinta-60:#6E6D67; --pv-tinta-30:#A9A8A2; --pv-linea:#D6D5CF; --pv-linea-sala:#2A2A27;
  --pv-ambar:#C98A2B; --pv-ambar-luz:#F5E9D2; --pv-ambar-hover:#B37A24; --pv-ambar-ink:#8F5F15; --pv-graso:#E0402A;
  --pv-display:'Playfair Display',Georgia,serif; --pv-sans:'Instrument Sans',-apple-system,system-ui,sans-serif;
  --pv-mono:'IBM Plex Mono',ui-monospace,monospace;
  --pv-r-panel:10px; --pv-r-input:8px; --pv-r-pill:999px;
  --pv-s2:8px;--pv-s3:12px;--pv-s4:16px;--pv-s5:24px;--pv-s6:32px;--pv-s7:48px;--pv-s8:64px;
  --pv-ease:cubic-bezier(.4,0,.2,1); --pv-ease-out:cubic-bezier(.19,1,.22,1);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--pv-papel);color:var(--pv-tinta);font-family:var(--pv-sans);font-size:18px;line-height:1.67;-webkit-font-smoothing:antialiased;overflow-x:clip}
.wrap{max-width:1180px;margin:0 auto;padding:0 clamp(20px,4vw,56px)}
h1,h2,h3{font-family:var(--pv-display);font-weight:300;letter-spacing:-.02em;line-height:1.08}
h1{line-height:1.04}
h1 em,h2 em{font-style:italic}
h2{font-size:clamp(30px,4vw,54px)}
.lede{font-size:clamp(18px,1.6vw,21px);line-height:1.55;color:var(--pv-tinta-60);max-width:58ch}
.eyebrow{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--pv-ambar-ink);display:flex;align-items:center;gap:var(--pv-s4);margin-bottom:var(--pv-s6)}
.eyebrow::after{content:"";flex:1;height:1px;background:currentColor;opacity:.28}
.dark .eyebrow,.capture .eyebrow{color:var(--pv-ambar)}
.eyebrow .idx{color:var(--pv-tinta-30)}
section{padding:clamp(72px,9vw,120px) 0}
html.js .reveal{opacity:0;transform:translateY(30px);transition:opacity .9s var(--pv-ease-out),transform .9s var(--pv-ease-out);transition-delay:var(--d,0s)}
html.js .reveal.is-in{opacity:1;transform:none}
.btn{display:inline-flex;align-items:center;gap:var(--pv-s2);font-size:15px;font-weight:600;padding:14px 28px;border-radius:var(--pv-r-pill);border:1px solid transparent;cursor:pointer;text-decoration:none;transition:all .22s var(--pv-ease)}
.btn-amber{background:var(--pv-ambar);color:#fff;border-color:var(--pv-ambar);text-transform:uppercase;letter-spacing:.08em;font-weight:700;box-shadow:0 6px 20px -8px rgba(201,138,43,.6)}
.btn-amber:hover{background:var(--pv-ambar-hover);border-color:var(--pv-ambar-hover);transform:translateY(-1px)}
.btn-ghost{color:var(--pv-tinta);border-color:var(--pv-linea)}
.btn-ghost:hover{border-color:var(--pv-tinta)}
.dark{background:var(--pv-sala);color:#EDECE8}
.dark .lede{color:#9C9B95}
.dark .eyebrow .idx{color:#5C5B56}
.dark h2{color:#EDECE8}
/* hero tipográfico compartido */
.heroC{position:relative;min-height:100svh;display:flex;flex-direction:column;overflow:clip}
.heroC.dark .hero-note{color:#5C5B56}
.heroC-inner{
  position:relative;z-index:2;padding-top:clamp(96px,12vh,136px);padding-bottom:clamp(40px,6vh,64px);
  flex:1;width:100%;
  display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr);gap:clamp(32px,5vw,80px);
  align-items:center;
}
.heroC h1{font-size:clamp(42px,5.8vw,82px);letter-spacing:-.025em;margin:clamp(8px,1vw,16px) 0 clamp(24px,3vw,44px)}
.heroC h1 em{color:var(--pv-ambar-ink)}
.heroC.dark h1{color:#EDECE8}
.heroC.dark h1 em{color:var(--pv-ambar)}
.heroC.dark .eyebrow{color:var(--pv-ambar)}
.heroC.dark .btn-ghost{color:#EDECE8;border-color:#3A3936}
.heroC.dark .btn-ghost:hover{border-color:#EDECE8}
.hl{display:block;overflow:hidden;padding-bottom:.12em;margin-bottom:-.12em}
.hl>span{display:inline-block;transform:translateY(128%);animation:pv-linea-sube .9s var(--pv-ease-out) forwards;animation-delay:var(--d,0s)}
@keyframes pv-linea-sube{to{transform:none}}
.heroC .lede{max-width:46ch}
.hero-cta{display:flex;gap:var(--pv-s3);margin-top:var(--pv-s6);flex-wrap:wrap}
.hero-note{margin-top:var(--pv-s6);font-family:var(--pv-mono);font-size:12.5px;line-height:1.8;letter-spacing:.02em;color:var(--pv-tinta-30)}
/* pila de capturas */
.pila{position:relative;justify-self:center;width:min(100%,520px);aspect-ratio:1200/900}
.pila img{position:absolute;width:86%;height:auto;border-radius:var(--pv-r-panel);display:block}
.pila .atras{right:0;top:0;transform:rotate(2.2deg);filter:drop-shadow(0 24px 44px rgba(23,22,20,.28)) saturate(.94);opacity:.92}
.pila .delante{left:0;bottom:6%;transform:rotate(-1.6deg);filter:drop-shadow(0 34px 60px rgba(23,22,20,.4));animation:pila-flota 7s ease-in-out infinite alternate}
@keyframes pila-flota{from{transform:rotate(-1.6deg) translateY(0)}to{transform:rotate(-1.6deg) translateY(-9px)}}
/* checklist (freelance) */
.lista-check{
  justify-self:center;width:min(100%,420px);background:var(--pv-sala);color:#EDECE8;
  border-radius:var(--pv-r-panel);padding:clamp(24px,3vw,36px);
  box-shadow:0 44px 90px -38px rgba(23,22,20,.5);display:grid;gap:14px;
}
.lista-check b{font-family:var(--pv-mono);font-size:10px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#5C5B56}
.lista-check span{display:flex;align-items:baseline;gap:12px;font-family:var(--pv-mono);font-size:13px;letter-spacing:.04em}
.lista-check i{font-style:normal;color:var(--pv-ambar);font-weight:700}
.lista-check .suma{border-top:1px solid var(--pv-linea-sala);padding-top:14px;color:var(--pv-ambar);text-transform:uppercase;font-weight:700;letter-spacing:.12em;font-size:11px}
/* bloques compartidos */
.head2{display:grid;grid-template-columns:1.05fr .95fr;gap:var(--pv-s8);align-items:end}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(20px,3vw,44px);margin-top:clamp(44px,6vw,72px)}
.steps.cuatro{grid-template-columns:repeat(4,1fr)}
.step{border-top:1px solid var(--pv-linea);padding-top:var(--pv-s5)}
.dark .step{border-top-color:var(--pv-linea-sala)}
.step em{font-style:normal;font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--pv-ambar-ink)}
.dark .step em{color:var(--pv-ambar)}
.step h3{font-size:clamp(21px,2vw,25px);font-weight:400;margin:var(--pv-s3) 0}
.step p{color:var(--pv-tinta-60);font-size:16px;line-height:1.62}
.dark .step p{color:#9C9B95}
.step a{color:var(--pv-ambar-ink)}
.dark .step a{color:var(--pv-ambar)}
.galeria-tira{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:clamp(44px,6vw,72px)}
.galeria-tira figure{margin:0;min-width:0}
.galeria-tira img{width:100%;height:auto;display:block;border-radius:var(--pv-r-panel);filter:drop-shadow(0 24px 44px rgba(0,0,0,.5))}
.tira-pie{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#5C5B56;margin-top:var(--pv-s4)}
.tira-pie b{color:var(--pv-ambar)}
.nota-linea{margin-top:clamp(36px,5vw,56px);border-top:1px solid var(--pv-linea);padding-top:var(--pv-s5);display:grid;grid-template-columns:1fr 1fr;gap:var(--pv-s5) var(--pv-s8)}
.dark .nota-linea{border-top-color:var(--pv-linea-sala)}
.nota-linea h3{font-family:var(--pv-mono);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--pv-ambar-ink);margin-bottom:var(--pv-s3)}
.dark .nota-linea h3{color:var(--pv-ambar)}
.nota-linea p{color:var(--pv-tinta-60);font-size:16px;line-height:1.62}
.dark .nota-linea p{color:#9C9B95}
.nota-linea a{color:var(--pv-ambar-ink)}
.dark .nota-linea a{color:var(--pv-ambar)}
details{border-top:1px solid var(--pv-linea)}
details:last-of-type{border-bottom:1px solid var(--pv-linea)}
summary{font-family:var(--pv-display);font-size:clamp(20px,2vw,24px);font-weight:400;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:baseline;gap:var(--pv-s4);padding:var(--pv-s5) 0;transition:color .18s}
summary:hover{color:var(--pv-ambar-hover)}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";color:var(--pv-ambar);font-family:var(--pv-sans);font-weight:400;flex:none;transition:transform .3s var(--pv-ease)}
details[open] summary::after{transform:rotate(45deg)}
details p{padding:0 0 var(--pv-s5);color:var(--pv-tinta-60);max-width:64ch}
details a{color:var(--pv-ambar-ink)}
.faq-list{margin-top:clamp(36px,5vw,56px)}
.related{margin-top:clamp(44px,6vw,72px);display:grid;grid-template-columns:repeat(2,1fr);gap:var(--pv-s2) var(--pv-s7)}
.related a{font-family:var(--pv-mono);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--pv-tinta-60);text-decoration:none;padding:12px 0;border-top:1px solid var(--pv-linea);display:flex;justify-content:space-between;gap:var(--pv-s4);transition:color .18s}
.related a::after{content:"→";color:var(--pv-ambar)}
.related a:hover{color:var(--pv-tinta)}
.capture{background:var(--pv-sala);color:#EDECE8;border-radius:var(--pv-r-panel);padding:clamp(56px,8vw,104px) var(--pv-s7);text-align:center}
.capture h2{color:#EDECE8;margin-bottom:var(--pv-s4)}
.capture .lede{margin:0 auto;color:#9C9B95}
.capture form{display:flex;gap:var(--pv-s2);max-width:480px;margin:var(--pv-s7) auto 0;flex-wrap:wrap}
input[type=email]{flex:1;min-width:220px;font-family:var(--pv-sans);font-size:16px;padding:14px 18px;background:var(--pv-sala-2);border:1px solid var(--pv-linea-sala);border-radius:var(--pv-r-input);color:#EDECE8}
input[type=email]::placeholder{color:#5C5B56}
input[type=email]:focus{outline:2px solid var(--pv-ambar);outline-offset:1px;border-color:transparent}
.capture form .btn{background:var(--pv-ambar);color:#fff;border:0;text-transform:uppercase;letter-spacing:.08em}
.capture form .btn:hover{background:var(--pv-ambar-hover)}
.capture small{display:block;margin-top:var(--pv-s5);font-family:var(--pv-mono);font-size:11px;letter-spacing:.08em;color:#5C5B56;text-transform:uppercase}
@media(max-width:940px){
  .heroC-inner{grid-template-columns:1fr;gap:var(--pv-s7);align-items:start;padding-top:clamp(96px,13vh,120px)}
  .heroC h1{font-size:clamp(42px,11.5vw,68px)}
  .pila,.lista-check{justify-self:start}
  .head2{grid-template-columns:1fr;gap:var(--pv-s5)}
  .steps,.steps.cuatro{grid-template-columns:1fr;gap:var(--pv-s6)}
  .nota-linea{grid-template-columns:1fr}
  .galeria-tira{grid-template-columns:1fr 1fr}
  .galeria-tira figure:nth-child(3){display:none}
  .related{grid-template-columns:1fr}
}
@media(prefers-reduced-motion:reduce){
  html.js .reveal{opacity:1;transform:none;transition:none}
  .hl>span{transform:none;animation:none}
  .pila .delante{animation:none}
}
"""

SCRIPTS = """
document.documentElement.classList.add('js');
(() => {
  if (!('IntersectionObserver' in window)) { document.querySelectorAll('.reveal').forEach(el => el.classList.add('is-in')); return; }
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } }), { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();
/* Lista de espera → /api/waitlist (mismo Worker que el resto). */
document.getElementById('wl').addEventListener('submit', async (e) => {
  e.preventDefault();
  const form = e.target;
  const email = form.email.value.trim();
  const msg = document.getElementById('msg');
  if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {
    msg.textContent = 'Ese email no parece válido. Revísalo.';
    msg.style.color = 'var(--pv-graso)';
    track(Events.WAITLIST_INVALID_EMAIL, { source: 'SOURCE' });
    return;
  }
  const btn = form.querySelector('button');
  btn.disabled = true;
  try {
    const r = await fetch('/api/waitlist', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, source: 'SOURCE' }),
    });
    if (!r.ok && r.status !== 409) throw new Error(String(r.status));
    msg.textContent = 'Apuntado. Te escribo el día que abra.';
    msg.style.color = 'var(--pv-ambar)';
    track(Events.WAITLIST_SUBMITTED, { source: 'SOURCE' });
    form.reset();
  } catch (_) {
    msg.textContent = 'No se ha podido guardar. Inténtalo de nuevo en un momento.';
    msg.style.color = 'var(--pv-graso)';
  } finally {
    btn.disabled = false;
  }
});
"""

def faq_jsonld(faqs):
    return json.dumps({
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a, _ in faqs
        ]
    }, ensure_ascii=False, indent=2)

def faq_html(faqs):
    out = []
    for q, a, extra in faqs:
        link = f'\n        {extra}' if extra else ''
        out.append(f'''      <details class="reveal">
        <summary>{q}</summary>
        <p>{a}{link}</p>
      </details>''')
    return '\n'.join(out)

def page(cfg):
    schema = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://positiva.studio/"},
                {"@type": "ListItem", "position": 2, "name": cfg['nombre'], "item": f"https://positiva.studio/{cfg['slug']}/"},
            ]},
            json.loads(faq_jsonld(cfg['faqs'])),
        ]
    }, ensure_ascii=False, indent=2)
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{cfg['title']}</title>
<meta name="description" content="{cfg['desc']}">
<meta property="og:title" content="{cfg['title']}">
<meta property="og:description" content="{cfg['ogdesc']}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://positiva.studio/{cfg['slug']}/">
<meta property="og:image" content="https://positiva.studio/assets/og.png">
<meta property="og:locale" content="es_ES">
<meta name="theme-color" content="{cfg.get('theme', '#F1F0EC')}">
<link rel="canonical" href="https://positiva.studio/{cfg['slug']}/">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/fonts/playfair.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/instrument.woff2" as="font" type="font/woff2" crossorigin>

<style>{BASE_CSS}{cfg.get('css','')}</style>

<!-- Analítica · Umami autoalojado (tracker servido en /stats). -->
<script defer src="https://analytics.labbo.studio/stats" data-website-id="ddf13c3b-1f69-4fac-bd38-4629c55611bd"></script>
<script defer src="https://analytics.labbo.studio/recorder.js" data-website-id="ddf13c3b-1f69-4fac-bd38-4629c55611bd"></script>
<script src="/js/analytics.js"></script>
<script type="application/ld+json">
{schema}
</script>
</head>
<body{cfg.get('bodyclass','')}>

<!-- pv:nav --><!-- /pv:nav -->

{cfg['hero']}

{cfg['secciones']}

<!-- ══ FAQ ══ -->
<section id="faq" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow reveal">Preguntas frecuentes</p>
    <div class="faq-list">
{faq_html(cfg['faqs'])}
    </div>

    <div class="related">
{cfg['related']}
    </div>
  </div>
</section>

<!-- ══ LISTA DE ESPERA ══ -->
<section id="lista" style="padding-top:0">
  <div class="wrap">
    <div class="capture reveal">
      <p class="eyebrow" style="justify-content:center">Lista de espera</p>
      <h2>{cfg['captura_h2']}</h2>
      <p class="lede">
        Estamos en fase Beta, puliendo los últimos detalles. Déjame tu email y te aviso el día
        que puedas entrar — con la tarifa fundador, no con otra.
      </p>
      <form id="wl" novalidate>
        <input type="email" name="email" placeholder="nombre@tuestudio.com" required aria-label="Tu email">
        <button type="submit" class="btn">Avísame</button>
      </form>
      <small id="msg">Sin newsletter. Un email, el día que abra.</small>
    </div>
  </div>
</section>

<!-- pv:footer --><!-- /pv:footer -->

<script>{SCRIPTS.replace("SOURCE", cfg['source'])}</script>
</body>
</html>
'''

import pathlib
CFGS = []  # se rellena en casos-data.py
exec(open('scripts/casos-data.py', encoding='utf-8').read())
for cfg in CFGS:
    p = pathlib.Path(f"public/{cfg['slug']}/index.html")
    p.parent.mkdir(exist_ok=True)
    p.write_text(page(cfg), encoding='utf-8')
    print('✓', p)
