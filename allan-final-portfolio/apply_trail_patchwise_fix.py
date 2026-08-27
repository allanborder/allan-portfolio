with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update cursor transition to be super crisp & snappy
old_cursor_css = '''    #cursor{position:fixed;width:16px;height:16px;background:white;border-radius:50%;pointer-events:none;z-index:999999;mix-blend-mode:difference;will-change:transform;transform:translate3d(-200px,-200px,0) translate(-50%,-50%);transition:width .18s ease,height .18s ease;opacity:0;}
    #cursor.visible{opacity:1;}
    #cursor.link{width:40px;height:40px;}
    #cursor.card{width:72px;height:72px;}
    #cursor.card::after{content:attr(data-text);position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:9px;font-weight:800;color:#000;white-space:nowrap;letter-spacing:1px;}
    #cursor.contact-cur{width:10px;height:10px;background:var(--dark);mix-blend-mode:normal;}
    #cursor.contact-cur.big{width:36px;height:36px;background:rgba(10,10,10,.12);}'''

new_cursor_css = '''    #cursor{position:fixed;width:14px;height:14px;background:white;border-radius:50%;pointer-events:none;z-index:999999;mix-blend-mode:difference;will-change:transform;transform:translate3d(-200px,-200px,0) translate(-50%,-50%);transition:width .12s cubic-bezier(.16,1,.3,1),height .12s cubic-bezier(.16,1,.3,1),border-radius .12s ease;opacity:0;}
    #cursor.visible{opacity:1;}
    #cursor.link{width:36px;height:36px;}
    #cursor.card{width:64px;height:64px;}
    #cursor.card::after{content:attr(data-text);position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:8.5px;font-weight:800;color:#000;white-space:nowrap;letter-spacing:1px;}
    #cursor.contact-cur{width:10px;height:10px;background:var(--dark);mix-blend-mode:normal;}
    #cursor.contact-cur.big{width:32px;height:32px;background:rgba(10,10,10,.12);}'''

assert old_cursor_css in content, 'old_cursor_css not found'
content = content.replace(old_cursor_css, new_cursor_css, 1)

# 2. Update cursor JavaScript logic for ultra-snappy tracking with event delegation
old_cursor_js = '''/* Cursor */
(function(){
  var c=document.getElementById('cursor');if(!c||window.matchMedia('(max-width:700px)').matches)return;
  var mx=-200,my=-200,cx=-200,cy=-200;
  document.addEventListener('mousemove',function(e){mx=e.clientX;my=e.clientY;if(!c.classList.contains('visible'))c.classList.add('visible');});
  document.addEventListener('mouseleave',function(){c.style.opacity='0';});
  document.addEventListener('mouseenter',function(){if(c.classList.contains('visible'))c.style.opacity='1';});
  (function tick(){cx+=(mx-cx)*.13;cy+=(my-cy)*.13;c.style.transform='translate3d('+cx+'px,'+cy+'px,0) translate(-50%,-50%)';requestAnimationFrame(tick);})();
  document.querySelectorAll('a,button').forEach(function(el){el.addEventListener('mouseenter',function(){if(!c.classList.contains('contact-cur')){c.classList.remove('card');c.classList.add('link');}});el.addEventListener('mouseleave',function(){c.classList.remove('link');});});
  document.querySelectorAll('.feat-proj-visual,.cs2-next-card').forEach(function(el){el.addEventListener('mouseenter',function(){c.classList.remove('link');c.classList.add('card');c.dataset.text='OPEN';});el.addEventListener('mouseleave',function(){c.classList.remove('card');c.dataset.text='VIEW';});});
  document.querySelectorAll('.cert-card,.img-card').forEach(function(el){el.addEventListener('mouseenter',function(){c.classList.add('card');c.dataset.text='VIEW';});el.addEventListener('mouseleave',function(){c.classList.remove('card');});});
})();'''

