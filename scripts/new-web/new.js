/* ── Nueva home (v1 en /new/) · sin librerías · solo transform/opacity ── */
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var track=window.track||function(){};
  /* nav: línea al hacer scroll */
  var nav=document.getElementById('nav');
  if(nav){addEventListener('scroll',function(){nav.classList.toggle('scrolled',scrollY>8)},{passive:true})}
  /* vídeos con arranque en un segundo concreto (el primer segundo de algunos clips está vacío) */
  document.querySelectorAll('video[data-start]').forEach(function(v){var t=+v.dataset.start;
    v.addEventListener('loadedmetadata',function(){if(v.currentTime<t)v.currentTime=t});
    v.addEventListener('timeupdate',function(){if(v.currentTime<t-0.05)v.currentTime=t});
  });
  /* capítulos del escenario del hero */
  var tabs=document.querySelectorAll('.chap button'),panes=document.querySelectorAll('#panes .pane'),url=document.getElementById('url');
  if(tabs.length){
    var cur=0,timer;
    function show(i){cur=i;clearTimeout(timer);
      tabs.forEach(function(t){var on=t.dataset.p==i;t.setAttribute('aria-selected',on);var bar=t.querySelector('i');bar.style.transition='none';bar.style.width='0';if(on){t.style.setProperty('--dur',t.dataset.dur+'ms');requestAnimationFrame(function(){requestAnimationFrame(function(){bar.style.transition='';bar.style.width='100%'})})}});
      panes.forEach(function(p){var on=p.dataset.p==i;p.classList.toggle('on',on);var v=p.querySelector('video');if(v){if(on){v.currentTime=+(v.dataset.start||0);v.play().catch(function(){})}else{v.pause()}}});
      if(url)url.textContent=tabs[i].dataset.url;
      if(!rm){timer=setTimeout(function(){show((cur+1)%tabs.length)},+tabs[i].dataset.dur)}
    }
    tabs.forEach(function(t){t.addEventListener('click',function(){show(+t.dataset.p);track('hero_chapter',{p:t.dataset.p})})});
    show(0);
    /* si el escenario sale de pantalla, pausar la rotación */
    var stage=document.getElementById('stage');
    if(stage&&'IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){show(cur)}else{clearTimeout(timer);panes.forEach(function(p){var v=p.querySelector('video');if(v)v.pause()})}})},{threshold:.2}).observe(stage)}
    /* el escenario crece con el scroll */
    if(!rm&&stage){addEventListener('scroll',function(){var r=stage.getBoundingClientRect();var p=Math.min(1,Math.max(0,1-(r.top)/(innerHeight*.9)));stage.style.transform='scale('+(0.94+0.06*p)+')'},{passive:true})}
  }
  /* tira de trabajo real: duplicar para el bucle */
  var tr=document.getElementById('track');if(tr){tr.innerHTML+=tr.innerHTML}
  /* reveals */
  var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -10% 0px'}):null;
  document.querySelectorAll('.r,.reveal-img').forEach(function(el){if(el.getBoundingClientRect().top<innerHeight){el.classList.add('in');return}io?io.observe(el):el.classList.add('in')});
  /* vídeos de los pasos: solo en pantalla */
  var vio=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(e.isIntersecting){v.play().catch(function(){})}else{v.pause()}})},{threshold:.35}):null;
  document.querySelectorAll('video.auto').forEach(function(v){vio?vio.observe(v):v.play().catch(function(){})});
  /* tarjetas: vídeo al pasar el ratón; en táctil, al entrar en pantalla */
  var touch=matchMedia('(hover: none)').matches;
  document.querySelectorAll('.q').forEach(function(q){var v=q.querySelector('video.hover');if(!v)return;
    if(touch){if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){q.classList.add('playing');v.play().catch(function(){})}else{q.classList.remove('playing');v.pause()}})},{threshold:.6}).observe(q)}}
    else{q.addEventListener('mouseenter',function(){v.play().catch(function(){})});q.addEventListener('mouseleave',function(){v.pause()})}});
  /* demo: mismo endpoint que la home actual (/api/waitlist → hola@positiva.studio) */
  var wl=document.getElementById('wl');
  if(wl){wl.addEventListener('submit',async function(e){e.preventDefault();var form=e.target,email=form.email.value.trim(),msg=document.getElementById('msg');
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){msg.textContent='Ese email no parece válido. Revísalo.';msg.style.color='var(--graso)';return}
    var btn=form.querySelector('button');btn.disabled=true;
    try{var r=await fetch('/api/waitlist',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:email,source:'landing-new'})});
      if(!r.ok&&r.status!==409)throw new Error(String(r.status));
      msg.textContent='Recibido. Te escribo para agendarla.';msg.style.color='var(--ambar-ink)';track('waitlist_submitted',{source:'landing-new'});form.reset()}
    catch(_){msg.textContent='No se ha podido guardar. Inténtalo de nuevo en un momento.';msg.style.color='var(--graso)'}
    finally{btn.disabled=false}})}
})();
