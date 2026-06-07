#!/usr/bin/env python3
"""
apply_trail_patch.py  — v2 (full hero zone + smoother)
Run: python3 apply_trail_patch.py
Reads index.html, injects image trail, writes index.html
Original backed up as index.html.bak
"""
import shutil, sys, os

SRC = 'index.html'
BAK = 'index.html.bak'

if not os.path.exists(SRC):
    print(f"ERROR: {SRC} not found. Run this from the same folder as index.html")
    sys.exit(1)

shutil.copy2(SRC, BAK)
print(f"Backed up → {BAK}")

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

# ── Remove any previous trail injection so re-running is safe ──
import re
html = re.sub(r'/\* ─── IMAGE TRAIL.*?\}\)\(\);\n', '', html, flags=re.DOTALL)
html = re.sub(r'\n\s*/\* ═+\s*IMAGE TRAIL EFFECT.*?-webkit-user-drag: none;\s*\}\n', '', html, flags=re.DOTALL)

# ────────────────────────────────────────────────────────────────
CSS_BLOCK = """
    /* ═══════════════════════════════════════════════
       IMAGE TRAIL EFFECT v2 — #home hero zone
       Awwwards / Framer / Luxury Fashion
    ═══════════════════════════════════════════════ */
    .trail-img {
      position: fixed;
      pointer-events: none;
      z-index: 1;
      will-change: transform, opacity;
      transform-origin: center center;
      border-radius: 8px;
      overflow: hidden;
      box-shadow:
        0 2px 0 rgba(255,255,255,.55) inset,
        0 20px 60px rgba(0,0,0,.20),
        0 6px 20px rgba(0,0,0,.10);
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
    }
    .trail-img img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center top;
      display: block;
      pointer-events: none;
      user-select: none;
      -webkit-user-drag: none;
    }
"""