new_cursor_js = '''/* Cursor (Snappy & Responsive Event Delegation) */
(function(){
  var c=document.getElementById('cursor');if(!c||window.matchMedia('(max-width:700px)').matches)return;
  var mx=-200,my=-200,cx=-200,cy=-200;
  document.addEventListener('mousemove',function(e){
    mx=e.clientX;my=e.clientY;
    if(!c.classList.contains('visible'))c.classList.add('visible');
    
    // Dynamic event delegation so hover states never get stuck
    if(c.classList.contains('contact-cur'))return;
    var target=e.target;
    var openCard=target.closest('.feat-proj-visual, .cs2-next-card');
    var viewCard=target.closest('.cert-card, .img-card');
    var link=target.closest('a, button, .hero-pill, .pc-tag, .feat-proj-tag, .nav-cta, .wf-btn, input, textarea');
    
    if(openCard){
      c.classList.remove('link');c.classList.add('card');c.dataset.text='OPEN';
    }else if(viewCard){
      c.classList.remove('link');c.classList.add('card');c.dataset.text='VIEW';
    }else if(link){
      c.classList.remove('card');c.classList.add('link');
    }else{
      c.classList.remove('link','card');c.dataset.text='VIEW';
    }
  },{passive:true});
  
  document.addEventListener('mouseleave',function(){c.style.opacity='0';c.classList.remove('link','card');});
  document.addEventListener('mouseenter',function(){if(c.classList.contains('visible'))c.style.opacity='1';});
  
  // Fast lerp factor (.26) for immediate, non-laggy cursor tracking
  (function tick(){
    cx+=(mx-cx)*.26;cy+=(my-cy)*.26;
    c.style.transform='translate3d('+cx+'px,'+cy+'px,0) translate(-50%,-50%)';
    requestAnimationFrame(tick);
  })();
})();'''

assert old_cursor_js in content, 'old_cursor_js not found'
content = content.replace(old_cursor_js, new_cursor_js, 1)

