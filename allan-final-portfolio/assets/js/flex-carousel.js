/**
 * FlexCarousel — React Bits (Vanilla JS Port with OGL)
 * WebGL-powered liquid-glass refraction carousel
 */
(function (global) {
  'use strict';

  var BEND_PRESETS = {
    liquid: {
      lensWidth: 0.74,
      lensHeight: 1.18,
      tilt: 62,
      roundness: 1,
      bend: 0.34,
      reach: 0.38,
      curl: 'twist',
      dispersion: 0.45,
      liquid: 0,
      followCursor: false
    },
    ribbon: {
      lensWidth: 0.8,
      lensHeight: 0.8,
      tilt: 0,
      roundness: 1,
      bend: 0.34,
      reach: 0.34,
      curl: 'twist',
      dispersion: 0.4,
      liquid: 0,
      followCursor: false
    },
    vortex: {
      lensWidth: 0.7,
      lensHeight: 0.95,
      tilt: 30,
      roundness: 1,
      bend: 0.46,
      reach: 0.3,
      curl: 'twist',
      dispersion: 0.5,
      liquid: 0,
      followCursor: false
    },
    arch: {
      lensWidth: 0.8,
      lensHeight: 0.8,
      tilt: 0,
      roundness: 1,
      bend: 0.3,
      reach: 0.36,
      curl: 'rise',
      dispersion: 0.4,
      liquid: 0,
      followCursor: false
    }
  };

  var FIT_ASPECT = { portrait: 0.75, square: 1, landscape: 4 / 3 };
  var TAPS = 12;
  var PIXEL_BUDGET = 4.5e6;
  var INTRO_DURATION = { rise: 2.1, bloom: 1.6, spin: 2.2, deal: 1.5, fade: 0.35 };

  var wrap = function (val, sz) { return ((((val + sz / 2) % sz) + sz) % sz) - sz / 2; };
  var clamp01 = function (v) { return Math.min(Math.max(v, 0), 1); };
  var easeOut = function (v) { return 1 - Math.pow(1 - clamp01(v), 3); };
  var easeOutQuint = function (v) { return 1 - Math.pow(1 - clamp01(v), 5); };
  var easeInOut = function (v) {
    var t = clamp01(v);
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  };

  var cardVertex = `#version 300 es
in vec3 position;
in vec2 uv;
uniform vec4 uRect;
uniform vec2 uResolution;
out vec2 vUv;
out vec2 vLocal;
void main() {
  vUv = uv;
  vLocal = vec2(position.x, -position.y) * uRect.zw;
  vec2 px = uRect.xy + vLocal;
  gl_Position = vec4(px.x / uResolution.x * 2.0 - 1.0, 1.0 - px.y / uResolution.y * 2.0, 0.0, 1.0);
}
`;

  var cardFragment = `#version 300 es
precision highp float;
uniform sampler2D tMap;
uniform vec2 uSize;
uniform vec2 uImage;
uniform float uRadius;
uniform float uAlpha;
uniform float uReady;
uniform float uShift;
uniform float uDpr;
uniform vec3 uPlaceholder;
in vec2 vUv;
in vec2 vLocal;
out vec4 fragColor;

float roundedBox(vec2 p, vec2 b, float r) {
  vec2 q = abs(p) - b + r;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
}

void main() {
  float sd = roundedBox(vLocal, uSize * 0.5, min(uRadius, min(uSize.x, uSize.y) * 0.5));
  float mask = clamp(0.5 - sd * uDpr, 0.0, 1.0);
  vec2 local = vLocal / uSize + 0.5;
  float cardAspect = uSize.x / uSize.y;
  float imageAspect = uImage.x / max(uImage.y, 1.0);
  vec2 scale = imageAspect > cardAspect ? vec2(cardAspect / imageAspect, 1.0) : vec2(1.0, imageAspect / cardAspect);
  scale /= 1.08;
  vec2 uv = vec2(local.x, 1.0 - local.y);
  uv = (uv - 0.5) * scale + 0.5;
  uv.x += uShift * (1.0 - scale.x) * 0.5;
  vec3 image = texture(tMap, uv).rgb;
  vec3 color = mix(uPlaceholder, image, uReady);
  float alpha = mask * uAlpha;
  fragColor = vec4(color * alpha, alpha);
}
`;

  var lensVertex = `#version 300 es
in vec2 position;
void main() {
  gl_Position = vec4(position, 0.0, 1.0);
}
`;

  var lensFragment = `#version 300 es
precision highp float;
uniform sampler2D tScene;
uniform vec2 uResolution;
uniform float uDpr;
uniform vec2 uCenter;
uniform vec2 uHalf;
uniform float uAngle;
uniform float uExponent;
uniform float uInner;
uniform float uOuter;
uniform float uFlow;
uniform float uCurl;
uniform float uDispersion;
uniform float uStrength;
uniform float uSceneAlpha;
out vec4 fragColor;

void main() {
  vec2 frag = gl_FragCoord.xy / uDpr;
  vec2 uv = frag / uResolution;
  vec2 rel = frag - vec2(uCenter.x, uResolution.y - uCenter.y);
  float ca = cos(uAngle);
  float sa = sin(uAngle);
  vec2 local = vec2(ca * rel.x + sa * rel.y, -sa * rel.x + ca * rel.y);
  vec2 k = max(abs(local) / uHalf, vec2(1e-5));
  float nd = pow(pow(k.x, uExponent) + pow(k.y, uExponent), 1.0 / uExponent);
  vec2 grad = pow(k, vec2(uExponent - 1.0)) * sign(local) / uHalf * pow(nd, 1.0 - uExponent);
  float glen = max(length(grad), 1e-6);
  float edge = (nd - 1.0) / glen;
  vec2 outward = grad / glen;
  vec2 normal = vec2(ca * outward.x - sa * outward.y, sa * outward.x + ca * outward.y);
  vec2 along = vec2(-normal.y, normal.x);

  float t = clamp((edge + uInner) / (uInner + uOuter), 0.0, 1.0);
  float ramp = t * t * t * (t * (t * 6.0 - 15.0) + 10.0);
  float slope = 16.0 * t * t * (1.0 - t) * (1.0 - t);
  float reachX = rel.x / (uResolution.x * 0.5);
  float side = smoothstep(0.02, 0.3, abs(reachX)) * (uCurl == 0.0 ? sign(reachX) : uCurl);
  float lift = ramp * side * uFlow * uStrength;
  vec2 swirl = along * along.y * side * slope * uFlow * uStrength * 0.35;
  vec2 drift = vec2(0.0, -lift) - swirl;
  vec2 shifted = uv + drift / uResolution;

  vec2 texels = uResolution * uDpr;
  vec2 gx = dFdx(shifted);
  vec2 gy = dFdy(shifted);
  gx *= min(1.0, 3.0 / max(length(gx * texels), 1e-4));
  gy *= min(1.0, 3.0 / max(length(gy * texels), 1e-4));

  vec4 color = textureGrad(tScene, shifted, gx, gy);
  vec2 spread = vec2(0.0, side * slope * uFlow * uStrength) / uResolution * uDispersion;
  float spreadPx = length(spread * texels);
  if (color.a > 0.002 && spreadPx > 0.25) {
    vec3 base = color.rgb / color.a;
    vec3 sumColor = vec3(0.0);
    vec3 sumWeight = vec3(0.0);
    for (int i = 0; i < ${TAPS}; i++) {
      float s = (float(i) + 0.5) / float(${TAPS});
      vec4 c = textureGrad(tScene, shifted + spread * (s - 0.5), gx, gy);
      vec3 w = max(1.0 - abs(vec3(s) - vec3(0.15, 0.5, 0.85)) * 2.6, 0.0) * c.a;
      sumColor += c.rgb * (w / max(c.a, 0.002));
      sumWeight += w;
    }
    vec3 split = mix(base, sumColor / max(sumWeight, vec3(1e-4)), clamp(sumWeight * 2.0, 0.0, 1.0));
    color.rgb = mix(color.rgb, clamp(split, 0.0, 1.0) * color.a, smoothstep(0.25, 1.5, spreadPx));
  }

  fragColor = color * uSceneAlpha;
}
`;

  function initFlexCarousel(container, options) {
    if (!container) return null;
    options = options || {};

    var OGL = global.OGL;
    if (!OGL) {
      console.warn('OGL library not found on global scope');
      return null;
    }

    var Renderer = OGL.Renderer;
    var Program = OGL.Program;
    var Mesh = OGL.Mesh;
    var Triangle = OGL.Triangle;
    var Plane = OGL.Plane;
    var Texture = OGL.Texture;
    var RenderTarget = OGL.RenderTarget;

    var list = options.items || [];
    var preset = options.preset || 'liquid';
    var base = BEND_PRESETS[preset] || BEND_PRESETS.liquid;
    var pick = function (v, k) { return v === undefined || v === null ? base[k] : v; };

    var settings = {
      intro: options.intro || 'rise',
      cardHeight: options.cardHeight || 0.52,
      gap: options.gap !== undefined ? options.gap : 14,
      radius: options.radius !== undefined ? options.radius : 14,
      fit: options.fit || 'natural',
      lensWidth: pick(options.lensWidth, 'lensWidth'),
      lensHeight: pick(options.lensHeight, 'lensHeight'),
      tilt: pick(options.tilt, 'tilt'),
      roundness: pick(options.roundness, 'roundness'),
      bend: pick(options.bend, 'bend'),
      reach: pick(options.reach, 'reach'),
      curl: pick(options.curl, 'curl'),
      dispersion: pick(options.dispersion, 'dispersion'),
      liquid: pick(options.liquid, 'liquid'),
      followCursor: pick(options.followCursor, 'followCursor'),
      squeeze: options.squeeze !== undefined ? options.squeeze : 0.2,
      focusOnClick: options.focusOnClick !== undefined ? options.focusOnClick : true,
      autoplay: options.autoplay || false,
      interval: options.interval || 4,
      captureWheel: options.captureWheel !== undefined ? options.captureWheel : true,
      captions: options.captions !== undefined ? options.captions : true
    };

    container.classList.add('flex-carousel');
    container.style.setProperty('--flex-carousel-half', (Math.min(Math.max(settings.cardHeight, 0.05), 1) * 50) + '%');

    var renderer;
    try {
      renderer = new Renderer({
        dpr: Math.min(window.devicePixelRatio || 1, 2),
        alpha: true,
        premultipliedAlpha: true,
        antialias: false,
        depth: false
      });
    } catch (e) {
      console.warn('WebGL initialization failed for FlexCarousel:', e);
      return null;
    }

    var gl = renderer.gl;
    if (!renderer.isWebgl2) {
      try { gl.getExtension('WEBGL_lose_context')?.loseContext(); } catch (err) {}
      console.warn('FlexCarousel requires WebGL2');
      return null;
    }

    gl.clearColor(0, 0, 0, 0);
    var canvas = gl.canvas;
    canvas.style.display = 'block';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.setAttribute('aria-hidden', 'true');
    container.prepend(canvas);

    // Caption Elements
    var captionEl = null;
    var titleEl = null;
    var subtitleEl = null;
    var countEl = null;
    var tensReel = null;
    var onesReel = null;

    if (settings.captions) {
      captionEl = document.createElement('div');
      captionEl.className = 'flex-carousel__caption';
      captionEl.setAttribute('aria-hidden', 'true');

      var titleWrap = document.createElement('span');
      titleWrap.className = 'flex-carousel__title';

      titleEl = document.createElement('span');
      titleEl.className = 'fc-title-text';
      titleWrap.appendChild(titleEl);

      subtitleEl = document.createElement('span');
      subtitleEl.className = 'flex-carousel__subtitle';
      titleWrap.appendChild(subtitleEl);

      captionEl.appendChild(titleWrap);

      countEl = document.createElement('span');
      countEl.className = 'flex-carousel__count';

      var digitsWrap = document.createElement('span');
      digitsWrap.className = 'flex-carousel__digits';

      var digitTens = document.createElement('span');
      digitTens.className = 'flex-carousel__digit';
      tensReel = document.createElement('span');
      tensReel.className = 'flex-carousel__reel';
      for (var d = 0; d <= 9; d++) {
        var sp = document.createElement('span');
        sp.textContent = d;
        tensReel.appendChild(sp);
      }
      digitTens.appendChild(tensReel);

      var digitOnes = document.createElement('span');
      digitOnes.className = 'flex-carousel__digit';
      onesReel = document.createElement('span');
      onesReel.className = 'flex-carousel__reel';
      for (var d2 = 0; d2 <= 9; d2++) {
        var sp2 = document.createElement('span');
        sp2.textContent = d2;
        onesReel.appendChild(sp2);
      }
      digitOnes.appendChild(onesReel);

      digitsWrap.appendChild(digitTens);
      digitsWrap.appendChild(digitOnes);
      countEl.appendChild(digitsWrap);

      var slash = document.createElement('span');
      slash.className = 'flex-carousel__slash';
      slash.textContent = '/';
      countEl.appendChild(slash);

      var totalSpan = document.createElement('span');
      totalSpan.className = 'fc-count-total';
      totalSpan.textContent = String(list.length).padStart(2, '0');
      countEl.appendChild(totalSpan);

      captionEl.appendChild(countEl);
      container.appendChild(captionEl);
    }

    var cardProgram = new Program(gl, {
      vertex: cardVertex,
      fragment: cardFragment,
      transparent: true,
      depthTest: false,
      depthWrite: false,
      uniforms: {
        tMap: { value: new Texture(gl) },
        uRect: { value: [0, 0, 1, 1] },
        uResolution: { value: [1, 1] },
        uSize: { value: [1, 1] },
        uImage: { value: [1, 1] },
        uRadius: { value: 16 },
        uAlpha: { value: 1 },
        uReady: { value: 0 },
        uShift: { value: 0 },
        uDpr: { value: 1 },
        uPlaceholder: { value: [0.5, 0.5, 0.5] }
      }
    });
    cardProgram.setBlendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
    var cardMesh = new Mesh(gl, { geometry: new Plane(gl), program: cardProgram });

    var target = new RenderTarget(gl, {
      width: 2,
      height: 2,
      depth: false,
      minFilter: gl.LINEAR_MIPMAP_LINEAR,
      magFilter: gl.LINEAR
    });

    var lensUniforms = {
      tScene: { value: target.texture },
      uResolution: { value: [1, 1] },
      uDpr: { value: 1 },
      uCenter: { value: [0, 0] },
      uHalf: { value: [1, 1] },
      uAngle: { value: 0 },
      uExponent: { value: 2 },
      uInner: { value: 60 },
      uOuter: { value: 80 },
      uFlow: { value: 0 },
      uCurl: { value: 0 },
      uDispersion: { value: 0 },
      uStrength: { value: 0 },
      uSceneAlpha: { value: 0 }
    };
    var lensMesh = new Mesh(gl, {
      geometry: new Triangle(gl),
      program: new Program(gl, {
        vertex: lensVertex,
        fragment: lensFragment,
        uniforms: lensUniforms,
        depthTest: false,
        depthWrite: false
      })
    });

    var reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var anisotropy = renderer.getExtension('EXT_texture_filter_anisotropic') ? 8 : 0;

    var slots = [];
    var width = 1;
    var height = 1;
    var pos = 0;
    var vel = 0;
    var goal = 0;
    var mode = 'spring';
    var wheelAt = 0;
    var raf = 0;
    var last = performance.now();
    var visible = true;
    var alive = true;
    var dirty = true;
    var activeIndex = -1;
    var interactedAt = -Infinity;
    var autoplayAt = performance.now();
    var hasFocus = false;
    var deform = 0;
    var deformVel = 0;
    var layout = null;
    var resnap = false;
    var hover = '';
    var lift = 1;
    var energy = 0;
    var lastPos = 0;
    var lens = { x: 0, y: 0, vx: 0, vy: 0, ready: false };
    var pointer = {
      x: 0,
      y: 0,
      over: false,
      down: false,
      id: -1,
      startX: 0,
      startY: 0,
      startPos: 0,
      dragging: false,
      touch: false,
      samples: []
    };
    var introState = { kind: 'none', t: 0, running: false, done: false, readyAt: 0 };
    var focus = { index: -1, pending: -1, t: 0, v: 0, target: 0 };
    var instances = [];

    var loadSlot = function (item, index) {
      var texture = new Texture(gl, {
        generateMipmaps: true,
        minFilter: gl.LINEAR_MIPMAP_LINEAR,
        magFilter: gl.LINEAR,
        anisotropy: anisotropy
      });
      var slot = {
        item: item,
        index: index,
        texture: texture,
        aspect: 0.8,
        loaded: false,
        failed: false,
        ready: 0,
        color: [0.35, 0.35, 0.35],
        image: [1, 1],
        dispose: function () {}
      };
      var img = new Image();
      if (item.src && (item.src.indexOf('http://') === 0 || item.src.indexOf('https://') === 0)) {
        try {
          if (typeof window !== 'undefined' && item.src.indexOf(window.location.origin) !== 0) {
            img.crossOrigin = 'anonymous';
          }
        } catch (e) {
          img.crossOrigin = 'anonymous';
        }
      }
      img.decoding = 'async';
      img.onload = function () {
        if (!alive || slots.indexOf(slot) === -1) return;
        texture.image = img;
        texture.update();
        slot.image = [img.naturalWidth || 1, img.naturalHeight || 1];
        slot.aspect = slot.image[0] / slot.image[1];
        try {
          var probe = document.createElement('canvas');
          probe.width = 8;
          probe.height = 8;
          var pctx = probe.getContext('2d', { willReadFrequently: true });
          if (pctx) {
            pctx.drawImage(img, 0, 0, 8, 8);
            var dt = pctx.getImageData(0, 0, 8, 8).data;
            var avg = [0, 0, 0];
            for (var i = 0; i < dt.length; i += 4) {
              avg[0] += dt[i];
              avg[1] += dt[i + 1];
              avg[2] += dt[i + 2];
            }
            slot.color = avg.map(function (v) { return v / 64 / 255; });
          }
        } catch (e) {
          slot.color = [0.35, 0.35, 0.35];
        }
        slot.loaded = true;
        dirty = true;
        start();
      };
      img.onerror = function () {
        if (!alive) return;
        slot.failed = true;
        dirty = true;
        start();
      };
      img.src = item.src;
      slot.dispose = function () {
        img.onload = null;
        img.onerror = null;
        try { gl.deleteTexture(texture.texture); } catch (e) {}
      };
      return slot;
    };

    var setItems = function (next) {
      slots.forEach(function (s) { s.dispose(); });
      slots = next.map(loadSlot);
      activeIndex = -1;
      layout = null;
      resnap = true;
      focus.target = 0;
      focus.t = 0;
      focus.v = 0;
      focus.pending = -1;
      introState.readyAt = performance.now();
      dirty = true;
      start();
    };

    var metrics = function (s) {
      var cardH = Math.max(24, s.cardHeight * height);
      var fixed = FIT_ASPECT[s.fit];
      var widths = slots.map(function (slot) { return (fixed || slot.aspect) * cardH; });
      var centers = [];
      var cursor = 0;
      for (var i = 0; i < widths.length; i++) {
        centers.push(cursor + widths[i] / 2);
        cursor += widths[i] + s.gap;
      }
      return { cardH: cardH, widths: widths, centers: centers, gap: s.gap, loop: Math.max(cursor, 1) };
    };

    var nearest = function (m, at) {
      var best = 0;
      var bestDist = Infinity;
      for (var i = 0; i < m.centers.length; i++) {
        var dist = Math.abs(wrap(m.centers[i] - at, m.loop));
        if (dist < bestDist) {
          bestDist = dist;
          best = i;
        }
      }
      return best;
    };

    var snapPoint = function (m, at) {
      var i = nearest(m, at);
      return at + wrap(m.centers[i] - at, m.loop);
    };

    var remap = function (from, to, at) {
      var i = nearest(from, at);
      var offset = wrap(at - from.centers[i], from.loop);
      var cycles = Math.round((at - offset - from.centers[i]) / from.loop);
      return cycles * to.loop + to.centers[i] + offset * (to.widths[i] / from.widths[i]);
    };

    var step = function (m, delta) {
      var at = snapPoint(m, goal);
      var index = nearest(m, at);
      var n = m.centers.length;
      for (var k = 0; k < Math.abs(delta); k++) {
        var next = (index + (delta > 0 ? 1 : n - 1)) % n;
        var distance = delta > 0
          ? m.widths[index] / 2 + m.gap + m.widths[next] / 2
          : -(m.widths[next] / 2 + m.gap + m.widths[index] / 2);
        at += distance;
        index = next;
      }
      goal = at;
      mode = 'spring';
      dirty = true;
      start();
    };

    var goTo = function (m, index) {
      var i = ((index % m.centers.length) + m.centers.length) % m.centers.length;
      goal = goal + wrap(m.centers[i] - goal, m.loop);
      mode = 'spring';
      dirty = true;
      start();
    };

    var openFocus = function (index) {
      focus.index = index;
      focus.pending = -1;
      focus.target = 1;
      if (countEl) countEl.setAttribute('data-hidden', '');
      dirty = true;
      start();
    };

    var closeFocus = function () {
      focus.pending = -1;
      if (focus.target === 0) return false;
      focus.target = 0;
      if (countEl) countEl.removeAttribute('data-hidden');
      dirty = true;
      start();
      return true;
    };

    var skipIntro = function () {
      if (introState.running) introState.t = 1;
    };

    var introEffects = function () {
      var t = introState.running ? introState.t : introState.done ? 1 : 0;
      var e = { sceneAlpha: 1, strength: 1, card: null };
      if (!introState.done && !introState.running) {
        e.sceneAlpha = 0;
        e.strength = 0;
        return e;
      }
      if (t >= 1) return e;
      var kind = introState.kind;
      if (kind === 'rise') {
        e.strength = easeInOut((t - 0.3) / 0.65);
        e.card = function (rel) {
          var delay = Math.min(Math.abs(rel) / (width * 0.6), 1) * 0.34;
          var local = clamp01((t - delay) / 0.6);
          return {
            alpha: clamp01(local * 4),
            x: 0,
            y: (1 - easeOutQuint(local)) * height * 0.62,
            scale: 0.5 + 0.5 * easeInOut((local - 0.18) / 0.82)
          };
        };
      } else if (kind === 'bloom') {
        e.strength = easeInOut((t - 0.2) / 0.8);
        e.card = function (rel) {
          var delay = Math.min(Math.abs(rel) / (width * 0.6), 1) * 0.25;
          var local = easeOut((t - delay) / 0.55);
          return { alpha: local, x: 0, y: 0, scale: 0.92 + 0.08 * local };
        };
      } else if (kind === 'spin') {
        e.sceneAlpha = easeOut(t / 0.25);
        e.strength = easeOut((t - 0.55) / 0.45);
      } else if (kind === 'deal') {
        e.strength = easeOut((t - 0.45) / 0.5);
        e.card = function (rel) {
          var spread = Math.min(Math.abs(rel) / (width * 0.6), 1) * 0.3;
          var local = easeOut((t - 0.12 - spread) / 0.5);
          return { alpha: easeOut((t - spread) / 0.12), x: -rel * (1 - local), y: 0, scale: 1 };
        };
      } else {
        e.sceneAlpha = easeOut(t);
        e.strength = easeOut(t);
      }
      return e;
    };

    var beginIntro = function (s, m) {
      var kind = reducedMotion && s.intro !== 'none' ? 'fade' : s.intro;
      introState.kind = INTRO_DURATION[kind] ? kind : 'none';
      introState.running = introState.kind !== 'none';
      introState.done = !introState.running;
      introState.t = 0;
      if (introState.kind === 'spin') {
        var distance = m.loop * 1.6 + width;
        pos = goal + distance;
        vel = -distance * 3;
        mode = 'spring';
      }
    };

    var updateCaptionUI = function (idx) {
      if (!settings.captions || !titleEl || !list[idx]) return;
      var cur = list[idx];
      titleEl.textContent = cur.title || cur.alt || ('Photo ' + (idx + 1));
      if (subtitleEl) subtitleEl.textContent = cur.subtitle || '';

      var num = String(idx + 1).padStart(2, '0');
      var tens = parseInt(num[0], 10);
      var ones = parseInt(num[1], 10);
      if (tensReel) tensReel.style.transform = 'translateY(' + (-tens * 10) + '%)';
      if (onesReel) onesReel.style.transform = 'translateY(' + (-ones * 10) + '%)';
    };

    var resize = function () {
      width = Math.max(1, container.clientWidth || container.offsetWidth || 1);
      height = Math.max(1, container.clientHeight || container.offsetHeight || 580);
      renderer.dpr = Math.min(window.devicePixelRatio || 1, 2, Math.sqrt(PIXEL_BUDGET / (width * height)));
      renderer.setSize(width, height);
      target.setSize(Math.max(2, Math.round(width * renderer.dpr)), Math.max(2, Math.round(height * renderer.dpr)));
      lensUniforms.tScene.value = target.texture;
      dirty = true;
      start();
    };

    var frame = function (now) {
      raf = 0;
      if (!alive) return;
      var s = settings;
      var dt = Math.min(0.05, Math.max(0.001, (now - last) / 1000));
      last = now;
      if (!s || !slots.length) {
        if (visible) raf = requestAnimationFrame(frame);
        return;
      }

      var m = metrics(s);
      var n = slots.length;
      var animating = false;

      if (resnap) {
        goal = snapPoint(m, goal);
        pos = goal;
        vel = 0;
        resnap = false;
      } else if (layout && layout.loop !== m.loop) {
        pos = remap(layout, m, pos);
        goal = remap(layout, m, goal);
        pointer.startPos = pos + (pointer.x - pointer.startX);
        animating = true;
      }
      layout = m;

      if (!introState.running && !introState.done) {
        var allSettled = slots.every(function (slot) { return slot.loaded || slot.failed; });
        if (allSettled || now - introState.readyAt > 3500) {
          goal = snapPoint(m, goal);
          pos = goal;
          beginIntro(s, m);
        }
      }
      if (introState.running) {
        introState.t = Math.min(1, introState.t + dt / (INTRO_DURATION[introState.kind] || 1));
        if (introState.t >= 1) {
          introState.running = false;
          introState.done = true;
        }
        animating = true;
      }

      if (mode === 'wheel' && now - wheelAt > 150) {
        goal = snapPoint(m, goal);
        mode = 'spring';
      }
      if (!pointer.dragging) {
        var spinning = introState.running && introState.kind === 'spin';
        var stiffness = spinning ? 9 : mode === 'wheel' ? 80 : 55;
        var damping = 2 * Math.sqrt(stiffness);
        var steps = Math.ceil(dt / (1 / 240));
        var h = dt / steps;
        for (var stp = 0; stp < steps; stp++) {
          var acc = stiffness * (goal - pos) - damping * vel;
          vel += acc * h;
          pos += vel * h;
        }
        if (Math.abs(goal - pos) < 0.05 && Math.abs(vel) < 0.5) {
          pos = goal;
          vel = 0;
        } else {
          animating = true;
        }
      } else {
        animating = true;
      }

      if (Math.abs(pos) > m.loop * 8) {
        var shift = Math.round(pos / m.loop) * m.loop;
        pos -= shift;
        goal -= shift;
        pointer.startPos -= shift;
      }

      var current = nearest(m, pos);
      if (current !== activeIndex) {
        activeIndex = current;
        updateCaptionUI(current);
        if (options.onChange) options.onChange(current, list[current]);
      }

      if (focus.pending >= 0 && mode === 'spring' && Math.abs(goal - pos) < 1.5 && Math.abs(vel) < 30) {
        if (current === focus.pending) openFocus(current);
        else focus.pending = -1;
      }

      if (
        s.autoplay &&
        !reducedMotion &&
        introState.done &&
        focus.target === 0 &&
        focus.t < 0.01 &&
        !pointer.over &&
        !pointer.down &&
        !hasFocus &&
        mode === 'spring' &&
        Math.abs(goal - pos) < 1 &&
        now - interactedAt > 3000 &&
        now - autoplayAt > s.interval * 1000
      ) {
        autoplayAt = now;
        step(m, 1);
      }
      if (s.autoplay && !reducedMotion) animating = true;

      var travel = Math.abs(pos - lastPos) / dt;
      lastPos = pos;
      var energyTarget = reducedMotion ? 0 : Math.min(travel / 2600, 1);
      energy += (energyTarget - energy) * (1 - Math.exp(-dt / (energyTarget > energy ? 0.07 : 0.35)));
      if (energy > 0.001) animating = true;
      var liquidAmount = reducedMotion ? 0 : s.liquid;
      var push = Math.max(-1, Math.min(1, vel / 2200));
      var deformStiffness = 120;
      var deformDamping = 2 * Math.sqrt(deformStiffness) * 0.32;
      deformVel += (deformStiffness * (push - deform) - deformDamping * deformVel) * dt;
      deform += deformVel * dt;
      if (Math.abs(deform) > 0.0005 || Math.abs(deformVel) > 0.005) animating = true;

      var focusStiffness = 64;
      focus.v += (focusStiffness * (focus.target - focus.t) - 2 * Math.sqrt(focusStiffness) * focus.v) * dt;
      focus.t += focus.v * dt;
      if (Math.abs(focus.target - focus.t) < 0.0005 && Math.abs(focus.v) < 0.001) {
        focus.t = focus.target;
        focus.v = 0;
      } else {
        animating = true;
      }
      var focusAmount = clamp01(focus.t);
      var focusEase = easeInOut(focusAmount);
      var focusW = focus.index >= 0 && focus.index < n ? m.widths[focus.index] : m.cardH;
      var focusScale = Math.max(1, Math.min(1.3, (height * 0.84) / m.cardH, (width * 0.92) / focusW));
      var nextLift = 1 + (focusScale - 1) * focusEase;
      if (Math.abs(nextLift - lift) > 0.0005) {
        lift = nextLift;
        container.style.setProperty('--flex-carousel-lift', lift.toFixed(4));
      }

      var effects = introEffects();

      var homeX = width / 2;
      var homeY = height / 2;
      var follow = s.followCursor && pointer.over && !pointer.dragging && !pointer.touch && focus.target === 0;
      var aimX = follow ? pointer.x : homeX;
      var aimY = follow ? pointer.y : homeY;
      if (!lens.ready) {
        lens.x = homeX;
        lens.y = homeY;
        lens.ready = true;
      }
      var lensK = 110;
      var lensC = 2 * Math.sqrt(lensK) * 0.8;
      lens.vx += (lensK * (aimX - lens.x) - lensC * lens.vx) * dt;
      lens.vy += (lensK * (aimY - lens.y) - lensC * lens.vy) * dt;
      lens.x += lens.vx * dt;
      lens.y += lens.vy * dt;
      if (Math.abs(aimX - lens.x) + Math.abs(aimY - lens.y) > 0.2 || Math.abs(lens.vx) + Math.abs(lens.vy) > 0.5)
        animating = true;

      var cardH = m.cardH;
      var halfW = (s.lensWidth * width) / 2;
      var halfH = (s.lensHeight * width) / 2;
      var squash = Math.abs(deform) * liquidAmount;
      halfW *= 1 + squash * 0.16;
      halfH *= 1 - squash * 0.08;
      var lensX = lens.x - deform * 14 * liquidAmount;

      for (var i = 0; i < n; i++) {
        var slot = slots[i];
        if (slot.loaded && slot.ready < 1) {
          slot.ready = Math.min(1, slot.ready + dt / 0.45);
          animating = true;
        }
      }

      var waiting = !introState.done;
      if (dirty || animating || pointer.dragging) {
        dirty = false;
        instances = [];
        var dpr = renderer.dpr;
        cardProgram.uniforms.uResolution.value = [width, height];
        cardProgram.uniforms.uDpr.value = dpr;
        cardProgram.uniforms.uRadius.value = s.radius;
        var shrink = 1 - clamp01(s.squeeze) * energy;
        var draws = [];
        for (var ci = 0; ci < n; ci++) {
          var w = m.widths[ci];
          var baseRel = wrap(m.centers[ci] - pos, m.loop);
          for (var k = -3; k <= 3; k++) {
            var rel = baseRel + k * m.loop;
            if (Math.abs(rel) - w / 2 > width + 40) continue;
            var fx = effects.card ? effects.card(rel) : null;
            var x = homeX + rel + (fx ? fx.x : 0);
            var scale = shrink * (fx ? fx.scale : 1);
            var alpha = fx ? fx.alpha : 1;
            if (focusAmount > 0) {
              if (ci === focus.index && Math.abs(rel) < w) {
                scale *= 1 + (focusScale - 1) * focusEase;
              } else {
                var order = Math.min(Math.abs(rel) / width, 1) * 0.25;
                var part = easeInOut(focusAmount * 1.25 - order);
                x += Math.sign(rel) * part * width * 0.7;
                alpha *= 1 - part;
              }
            }
            var cw = w * scale;
            if (alpha <= 0.001 || x + cw / 2 < -40 || x - cw / 2 > width + 40) continue;
            draws.push({ i: ci, rel: rel, x: x, y: homeY + (fx ? fx.y : 0), cw: cw, ch: cardH * scale, alpha: alpha });
          }
        }
        draws.sort(function (a, b) { return Math.abs(b.rel) - Math.abs(a.rel); });
        var first = true;
        for (var di = 0; di < draws.length; di++) {
          var draw = draws[di];
          var dslot = slots[draw.i];
          cardProgram.uniforms.tMap.value = dslot.texture;
          cardProgram.uniforms.uRect.value = [draw.x, draw.y, draw.cw + 2, draw.ch + 2];
          cardProgram.uniforms.uSize.value = [draw.cw, draw.ch];
          cardProgram.uniforms.uImage.value = dslot.image;
          cardProgram.uniforms.uAlpha.value = draw.alpha;
          cardProgram.uniforms.uReady.value = dslot.ready;
          cardProgram.uniforms.uShift.value = reducedMotion ? 0 : Math.max(-1, Math.min(1, draw.rel / (width * 0.75)));
          cardProgram.uniforms.uPlaceholder.value = dslot.color;
          renderer.render({ scene: cardMesh, target: target, clear: first });
          first = false;
          instances.push({
            index: draw.i,
            x0: draw.x - draw.cw / 2,
            x1: draw.x + draw.cw / 2,
            y0: draw.y - draw.ch / 2,
            y1: draw.y + draw.ch / 2
          });
        }
        if (first) {
          renderer.bindFramebuffer(target);
          gl.viewport(0, 0, target.width, target.height);
          gl.clear(gl.COLOR_BUFFER_BIT);
        }
        renderer.bindFramebuffer();
        target.texture.bind();
        gl.generateMipmap(gl.TEXTURE_2D);

        lensUniforms.uResolution.value = [width, height];
        lensUniforms.uDpr.value = dpr;
        lensUniforms.uCenter.value = [lensX, lens.y];
        lensUniforms.uHalf.value = [Math.max(halfW, 1), Math.max(halfH, 1)];
        lensUniforms.uAngle.value = (s.tilt * Math.PI) / 180;
        lensUniforms.uExponent.value = 2 + Math.pow(1 - clamp01(s.roundness), 1.5) * 10;
        var spanW = Math.max(halfW, 1);
        var spanH = Math.max(halfH, 1);
        var inner = Math.max(4, s.reach * (spanW + spanH) * 0.5);
        lensUniforms.uInner.value = inner;
        lensUniforms.uOuter.value = inner * 1.6;
        lensUniforms.uFlow.value = s.bend * (spanW + spanH) * 0.45;
        lensUniforms.uCurl.value = s.curl === 'rise' ? 1 : s.curl === 'fall' ? -1 : 0;
        lensUniforms.uDispersion.value = s.dispersion * 0.12 * (1 + Math.abs(deform) * liquidAmount * 1.2);
        lensUniforms.uStrength.value = effects.strength * (1 - focusEase);
        lensUniforms.uSceneAlpha.value = effects.sceneAlpha;
        renderer.render({ scene: lensMesh });
      }

      var nextHover = '';
      if (pointer.over && !pointer.dragging && introState.done && s.focusOnClick) {
        var hit = instances.find(function (inst) {
          return pointer.x >= inst.x0 && pointer.x <= inst.x1 && pointer.y >= inst.y0 && pointer.y <= inst.y1;
        });
        if (focus.target > 0) nextHover = 'close';
        else if (hit) nextHover = 'open';
      }
      if (nextHover !== hover) {
        hover = nextHover;
        if (hover) container.setAttribute('data-hover', hover);
        else container.removeAttribute('data-hover');
      }

      if (visible && (animating || waiting || dirty || pointer.down)) raf = requestAnimationFrame(frame);
    };

    var start = function () {
      if (raf || !visible || !alive) return;
      last = performance.now();
      raf = requestAnimationFrame(frame);
    };

    var localPoint = function (e) {
      var rect = container.getBoundingClientRect();
      return [e.clientX - rect.left, e.clientY - rect.top];
    };

    var onPointerDown = function (e) {
      if (e.button !== undefined && e.button > 0) return;
      skipIntro();
      var pt = localPoint(e);
      pointer.down = true;
      pointer.id = e.pointerId;
      pointer.touch = e.pointerType === 'touch';
      pointer.startX = pt[0];
      pointer.startY = pt[1];
      pointer.x = pt[0];
      pointer.y = pt[1];
      pointer.startPos = pos;
      pointer.dragging = false;
      pointer.samples = [{ x: pt[0], t: performance.now() }];
      interactedAt = performance.now();
      if (Math.abs(vel) > 40) {
        goal = pos;
        vel = 0;
      }
      dirty = true;
      start();
    };

    var onPointerMove = function (e) {
      var pt = localPoint(e);
      var x = pt[0];
      var y = pt[1];
      pointer.x = x;
      pointer.y = y;
      pointer.over = true;
      if (pointer.down && e.pointerId === pointer.id) {
        var dx = x - pointer.startX;
        var dy = y - pointer.startY;
        var slop = pointer.touch ? 10 : 5;
        if (!pointer.dragging) {
          if (pointer.touch && Math.abs(dy) > slop && Math.abs(dy) > Math.abs(dx)) {
            pointer.down = false;
            return;
          }
          if (Math.abs(dx) > slop) {
            pointer.dragging = true;
            pointer.startX = x;
            pointer.startPos = pos;
            closeFocus();
            try { container.setPointerCapture(e.pointerId); } catch (err) {}
            container.setAttribute('data-dragging', '');
          }
        }
        if (pointer.dragging) {
          pos = pointer.startPos - (x - pointer.startX);
          goal = pos;
          vel = 0;
          var now = performance.now();
          pointer.samples.push({ x: x, t: now });
          while (pointer.samples.length > 2 && now - pointer.samples[0].t > 100) pointer.samples.shift();
        }
      }
      dirty = true;
      start();
    };

    var onPointerUp = function (e) {
      if (!pointer.down || e.pointerId !== pointer.id) return;
      pointer.down = false;
      container.removeAttribute('data-dragging');
      var s = settings;
      if (!s) return;
      var m = metrics(s);
      interactedAt = performance.now();
      if (pointer.dragging) {
        pointer.dragging = false;
        var now = performance.now();
        var first = pointer.samples[0];
        var lastSample = pointer.samples[pointer.samples.length - 1];
        var velocity = 0;
        if (first && lastSample && lastSample.t > first.t && now - lastSample.t < 70) {
          velocity = -((lastSample.x - first.x) / (lastSample.t - first.t)) * 1000;
        }
        vel = velocity;
        var landing = snapPoint(m, pos + velocity * 0.32);
        goal = landing;
        if (Math.abs(velocity) > 400 && Math.abs(landing - pos) < 1) step(m, velocity > 0 ? 1 : -1);
        mode = 'spring';
        start();
        return;
      }
      if (closeFocus()) return;
      var pt = localPoint(e);
      var hit = instances.find(function (inst) {
        return pt[0] >= inst.x0 && pt[0] <= inst.x1 && pt[1] >= inst.y0 && pt[1] <= inst.y1;
      });
      if (!hit) return;
      if (hit.index === activeIndex && Math.abs(goal - pos) < 2) {
        if (options.onSelect) options.onSelect(hit.index, list[hit.index]);
        if (s.focusOnClick) openFocus(hit.index);
      } else {
        var rel = (hit.x0 + hit.x1) / 2 - width / 2;
        goal = snapPoint(m, pos + rel);
        mode = 'spring';
        if (s.focusOnClick) focus.pending = hit.index;
        start();
      }
    };

    var onPointerLeave = function () {
      pointer.over = false;
      dirty = true;
      start();
    };

    var onPointerCancel = function () {
      pointer.down = false;
      pointer.dragging = false;
      container.removeAttribute('data-dragging');
      var s = settings;
      if (!s) return;
      goal = snapPoint(metrics(s), pos);
      mode = 'spring';
      start();
    };

    var onWheel = function (e) {
      var s = settings;
      if (!s || e.ctrlKey) return;
      var dx = e.deltaX;
      var dy = e.deltaY;
      if (e.shiftKey && Math.abs(dx) < Math.abs(dy)) {
        dx = dy;
        dy = 0;
      }
      var unit = e.deltaMode === 1 ? 16 : e.deltaMode === 2 ? height : 1;
      var horizontal = Math.abs(dx) > Math.abs(dy);
      if (!horizontal && !s.captureWheel) return;
      e.preventDefault();
      skipIntro();
      interactedAt = performance.now();
      if (closeFocus()) return;
      var delta = Math.max(-120, Math.min(120, (horizontal ? dx : dy) * unit));
      goal += delta * 1.25;
      mode = 'wheel';
      wheelAt = performance.now();
      start();
    };

    var onKeyDown = function (e) {
      var s = settings;
      if (!s) return;
      var m = metrics(s);
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        skipIntro();
        closeFocus();
        interactedAt = performance.now();
        step(m, 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        skipIntro();
        closeFocus();
        interactedAt = performance.now();
        step(m, -1);
      } else if (e.key === 'Home') {
        e.preventDefault();
        closeFocus();
        goTo(m, 0);
      } else if (e.key === 'End') {
        e.preventDefault();
        closeFocus();
        goTo(m, slots.length - 1);
      } else if (e.key === 'Escape') {
        if (closeFocus()) e.preventDefault();
      } else if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        if (closeFocus() || activeIndex < 0) return;
        if (options.onSelect) options.onSelect(activeIndex, list[activeIndex]);
        if (s.focusOnClick) openFocus(activeIndex);
      }
    };

    container.addEventListener('pointerdown', onPointerDown);
    container.addEventListener('pointermove', onPointerMove);
    container.addEventListener('pointerup', onPointerUp);
    container.addEventListener('pointerleave', onPointerLeave);
    container.addEventListener('pointercancel', onPointerCancel);
    container.addEventListener('wheel', onWheel, { passive: false });
    container.addEventListener('keydown', onKeyDown);

    var resizeObserver = new ResizeObserver(resize);
    resizeObserver.observe(container);

    var intersectionObserver = new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible) start();
    });
    intersectionObserver.observe(container);

    resize();
    setItems(list);

    function setPreset(name) {
      var p = BEND_PRESETS[name];
      if (!p) return;
      Object.assign(settings, p);
      dirty = true;
      start();
    }

    return {
      setPreset: setPreset,
      setItems: setItems,
      step: function (delta) { if (layout) step(layout, delta); },
      goTo: function (idx) { if (layout) goTo(layout, idx); },
      resize: resize,
      wake: function () { dirty = true; start(); },
      destroy: function () {
        alive = false;
        visible = false;
        cancelAnimationFrame(raf);
        resizeObserver.disconnect();
        intersectionObserver.disconnect();
        container.removeEventListener('pointerdown', onPointerDown);
        container.removeEventListener('pointermove', onPointerMove);
        container.removeEventListener('pointerup', onPointerUp);
        container.removeEventListener('pointerleave', onPointerLeave);
        container.removeEventListener('pointercancel', onPointerCancel);
        container.removeEventListener('wheel', onWheel);
        container.removeEventListener('keydown', onKeyDown);
        slots.forEach(function (slot) { slot.dispose(); });
        slots = [];
        try { gl.getExtension('WEBGL_lose_context')?.loseContext(); } catch (err) {}
        if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
        if (captionEl && captionEl.parentNode) captionEl.parentNode.removeChild(captionEl);
      }
    };
  }

  global.initFlexCarousel = initFlexCarousel;

})(typeof window !== 'undefined' ? window : this);
