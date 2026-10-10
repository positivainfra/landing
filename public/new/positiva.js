/* ══════════════════════════════════════════════════════════════════════
   POSITIVA · web nueva · script común de todas las páginas
   Fuente: scripts/new-web/positiva.js → public/new/positiva.js (gen.py)
   Sin librerías. Respeta prefers-reduced-motion.
   Los vídeos que controla este script llevan data-noauto para que el
   autoplay genérico del pie común no los arranque por su cuenta.
   ══════════════════════════════════════════════════════════════════════ */
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var track=function(n,d){try{if(window.track)window.track(n,d)}catch(_){}};
  var hasIO='IntersectionObserver' in window;

  /* nav: línea al hacer scroll, enlace actual y menú móvil */
  var nav=document.getElementById('nav');
  if(nav){addEventListener('scroll',function(){nav.classList.toggle('scrolled',scrollY>8)},{passive:true})}
  var here=location.pathname.replace(/index\.html$/,'');
  document.querySelectorAll('.links a, .menu-m a').forEach(function(a){
    var h=a.getAttribute('href');
    if(h&&h!=='/new/'&&h.charAt(0)==='/'&&here.indexOf(h)===0)a.setAttribute('aria-current','page');
  });
  /* Mientras la web nueva vive en /new/: los enlaces que se pintan en el navegador
     (resultados del buscador de soporte, etc.) no pasan por gen.py; si apuntan a
     blog, soporte o novedades de la raíz, se llevan a su copia en /new/. Al pasar
     a la raíz, la ruta ya no empieza por /new/ y esto no hace nada. */
  if(location.pathname.indexOf('/new/')===0){
    document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href^="/"]');if(!a)return;
      var h=a.getAttribute('href');
      if(/^\/(soporte|notas|novedades)(\/|$)/.test(h)&&!/\.[a-z0-9]{2,5}(#|\?|$)/i.test(h)){a.setAttribute('href','/new'+(h==='/soporte'||h==='/soporte/'?'/soporte/es/':h))}
    },true);
  }

  /* desplegable «Casos de uso»: ratón (hover con margen), teclado y toque */
  document.querySelectorAll('nav.top .dd').forEach(function(dd){
    var b=dd.querySelector('.dd-b'),t;
    var abre=function(v){clearTimeout(t);dd.classList.toggle('abierto',v);b.setAttribute('aria-expanded',v)};
    if(dd.querySelector('a[aria-current]'))b.classList.add('actual');
    b.addEventListener('click',function(){abre(!dd.classList.contains('abierto'))});
    dd.addEventListener('mouseenter',function(e){if(matchMedia('(hover:hover)').matches)abre(true)});
    dd.addEventListener('mouseleave',function(){t=setTimeout(function(){abre(false)},180)});
    dd.addEventListener('focusout',function(e){if(!dd.contains(e.relatedTarget))abre(false)});
    document.addEventListener('click',function(e){if(!dd.contains(e.target))abre(false)});
    dd.addEventListener('keydown',function(e){if(e.key==='Escape'){abre(false);b.focus()}});
  });

  /* CTA flotante de registro: todas las páginas menos /soporte/ */
  (function(){
    if(/\/soporte\//.test(location.pathname))return;
    try{if(sessionStorage.getItem('pv-cta-flot')==='no')return}catch(_){}
    var el=document.createElement('div');el.className='cta-flot';el.setAttribute('role','complementary');el.setAttribute('aria-label','Prueba Positiva');
    el.innerHTML='<a href="https://app.positiva.studio/registro" data-ev="register_click" data-ev-place="flotante"><span class="ico"><svg viewBox="-2 -2 56 59" aria-hidden="true"><path fill-rule="evenodd" fill="currentColor" d="M12 0 H40 A12 12 0 0 1 52 12 V29 A12 12 0 0 1 40 41 H12 A12 12 0 0 1 0 29 V12 A12 12 0 0 1 12 0 Z M10 10 H42 V31 H10 Z"/><path fill="currentColor" d="M0 20 H10 V50 A5 5 0 0 1 5 55 A5 5 0 0 1 0 50 Z"/></svg></span><span>Prueba <b>Positiva</b> gratis</span></a>'
      +'<button class="x" type="button" aria-label="Cerrar"><svg viewBox="0 0 10 10" aria-hidden="true"><path d="M1 1l8 8M9 1l-8 8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>';
    document.body.appendChild(el);
    var UMBRAL=1000,otros=0,cerrado=false,ancho=matchMedia('(min-width:1001px)');
    var pinta=function(){var v=!cerrado&&scrollY>UMBRAL&&otros===0;
      if(v!==el.classList.contains('ver')){el.classList.toggle('ver',v);if(v&&ancho.matches)track('cta_flotante_visto')}};
    /* otros botones de registro a la vista (salvo los del nav): el flotante se aparta */
    if(hasIO){var vis=new Set();var io=new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?vis.add(e.target):vis.delete(e.target)});otros=vis.size;pinta()});
      document.querySelectorAll('a[href^="https://app.positiva.studio/registro"], form#wl').forEach(function(a){if(!a.closest('nav.top, .menu-m, .cta-flot'))io.observe(a)})}
    addEventListener('scroll',pinta,{passive:true});pinta();
    el.querySelector('.x').addEventListener('click',function(){cerrado=true;pinta();track('cta_flotante_cerrado');try{sessionStorage.setItem('pv-cta-flot','no')}catch(_){}});
  })();

  var burger=document.querySelector('.burger'),menu=document.getElementById('menu-m');
  if(burger&&menu){
    var set=function(open){burger.setAttribute('aria-expanded',open);burger.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');menu.hidden=!open;document.body.classList.toggle('menu-abierto',open)};
    burger.addEventListener('click',function(){set(burger.getAttribute('aria-expanded')!=='true')});
    menu.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
    addEventListener('keydown',function(e){if(e.key==='Escape'&&!menu.hidden){set(false);burger.focus()}});
    addEventListener('resize',function(){if(innerWidth>1000&&!menu.hidden)set(false)});
  }

  /* vídeos que arrancan en un segundo concreto (el inicio de algunos clips está vacío) */
  document.querySelectorAll('video[data-start]').forEach(function(v){var t=+v.dataset.start;
    v.addEventListener('loadedmetadata',function(){if(v.currentTime<t)v.currentTime=t});
    v.addEventListener('timeupdate',function(){if(v.currentTime<t-0.05)v.currentTime=t});
  });

  /* escenario con capítulos (home) */
  var tabs=document.querySelectorAll('.chap button'),panes=document.querySelectorAll('#panes .pane'),url=document.getElementById('url');
  if(tabs.length){
    var cur=0,timer,visible=true;
    var show=function(i){cur=i;clearTimeout(timer);
      tabs.forEach(function(t){var on=t.dataset.p==i;t.setAttribute('aria-selected',on);var bar=t.querySelector('i');bar.style.transition='none';bar.style.width='0';if(on){t.style.setProperty('--dur',t.dataset.dur+'ms');requestAnimationFrame(function(){requestAnimationFrame(function(){bar.style.transition='';bar.style.width='100%'})})}});
      panes.forEach(function(p){var on=p.dataset.p==i;p.classList.toggle('on',on);var v=p.querySelector('video');if(v){if(on&&visible){v.currentTime=+(v.dataset.start||0);v.play().catch(function(){})}else{v.pause()}}});
      if(url)url.textContent=tabs[i].dataset.url;
      if(!rm&&visible){timer=setTimeout(function(){show((cur+1)%tabs.length)},+tabs[i].dataset.dur)}
    };
    tabs.forEach(function(t){t.addEventListener('click',function(){show(+t.dataset.p);track('hero_chapter',{p:t.dataset.p})})});
    show(0);
    var stage=document.getElementById('stage');
    if(stage&&hasIO){new IntersectionObserver(function(es){es.forEach(function(e){visible=e.isIntersecting;if(visible){show(cur)}else{clearTimeout(timer);panes.forEach(function(p){var v=p.querySelector('video');if(v)v.pause()})}})},{threshold:.2}).observe(stage)}
  }

  /* el escenario o el medio del hero crecen con el scroll */
  var grow=document.querySelector('[data-grow]');
  if(!rm&&grow){addEventListener('scroll',function(){var r=grow.getBoundingClientRect();var p=Math.min(1,Math.max(0,1-(r.top)/(innerHeight*.9)));grow.style.transform='scale('+(0.94+0.06*p)+')'},{passive:true})}

  /* tira de trabajo real: duplicar para el bucle */
  var tr=document.getElementById('track');if(tr){tr.innerHTML+=tr.innerHTML}

  /* reveals */
  var io=hasIO?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -10% 0px'}):null;
  var pend=[].slice.call(document.querySelectorAll('.r,.reveal-img'));
  pend.forEach(function(el){if(!io||el.getBoundingClientRect().top<innerHeight){el.classList.add('in');return}io.observe(el)});
  /* red de seguridad: con scroll muy rápido el observador puede saltarse alguno */
  var tick=false;addEventListener('scroll',function(){if(tick)return;tick=true;requestAnimationFrame(function(){tick=false;
    pend=pend.filter(function(el){if(el.classList.contains('in'))return false;if(el.getBoundingClientRect().top<innerHeight*.95){el.classList.add('in');return false}return true})})},{passive:true});

  /* vídeos en bucle: solo mientras están en pantalla */
  var vio=hasIO?new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting&&!rm){v.play().catch(function(){})}else{v.pause()}})},{threshold:.35}):null;
  document.querySelectorAll('video.auto').forEach(function(v){if(vio)vio.observe(v)});

  /* tarjetas: vídeo al pasar el ratón; en táctil, al entrar en pantalla */
  var touch=matchMedia('(hover: none)').matches;
  document.querySelectorAll('.q').forEach(function(q){var v=q.querySelector('video.hover');if(!v||rm)return;
    if(touch){if(hasIO){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){q.classList.add('playing');v.play().catch(function(){})}else{q.classList.remove('playing');v.pause()}})},{threshold:.6}).observe(q)}}
    else{q.addEventListener('mouseenter',function(){v.play().catch(function(){})});q.addEventListener('mouseleave',function(){v.pause()})}});

  /* demo: mismo endpoint que la web actual (/api/waitlist → hola@positiva.studio) */
  var wl=document.querySelector('#wl[data-demo]');
  if(wl){wl.addEventListener('submit',async function(e){e.preventDefault();var form=e.target,email=form.email.value.trim(),msg=document.getElementById('msg');
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){msg.textContent='Ese email no parece válido. Revísalo.';msg.style.color='var(--graso)';return}
    var btn=form.querySelector('button');btn.disabled=true;
    try{var r=await fetch('/api/waitlist',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:email,source:'landing-new:'+location.pathname})});
      if(!r.ok&&r.status!==409)throw new Error(String(r.status));
      msg.textContent='Recibido. Te escribo para agendarla.';msg.style.color='var(--ambar-ink)';track('waitlist_submitted',{source:'landing-new'});form.reset()}
    catch(_){msg.textContent='No se ha podido guardar. Inténtalo de nuevo en un momento.';msg.style.color='var(--graso)'}
    finally{btn.disabled=false}})}
})();
