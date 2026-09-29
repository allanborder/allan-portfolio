/**
 * LEGOCharacterEffect.js
 * 
 * GPU-Accelerated 2D Image Treatment:
 * High-Contrast Monochrome Bayer Dither + Iridescent Liquid Scan Sweep + Organic UV Refraction.
 * 
 * Preserves the 2D source character with 100% alpha transparency.
 * Zero 3D conversion. Zero DOM particles. Pure WebGL fragment shader.
 */

export const DEFAULT_LEGO_CONFIG = {
  cycleDuration: 4.8,         // Seconds per complete loop (default ~4.8s)
  sweepWidth: 0.28,           // ~28% of character height
  distortionStrength: 0.014,  // Subtle organic liquid UV displacement
  chromaticStrength: 0.005,   // Subtle RGB channel separation inside sweep
  ditherScale: 1.0,           // Dither dot resolution scale
  hoverStrength: 1.0,         // Hover amplification
  parallaxStrength: 4.0,      // Max 2D parallax in pixels (±4px)
  mobileDprCap: 1.5           // Max DPR cap on mobile
};

export class LEGOCharacterEffect {
  constructor(canvas, imageSrc, config = {}) {
    this.canvas = canvas;
    this.imageSrc = imageSrc;
    this.config = Object.assign({}, DEFAULT_LEGO_CONFIG, config);

    this.gl = null;
    this.program = null;
    this.texture = null;
    this.textureLoaded = false;
    this.textureSize = { width: 769, height: 1024 };

    this.animId = null;
    this.startTime = performance.now();
    this.lastTime = this.startTime;

    this.mouseTarget = { x: 0, y: 0 };
    this.mouseCurrent = { x: 0, y: 0 };
    this.hoverTarget = 0.0;
    this.hoverCurrent = 0.0;

    this.isReducedMotion = false;
    this.isDestroyed = false;

    this.init();
  }

  init() {
    if (!this.canvas) return;

    // Check prefers-reduced-motion
    if (typeof window !== 'undefined' && window.matchMedia) {
      const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      this.isReducedMotion = mediaQuery.matches;
      mediaQuery.addEventListener('change', (e) => {
        this.isReducedMotion = e.matches;
      });
    }

    // Initialize WebGL context
    const glOpts = {
      alpha: true,
      antialias: true,
      premultipliedAlpha: true,
      preserveDrawingBuffer: false
    };

    this.gl = this.canvas.getContext('webgl', glOpts) || this.canvas.getContext('experimental-webgl', glOpts);
    if (!this.gl) {
      console.warn('[LEGOCharacterEffect] WebGL not supported, using fallback.');
      return;
    }

    const gl = this.gl;
    gl.disable(gl.DEPTH_TEST);
    gl.enable(gl.BLEND);
    gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);

    // Compile Shaders
    const vsSource = `
      attribute vec2 a_position;
      varying vec2 v_uv;
      void main() {
        v_uv = (a_position + 1.0) * 0.5;
        v_uv.y = 1.0 - v_uv.y;
        gl_Position = vec4(a_position, 0.0, 1.0);
      }
    `;