JS_BLOCK = r"""
/* ─── IMAGE TRAIL v2 — Desktop only, full #home hero zone ─── */
(function() {
  /* ── Desktop-only guard ── */
  if (window.matchMedia('(max-width:700px)').matches) return;
  if ('ontouchstart' in window && !window.matchMedia('(pointer:fine)').matches) return;

  /* ── Config ── */
  var IMAGES       = ['trail_1','trail_2','trail_3','trail_4','trail_5','trail_6'];
  var IMG_W        = 152;          /* base width px  — 4:5 ratio */
  var IMG_H        = 190;          /* base height px */
  var MAX_VISIBLE  = 8;
  var COOLDOWN_MAX = 95;           /* ms at rest */
  var COOLDOWN_MIN = 26;           /* ms at full speed */
  var VEL_SCALE    = 3.2;          /* how aggressively cooldown shrinks */
  var VEL_THRESH   = 2.5;          /* min vel to spawn */
  var LERP_VEL     = 0.18;         /* smoother velocity (lower = smoother) */

  /* ── State ── */
  var zone = document.getElementById('home');
  if (!zone) return;

  var imgIdx       = 0;
  var activeTrails = [];
  var lastSpawn    = 0;
  var mouseX = 0, mouseY = 0;
  var prevX  = 0, prevY  = 0;
  var smoothVel    = 0;
  var isHovering   = false;
  var rafId        = null;

  /* ── Math helpers ── */
  function lerp(a, b, t) { return a + (b - a) * t; }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  function rand(lo, hi) { return lo + Math.random() * (hi - lo); }

  /* ── Easing ── */
  function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }
  function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }
  function easeInCubic(t)  { return t * t * t; }

  /* ── Spawn ── */
  function spawnTrail(x, y) {
    /* Cull oldest if at cap */
    if (activeTrails.length >= MAX_VISIBLE) {
      var oldest = activeTrails[0];
      if (oldest && !oldest.dying) killTrail(oldest);
    }

    var src      = IMAGES[imgIdx % IMAGES.length]; imgIdx++;
    var rotation = rand(-7, 7);
    var sz       = rand(0.78, 1.12);
    var w        = Math.round(IMG_W * sz);
    var h        = Math.round(IMG_H * sz);

    /* Spawn position: slightly behind cursor, subtle scatter */
    var spawnX = x + rand(-14, 14) - w / 2;
    var spawnY = y + rand(-20, 6)  - h / 2;

    var el = document.createElement('div');
    el.className = 'trail-img';
    el.style.cssText = [
      'width:'   + w    + 'px',
      'height:'  + h    + 'px',
      'left:'    + spawnX + 'px',
      'top:'     + spawnY + 'px',
      'opacity:0',
      'transform:rotate(' + rotation + 'deg) scale(0.84) translate3d(0,6px,0)',
      'transition:none'
    ].join(';');

    var img = document.createElement('img');
    img.src = src + '.webp';
    img.alt = '';
    img.loading = 'eager';
    img.onerror = function() {
      if (this.src.indexOf('.webp') !== -1) this.src = src + '.jpg';
    };
    el.appendChild(img);
    document.body.appendChild(el);

    var trail = {
      el:       el,
      rotation: rotation,
      dying:    false,
      animRaf:  null,
      lifetime: rand(900, 1300)
    };
    activeTrails.push(trail);

    /* ── Fade-in phase ── */
    var inDur   = 340;                    /* slightly longer = smoother feel */
    var inStart = performance.now();

    function fadeIn(now) {
      var t = clamp((now - inStart) / inDur, 0, 1);
      var e = easeOutCubic(t);
      el.style.opacity   = String(e);
      /* scale 0.84 → 1, translateY 6 → 0 */
      el.style.transform = 'rotate(' + rotation + 'deg) scale(' + (0.84 + 0.16 * e) + ') translate3d(0,' + (6 - 6 * e) + 'px,0)';
      if (t < 1) {
        trail.animRaf = requestAnimationFrame(fadeIn);
      } else {
        trail.animRaf = null;
        setTimeout(function() {
          if (!trail.dying) killTrail(trail);
        }, trail.lifetime);
      }
    }
    trail.animRaf = requestAnimationFrame(fadeIn);
  }

  /* ── Kill / fade-out ── */
  function killTrail(trail) {
    if (trail.dying) return;
    trail.dying = true;
    var idx = activeTrails.indexOf(trail);
    if (idx !== -1) activeTrails.splice(idx, 1);
    if (trail.animRaf) { cancelAnimationFrame(trail.animRaf); trail.animRaf = null; }

    var outDur      = 480;
    var outStart    = performance.now();
    var startOpacity = parseFloat(trail.el.style.opacity) || 1;

    function fadeOut(now) {
      var t  = clamp((now - outStart) / outDur, 0, 1);
      var e  = easeInCubic(t);
      var drift = e * 22;          /* floats upward as it disappears */
      trail.el.style.opacity   = String(startOpacity * (1 - e));
      trail.el.style.transform = 'rotate(' + trail.rotation + 'deg) scale(' + (1 - 0.05 * e) + ') translate3d(0,' + (-drift) + 'px,0)';
      if (t < 1) {
        requestAnimationFrame(fadeOut);
      } else {
        if (trail.el.parentNode) trail.el.parentNode.removeChild(trail.el);
      }
    }
    requestAnimationFrame(fadeOut);
  }

  /* ── RAF tick: smooth velocity + spawn gate ── */
  function tick(now) {
    if (!isHovering) {
      activeTrails.slice().forEach(killTrail);
      rafId = null;
      return;
    }
    rafId = requestAnimationFrame(tick);

    var dx = mouseX - prevX;
    var dy = mouseY - prevY;
    /* lerp smooths out jitter between frames */
    smoothVel = lerp(smoothVel, Math.sqrt(dx * dx + dy * dy), LERP_VEL);
    prevX = mouseX;
    prevY = mouseY;

    var cooldown = clamp(COOLDOWN_MAX - smoothVel * VEL_SCALE, COOLDOWN_MIN, COOLDOWN_MAX);

    if (smoothVel > VEL_THRESH && (now - lastSpawn) > cooldown) {
      spawnTrail(mouseX, mouseY);
      lastSpawn = now;
    }
  }

  /* ── Attach to #home (entire hero section) ── */
  zone.addEventListener('mouseenter', function() {
    isHovering = true;
    prevX = mouseX; prevY = mouseY;
    smoothVel = 0;
    if (!rafId) rafId = requestAnimationFrame(tick);
  });

  zone.addEventListener('mouseleave', function() {
    isHovering = false;
    smoothVel  = 0;
    /* Stagger-kill for organic feel */
    activeTrails.slice().forEach(function(t, i) {
      setTimeout(function() { killTrail(t); }, i * 40);
    });
  });

  /* Global mousemove — keeps coords updated at all times */
  document.addEventListener('mousemove', function(e) {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  /* ── Purge on view transitions ── */
  function purgeAll() {
    isHovering = false;
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
    activeTrails.slice().forEach(function(t) {
      if (t.animRaf) cancelAnimationFrame(t.animRaf);
      if (t.el && t.el.parentNode) t.el.parentNode.removeChild(t.el);
    });
    activeTrails = [];
    smoothVel = 0;
  }
  window.trailPurge = purgeAll;

  /* Wrap existing view-switch functions */
  ['showAbout', 'showContact'].forEach(function(fn) {
    if (typeof window[fn] === 'function') {
      var orig = window[fn];
      window[fn] = function() { purgeAll(); orig.apply(this, arguments); };
    }
  });

})();
"""

# ── Inject CSS before </style></head> ──
CSS_ANCHOR = '  </style>\n</head>'
if CSS_ANCHOR not in html:
    print("ERROR: CSS anchor '</style></head>' not found")
    sys.exit(1)
html = html.replace(CSS_ANCHOR, CSS_BLOCK + CSS_ANCHOR, 1)
print("CSS injected ✓")

# ── Inject JS before last </script></body> ──
JS_ANCHOR = '\n</script>\n</body>'
pos = html.rfind(JS_ANCHOR)
if pos == -1:
    print("ERROR: JS anchor '</script></body>' not found")
    sys.exit(1)
html = html[:pos] + '\n' + JS_BLOCK + html[pos:]
print("JS injected ✓")

with open(SRC, 'w', encoding='utf-8') as f:
    f.write(html)

lines = html.count('\n')
print(f"\nDone! {SRC} updated ({len(html):,} chars, {lines:,} lines)")
print("Trail images needed: trail_1.webp → trail_6.webp  (JPG fallback built-in)")