# 3. Update Image Trail: smaller, tighter, faster & aesthetic
old_trail_js = '''/* ─── IMAGE TRAIL ─── */
(function(){
  if(window.matchMedia('(max-width:700px)').matches)return;
  if('ontouchstart' in window&&!window.matchMedia('(pointer:fine)').matches)return;
  var IMAGES=['trail_1','trail_2','trail_3','trail_4','trail_5','trail_6'];
  var IMG_W=152,IMG_H=190,MAX_VISIBLE=8,COOLDOWN_MAX=95,COOLDOWN_MIN=26,VEL_SCALE=3.2,VEL_THRESH=2.5,LERP_VEL=0.18;
  var zone=document.getElementById('home');if(!zone)return;
  var imgIdx=0,activeTrails=[],lastSpawn=0,mouseX=0,mouseY=0,prevX=0,prevY=0,smoothVel=0,isHovering=false,rafId=null;
  function lerp(a,b,t){return a+(b-a)*t;}function clamp(v,lo,hi){return Math.max(lo,Math.min(hi,v));}function rand(lo,hi){return lo+Math.random()*(hi-lo);}function easeOutCubic(t){return 1-Math.pow(1-t,3);}function easeInCubic(t){return t*t*t;}
  function spawnTrail(x,y){
    if(activeTrails.length>=MAX_VISIBLE){var oldest=activeTrails[0];if(oldest&&!oldest.dying)killTrail(oldest);}
    var src=IMAGES[imgIdx%IMAGES.length];imgIdx++;var rotation=rand(-7,7),sz=rand(0.78,1.12),w=Math.round(IMG_W*sz),h=Math.round(IMG_H*sz);
    var spawnX=x+rand(-14,14)-w/2,spawnY=y+rand(-20,6)-h/2;
    var el=document.createElement('div');el.className='trail-img';el.style.cssText=['width:'+w+'px','height:'+h+'px','left:'+spawnX+'px','top:'+spawnY+'px','opacity:0','transform:rotate('+rotation+'deg) scale(0.84) translate3d(0,6px,0)','transition:none'].join(';');
    var img=document.createElement('img');img.src=src+'.webp';img.alt='';img.loading='eager';img.onerror=function(){if(this.src.indexOf('.webp')!==-1)this.src=src+'.jpg';};el.appendChild(img);document.body.appendChild(el);
    var trail={el:el,rotation:rotation,dying:false,animRaf:null,lifetime:rand(900,1300)};activeTrails.push(trail);
    var inDur=340,inStart=performance.now();
    function fadeIn(now){var t=clamp((now-inStart)/inDur,0,1),e=easeOutCubic(t);el.style.opacity=String(e);el.style.transform='rotate('+rotation+'deg) scale('+(0.84+0.16*e)+') translate3d(0,'+(6-6*e)+'px,0)';if(t<1){trail.animRaf=requestAnimationFrame(fadeIn);}else{trail.animRaf=null;setTimeout(function(){if(!trail.dying)killTrail(trail);},trail.lifetime);}}
    trail.animRaf=requestAnimationFrame(fadeIn);
  }
  function killTrail(trail){
    if(trail.dying)return;trail.dying=true;var idx=activeTrails.indexOf(trail);if(idx!==-1)activeTrails.splice(idx,1);if(trail.animRaf){cancelAnimationFrame(trail.animRaf);trail.animRaf=null;}
    var outDur=480,outStart=performance.now(),startOpacity=parseFloat(trail.el.style.opacity)||1;
    function fadeOut(now){var t=clamp((now-outStart)/outDur,0,1),e=easeInCubic(t),drift=e*22;trail.el.style.opacity=String(startOpacity*(1-e));trail.el.style.transform='rotate('+trail.rotation+'deg) scale('+(1-0.05*e)+') translate3d(0,'+(-drift)+'px,0)';if(t<1){requestAnimationFrame(fadeOut);}else{if(trail.el.parentNode)trail.el.parentNode.removeChild(trail.el);}}
    requestAnimationFrame(fadeOut);
  }
  function tick(now){if(!isHovering){activeTrails.slice().forEach(killTrail);rafId=null;return;}rafId=requestAnimationFrame(tick);var dx=mouseX-prevX,dy=mouseY-prevY;smoothVel=lerp(smoothVel,Math.sqrt(dx*dx+dy*dy),LERP_VEL);prevX=mouseX;prevY=mouseY;var cooldown=clamp(COOLDOWN_MAX-smoothVel*VEL_SCALE,COOLDOWN_MIN,COOLDOWN_MAX);if(smoothVel>VEL_THRESH&&(now-lastSpawn)>cooldown){spawnTrail(mouseX,mouseY);lastSpawn=now;}}
  zone.addEventListener('mouseenter',function(){isHovering=true;prevX=mouseX;prevY=mouseY;smoothVel=0;if(!rafId)rafId=requestAnimationFrame(tick);});
  zone.addEventListener('mouseleave',function(){isHovering=false;smoothVel=0;activeTrails.slice().forEach(function(t,i){setTimeout(function(){killTrail(t);},i*40);});});
  document.addEventListener('mousemove',function(e){mouseX=e.clientX;mouseY=e.clientY;},{passive:true});
  function purgeAll(){isHovering=false;if(rafId){cancelAnimationFrame(rafId);rafId=null;}activeTrails.slice().forEach(function(t){if(t.animRaf)cancelAnimationFrame(t.animRaf);if(t.el&&t.el.parentNode)t.el.parentNode.removeChild(t.el);});activeTrails=[];smoothVel=0;}
  window.trailPurge=purgeAll;
  ['showAbout','showContact'].forEach(function(fn){if(typeof window[fn]==='function'){var orig=window[fn];window[fn]=function(){purgeAll();orig.apply(this,arguments);};}});
})();'''