    const fsSource = `
      precision highp float;
      varying vec2 v_uv;

      uniform sampler2D u_texture;
      uniform float u_time;
      uniform vec2 u_resolution;
      uniform vec2 u_textureResolution;
      uniform vec2 u_mouse;
      uniform float u_hover;
      uniform float u_cycleDuration;
      uniform float u_sweepWidth;
      uniform float u_distortionStrength;
      uniform float u_chromaticStrength;
      uniform float u_ditherScale;
      uniform float u_reducedMotion;

      float hash(vec2 p) {
        p = 50.0 * fract(p * 0.3183099 + vec2(0.71, 0.113));
        return -1.0 + 2.0 * fract(p.x * p.y * (p.x + p.y));
      }

      float noise(vec2 p) {
        vec2 i = floor(p);
        vec2 f = fract(p);
        vec2 u = f * f * (3.0 - 2.0 * f);
        return mix(
          mix(hash(i + vec2(0.0, 0.0)), hash(i + vec2(1.0, 0.0)), u.x),
          mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x),
          u.y
        );
      }

      float fbm(vec2 p) {
        float v = 0.0;
        v += 0.5000 * noise(p); p *= 2.02;
        v += 0.2500 * noise(p); p *= 2.03;
        v += 0.1250 * noise(p);
        return v;
      }

      float getBayer4(vec2 p) {
        vec2 f = mod(floor(p), 4.0);
        int x = int(f.x);
        int y = int(f.y);
        if (y == 0) {
          if (x == 0) return 0.0 / 16.0;
          if (x == 1) return 8.0 / 16.0;
          if (x == 2) return 2.0 / 16.0;
          return 10.0 / 16.0;
        } else if (y == 1) {
          if (x == 0) return 12.0 / 16.0;
          if (x == 1) return 4.0 / 16.0;
          if (x == 2) return 14.0 / 16.0;
          return 6.0 / 16.0;
        } else if (y == 2) {
          if (x == 0) return 3.0 / 16.0;
          if (x == 1) return 11.0 / 16.0;
          if (x == 2) return 1.0 / 16.0;
          return 9.0 / 16.0;
        } else {
          if (x == 0) return 15.0 / 16.0;
          if (x == 1) return 7.0 / 16.0;
          if (x == 2) return 13.0 / 16.0;
          return 5.0 / 16.0;
        }
      }

      vec3 getIridescentColor(vec2 uv, float t) {
        float waveCoord = uv.y * 3.2 + uv.x * 1.8 + fbm(uv * 4.2 + t * 0.35) * 0.55 + t * 0.85;
        vec3 a = vec3(0.62, 0.60, 0.66);
        vec3 b = vec3(0.42, 0.40, 0.46);
        vec3 c = vec3(1.25, 1.05, 1.15);
        vec3 d = vec3(0.05, 0.35, 0.68);
        vec3 col = a + b * cos(6.28318 * (c * waveCoord + d));
        float shimmer = sin(uv.x * 14.0 - uv.y * 9.0 + t * 2.2) * 0.5 + 0.5;
        col = mix(col, vec3(col.g, col.b, col.r), shimmer * 0.25);
        return col;
      }

      void main() {
        float screenAspect = u_resolution.x / u_resolution.y;
        float texAspect = u_textureResolution.x / u_textureResolution.y;
        vec2 uv = v_uv;
        
        if (screenAspect > texAspect) {
          float s = screenAspect / texAspect;
          uv.x = (uv.x - 0.5) * s + 0.5;
        } else {
          float s = texAspect / screenAspect;
          uv.y = (uv.y - 0.5) * s + 0.5;
        }

        vec2 parallax = u_mouse * vec2(4.0 / u_resolution.x, 4.0 / u_resolution.y);
        uv -= parallax;

        if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
          gl_FragColor = vec4(0.0);
          return;
        }

        vec4 origTex = texture2D(u_texture, uv);
        if (origTex.a <= 0.02) {
          gl_FragColor = vec4(0.0);
          return;
        }

        float cycleTime = mod(u_time, u_cycleDuration);
        float cycleProgress = cycleTime / u_cycleDuration;
        float sweepProgress = clamp(cycleProgress / 0.78, 0.0, 1.0);
        float sweepY = mix(-0.25, 1.25, smoothstep(0.0, 1.0, sweepProgress));
        
        float sweepCoord = uv.y + 0.16 * (uv.x - 0.5);
        float fluidNoise = fbm(vec2(uv.x * 3.6, uv.y * 3.2 + u_time * 0.45)) * 0.09
                         + fbm(vec2(uv.x * 7.2 + u_time * 0.25, uv.y * 7.2)) * 0.035;
        
        float distToSweep = abs(sweepCoord - sweepY + fluidNoise);
        float sweepW = u_sweepWidth * (1.0 + 0.2 * u_hover);
        float sweepMask = 1.0 - smoothstep(0.0, sweepW, distToSweep);
        sweepMask = pow(clamp(sweepMask, 0.0, 1.0), 1.35);

        if (u_reducedMotion > 0.5) {
          sweepMask = 0.0;
        }

        vec2 liquidNoiseCoord = uv * 4.8 + vec2(u_time * 0.28, -u_time * 0.38);
        vec2 liquidDistort = vec2(
          fbm(liquidNoiseCoord + vec2(0.0, 1.7)),
          fbm(liquidNoiseCoord + vec2(3.4, 0.0))
        );
        float currentDistort = u_distortionStrength * (1.0 + 0.5 * u_hover) * sweepMask;
        vec2 distortedUV = uv + liquidDistort * currentDistort;

        float currentChroma = u_chromaticStrength * (1.0 + 0.6 * u_hover) * sweepMask;
        vec2 chromaOffset = vec2(currentChroma, currentChroma * 0.5);

        vec4 sampleR = texture2D(u_texture, distortedUV + chromaOffset);
        vec4 sampleG = texture2D(u_texture, distortedUV);
        vec4 sampleB = texture2D(u_texture, distortedUV - chromaOffset);
        vec4 baseSample = vec4(sampleR.r, sampleG.g, sampleB.b, sampleG.a);

        float finalAlpha = min(baseSample.a, origTex.a);
        if (finalAlpha <= 0.02) {
          gl_FragColor = vec4(0.0);
          return;
        }

        vec2 ditherCoord = (uv * u_textureResolution) / (2.0 * u_ditherScale);
        float ditherThresh = getBayer4(ditherCoord);

        float lum = dot(baseSample.rgb, vec3(0.299, 0.587, 0.114));
        float contrastLum = smoothstep(0.12, 0.88, lum);
        float ditherStep = step(ditherThresh, contrastLum);

        vec3 ditherWhite = vec3(0.96, 0.97, 0.98);
        vec3 ditherBlack = vec3(0.04, 0.04, 0.05);
        vec3 monoColor = mix(ditherBlack, ditherWhite, ditherStep);

        vec3 iridescentColor = getIridescentColor(distortedUV, u_time);
        vec3 litColor = mix(ditherBlack, iridescentColor, ditherStep);
        litColor += iridescentColor * 0.14 * smoothstep(0.2, 0.8, contrastLum) * (1.0 - ditherStep);
        litColor += vec3(0.08, 0.08, 0.10) * u_hover * ditherStep;

        vec3 finalRGB = mix(monoColor, litColor, sweepMask);

        gl_FragColor = vec4(finalRGB * finalAlpha, finalAlpha);
      }
    `;

    const vs = this.compileShader(gl.VERTEX_SHADER, vsSource);
    const fs = this.compileShader(gl.FRAGMENT_SHADER, fsSource);
    if (!vs || !fs) return;

    this.program = gl.createProgram();
    gl.attachShader(this.program, vs);
    gl.attachShader(this.program, fs);
    gl.linkProgram(this.program);

    if (!gl.getProgramParameter(this.program, gl.LINK_STATUS)) {
      console.error('[LEGOCharacterEffect] Shader link error:', gl.getProgramInfoLog(this.program));
      return;
    }

    gl.useProgram(this.program);

    // Quad geometry buffer
    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    gl.bufferData(
      gl.ARRAY_BUFFER,
      new Float32Array([
        -1, -1,
         1, -1,
        -1,  1,
        -1,  1,
         1, -1,
         1,  1
      ]),
      gl.STATIC_DRAW
    );

    const aPosition = gl.getAttribLocation(this.program, 'a_position');
    gl.enableVertexAttribArray(aPosition);
    gl.vertexAttribPointer(aPosition, 2, gl.FLOAT, false, 0, 0);

    // Uniform locations cache
    this.uniforms = {
      u_texture: gl.getUniformLocation(this.program, 'u_texture'),
      u_time: gl.getUniformLocation(this.program, 'u_time'),
      u_resolution: gl.getUniformLocation(this.program, 'u_resolution'),
      u_textureResolution: gl.getUniformLocation(this.program, 'u_textureResolution'),
      u_mouse: gl.getUniformLocation(this.program, 'u_mouse'),
      u_hover: gl.getUniformLocation(this.program, 'u_hover'),
      u_cycleDuration: gl.getUniformLocation(this.program, 'u_cycleDuration'),
      u_sweepWidth: gl.getUniformLocation(this.program, 'u_sweepWidth'),
      u_distortionStrength: gl.getUniformLocation(this.program, 'u_distortionStrength'),
      u_chromaticStrength: gl.getUniformLocation(this.program, 'u_chromaticStrength'),
      u_ditherScale: gl.getUniformLocation(this.program, 'u_ditherScale'),
      u_reducedMotion: gl.getUniformLocation(this.program, 'u_reducedMotion')
    };

    // Load Image Texture
    this.loadTexture();

    // Listeners
    this.attachEvents();
    this.resize();