new_trail_js = '''/* ─── IMAGE TRAIL (Compact, Faster & Elegant) ─── */
(function(){
  if(window.matchMedia('(max-width:700px)').matches)return;
  if('ontouchstart' in window&&!window.matchMedia('(pointer:fine)').matches)return;
  var IMAGES=['trail_1','trail_2','trail_3','trail_4','trail_5','trail_6'];
  var IMG_W=110,IMG_H=138,MAX_VISIBLE=7,COOLDOWN_MAX=75,COOLDOWN_MIN=20,VEL_SCALE=3.5,VEL_THRESH=2.2,LERP_VEL=0.22;
  var zone=document.getElementById('home');if(!zone)return;
  var imgIdx=0,activeTrails=[],lastSpawn=0,mouseX=0,mouseY=0,prevX=0,prevY=0,smoothVel=0,isHovering=false,rafId=null;
  function lerp(a,b,t){return a+(b-a)*t;}function clamp(v,lo,hi){return Math.max(lo,Math.min(hi,v));}function rand(lo,hi){return lo+Math.random()*(hi-lo);}function easeOutCubic(t){return 1-Math.pow(1-t,3);}function easeInCubic(t){return t*t*t;}
  function spawnTrail(x,y){
    if(activeTrails.length>=MAX_VISIBLE){var oldest=activeTrails[0];if(oldest&&!oldest.dying)killTrail(oldest);}
    var src=IMAGES[imgIdx%IMAGES.length];imgIdx++;var rotation=rand(-6,6),sz=rand(0.85,1.05),w=Math.round(IMG_W*sz),h=Math.round(IMG_H*sz);
    var spawnX=x+rand(-10,10)-w/2,spawnY=y+rand(-14,4)-h/2;
    var el=document.createElement('div');el.className='trail-img';el.style.cssText=['width:'+w+'px','height:'+h+'px','left:'+spawnX+'px','top:'+spawnY+'px','opacity:0','transform:rotate('+rotation+'deg) scale(0.88) translate3d(0,4px,0)','transition:none'].join(';');
    var img=document.createElement('img');img.src=src+'.webp';img.alt='';img.loading='eager';img.onerror=function(){if(this.src.indexOf('.webp')!==-1)this.src=src+'.jpg';};el.appendChild(img);document.body.appendChild(el);
    var trail={el:el,rotation:rotation,dying:false,animRaf:null,lifetime:rand(650,950)};activeTrails.push(trail);
    var inDur=220,inStart=performance.now();
    function fadeIn(now){var t=clamp((now-inStart)/inDur,0,1),e=easeOutCubic(t);el.style.opacity=String(e);el.style.transform='rotate('+rotation+'deg) scale('+(0.88+0.12*e)+') translate3d(0,'+(4-4*e)+'px,0)';if(t<1){trail.animRaf=requestAnimationFrame(fadeIn);}else{trail.animRaf=null;setTimeout(function(){if(!trail.dying)killTrail(trail);},trail.lifetime);}}
    trail.animRaf=requestAnimationFrame(fadeIn);
  }
  function killTrail(trail){
    if(trail.dying)return;trail.dying=true;var idx=activeTrails.indexOf(trail);if(idx!==-1)activeTrails.splice(idx,1);if(trail.animRaf){cancelAnimationFrame(trail.animRaf);trail.animRaf=null;}
    var outDur=320,outStart=performance.now(),startOpacity=parseFloat(trail.el.style.opacity)||1;
    function fadeOut(now){var t=clamp((now-outStart)/outDur,0,1),e=easeInCubic(t),drift=e*16;trail.el.style.opacity=String(startOpacity*(1-e));trail.el.style.transform='rotate('+trail.rotation+'deg) scale('+(1-0.04*e)+') translate3d(0,'+(-drift)+'px,0)';if(t<1){requestAnimationFrame(fadeOut);}else{if(trail.el.parentNode)trail.el.parentNode.removeChild(trail.el);}}
    requestAnimationFrame(fadeOut);
  }
  function tick(now){if(!isHovering){activeTrails.slice().forEach(killTrail);rafId=null;return;}rafId=requestAnimationFrame(tick);var dx=mouseX-prevX,dy=mouseY-prevY;smoothVel=lerp(smoothVel,Math.sqrt(dx*dx+dy*dy),LERP_VEL);prevX=mouseX;prevY=mouseY;var cooldown=clamp(COOLDOWN_MAX-smoothVel*VEL_SCALE,COOLDOWN_MIN,COOLDOWN_MAX);if(smoothVel>VEL_THRESH&&(now-lastSpawn)>cooldown){spawnTrail(mouseX,mouseY);lastSpawn=now;}}
  zone.addEventListener('mouseenter',function(){isHovering=true;prevX=mouseX;prevY=mouseY;smoothVel=0;if(!rafId)rafId=requestAnimationFrame(tick);});
  zone.addEventListener('mouseleave',function(){isHovering=false;smoothVel=0;activeTrails.slice().forEach(function(t,i){setTimeout(function(){killTrail(t);},i*30);});});
  document.addEventListener('mousemove',function(e){mouseX=e.clientX;mouseY=e.clientY;},{passive:true});
  function purgeAll(){isHovering=false;if(rafId){cancelAnimationFrame(rafId);rafId=null;}activeTrails.slice().forEach(function(t){if(t.animRaf)cancelAnimationFrame(t.animRaf);if(t.el&&t.el.parentNode)t.el.parentNode.removeChild(t.el);});activeTrails=[];smoothVel=0;}
  window.trailPurge=purgeAll;
  ['showAbout','showContact'].forEach(function(fn){if(typeof window[fn]==='function'){var orig=window[fn];window[fn]=function(){purgeAll();orig.apply(this,arguments);};}});
})();'''

assert old_trail_js in content, 'old_trail_js not found'
content = content.replace(old_trail_js, new_trail_js, 1)

# 4. Update Project 06 heading to Patchwise
old_proj06_html = '''        <!-- 06 / NEXORA HACKATHON -->
        <article class="feat-project-row row-reverse" data-project="nexora">
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Rapid Prototype · 24h Hackathon Finalist</div>
            <h3 class="feat-proj-title">Nexora AI System</h3>
            <p class="feat-proj-tagline">Real-time modular software pipeline engineered under intense 24-hour hackathon conditions at Nexora — built for high throughput and rapid processing.</p>'''

new_proj06_html = '''        <!-- 06 / PATCHWISE (NEXORA HACKATHON) -->
        <article class="feat-project-row row-reverse" data-project="nexora">
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Nexora Hackathon Finalist · Rapid Prototype</div>
            <h3 class="feat-proj-title">Patchwise</h3>
            <p class="feat-proj-tagline">Intelligent real-time pipeline engineered under intense 24-hour hackathon sprint conditions at Nexora — built for high throughput and rapid modular processing.</p>'''

assert old_proj06_html in content, 'old_proj06_html not found'
content = content.replace(old_proj06_html, new_proj06_html, 1)

# 5. Update PROJECTS dictionary entry for nexora -> Patchwise
old_nexora_dict = '''  nexora:{
    num:'06',badge:'Hackathon · AI Pipeline · 2025',title:'Nexora AI System',
    heroDesc:'A rapid-prototype real-time AI and data processing solution engineered under intense 24-hour hackathon conditions at Nexora — featuring modular pipelines and sub-second processing.','''

new_nexora_dict = '''  nexora:{
    num:'06',badge:'Nexora Hackathon Finalist · Rapid Prototype · 2025',title:'Patchwise',
    heroDesc:'An intelligent real-time processing solution engineered under intense 24-hour hackathon conditions at Nexora — featuring modular pipelines and sub-second execution.',
'''
assert old_nexora_dict in content, 'old_nexora_dict not found'
content = content.replace(old_nexora_dict, new_nexora_dict, 1)

# 6. Update quote in nexora case study
old_nexora_quote = "Allan Paulraj on Nexora"
new_nexora_quote = "Allan Paulraj on Patchwise"
if old_nexora_quote in content:
    content = content.replace(old_nexora_quote, new_nexora_quote, 1)

# 7. Update terminal command list for Patchwise
old_term_nexora = "'<span class=\"t-o\">6. <span class=\"t-v\">Nexora AI</span>         — Rapid Hackathon Pipeline</span>'"
new_term_nexora = "'<span class=\"t-o\">6. <span class=\"t-v\">Patchwise</span>         — Nexora Hackathon Finalist Prototype</span>'"
if old_term_nexora in content:
    content = content.replace(old_term_nexora, new_term_nexora, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html: Patchwise project heading + snappy cursor + compact fast trail!')