    // Start render loop
    this.render = this.render.bind(this);
    this.animId = requestAnimationFrame(this.render);
  }

  compileShader(type, source) {
    const gl = this.gl;
    const shader = gl.createShader(type);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      console.error('[LEGOCharacterEffect] Shader compile error:', gl.getShaderInfoLog(shader));
      gl.deleteShader(shader);
      return null;
    }
    return shader;
  }

  loadTexture() {
    const gl = this.gl;
    this.texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, this.texture);

    // 1x1 transparent placeholder
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, 1, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array([0, 0, 0, 0]));

    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.src = this.imageSrc;
    img.onload = () => {
      if (this.isDestroyed) return;
      this.textureSize.width = img.naturalWidth || 769;
      this.textureSize.height = img.naturalHeight || 1024;

      gl.bindTexture(gl.TEXTURE_2D, this.texture);
      gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);

      this.textureLoaded = true;
      if (this.onReady) this.onReady();
    };
  }

  attachEvents() {
    const stage = this.canvas.parentElement;
    if (!stage) return;

    this._onPointerMove = (e) => {
      const rect = stage.getBoundingClientRect();
      const px = ((e.clientX - rect.left) / rect.width) * 2.0 - 1.0;
      const py = ((e.clientY - rect.top) / rect.height) * 2.0 - 1.0;
      this.mouseTarget.x = Math.max(-1, Math.min(1, px));
      this.mouseTarget.y = Math.max(-1, Math.min(1, py));
      this.hoverTarget = 1.0;
    };

    this._onPointerEnter = () => {
      this.hoverTarget = 1.0;
    };

    this._onPointerLeave = () => {
      this.hoverTarget = 0.0;
      this.mouseTarget.x = 0;
      this.mouseTarget.y = 0;
    };

    stage.addEventListener('pointermove', this._onPointerMove, { passive: true });
    stage.addEventListener('pointerenter', this._onPointerEnter, { passive: true });
    stage.addEventListener('pointerleave', this._onPointerLeave, { passive: true });

    if (window.ResizeObserver) {
      this._ro = new ResizeObserver(() => this.resize());
      this._ro.observe(stage);
    }
    this._onResize = () => this.resize();
    window.addEventListener('resize', this._onResize, { passive: true });
  }

  resize() {
    if (!this.canvas || !this.gl) return;
    const stage = this.canvas.parentElement;
    if (!stage) return;

    const rect = stage.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return;

    const isMobile = window.innerWidth <= 768;
    const maxDpr = isMobile ? this.config.mobileDprCap : 2.0;
    const dpr = Math.min(window.devicePixelRatio || 1, maxDpr);

    const w = Math.floor(rect.width * dpr);
    const h = Math.floor(rect.height * dpr);

    if (this.canvas.width !== w || this.canvas.height !== h) {
      this.canvas.width = w;
      this.canvas.height = h;
      this.gl.viewport(0, 0, w, h);
    }
  }

  render(timestamp) {
    if (this.isDestroyed) return;

    const gl = this.gl;
    if (!gl || !this.program || !this.textureLoaded) {
      this.animId = requestAnimationFrame(this.render);
      return;
    }

    const elapsed = (timestamp - this.startTime) * 0.001;

    // Smooth lerping for hover and 2D parallax
    this.mouseCurrent.x += (this.mouseTarget.x - this.mouseCurrent.x) * 0.08;
    this.mouseCurrent.y += (this.mouseTarget.y - this.mouseCurrent.y) * 0.08;
    this.hoverCurrent += (this.hoverTarget - this.hoverCurrent) * 0.08;

    gl.clearColor(0.0, 0.0, 0.0, 0.0);
    gl.clear(gl.COLOR_BUFFER_BIT);

    gl.useProgram(this.program);

    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.texture);
    gl.uniform1i(this.uniforms.u_texture, 0);

    gl.uniform1f(this.uniforms.u_time, elapsed);
    gl.uniform2f(this.uniforms.u_resolution, this.canvas.width, this.canvas.height);
    gl.uniform2f(this.uniforms.u_textureResolution, this.textureSize.width, this.textureSize.height);
    gl.uniform2f(this.uniforms.u_mouse, this.mouseCurrent.x, this.mouseCurrent.y);
    gl.uniform1f(this.uniforms.u_hover, this.hoverCurrent);
    gl.uniform1f(this.uniforms.u_cycleDuration, this.config.cycleDuration);
    gl.uniform1f(this.uniforms.u_sweepWidth, this.config.sweepWidth);
    gl.uniform1f(this.uniforms.u_distortionStrength, this.config.distortionStrength);
    gl.uniform1f(this.uniforms.u_chromaticStrength, this.config.chromaticStrength);
    gl.uniform1f(this.uniforms.u_ditherScale, this.config.ditherScale);
    gl.uniform1f(this.uniforms.u_reducedMotion, this.isReducedMotion ? 1.0 : 0.0);

    gl.drawArrays(gl.TRIANGLES, 0, 6);

    this.animId = requestAnimationFrame(this.render);
  }

  destroy() {
    this.isDestroyed = true;
    if (this.animId) cancelAnimationFrame(this.animId);

    const stage = this.canvas.parentElement;
    if (stage) {
      stage.removeEventListener('pointermove', this._onPointerMove);
      stage.removeEventListener('pointerenter', this._onPointerEnter);
      stage.removeEventListener('pointerleave', this._onPointerLeave);
      if (this._ro) this._ro.disconnect();
    }
    window.removeEventListener('resize', this._onResize);

    if (this.gl && this.program) {
      this.gl.deleteProgram(this.program);
      if (this.texture) this.gl.deleteTexture(this.texture);
    }
  }
}
