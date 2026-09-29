# 2D LEGO Character Iridescent Dither & Liquid Scan Effect

GPU-accelerated 2D WebGL fragment shader effect for the 2D LEGO character.

## Core Features
1. **High-Contrast Monochrome Digital Halftone Base**:
   - 4x4 Bayer ordered dither matrix.
   - Near-white / light pixels, deep black areas, crisp halftone dots.
   - Consistent dither scale across desktop, tablet, and mobile.
2. **Organic Iridescent Liquid Scan Sweep**:
   - Periodic 4.8s seamless loop: top -> middle -> lower body -> off-screen fade out -> rest in monochrome.
   - Fluid contour mask modulated by procedural multi-octave noise (`fbm`).
   - Pure editorial spectrum: cyan, mint/green, violet, magenta, pink, orange, subtle blue.
3. **Subtle Liquid / Refraction Distortion**:
   - Organic UV displacement (`0.005–0.02`) localized to the sweep region.
4. **Chromatic Aberration**:
   - Subtle RGB channel separation inside the strongest portion of the wave.
5. **Dither + Color Coexistence**:
   - Dark pixels retain deep black, bright pixels shine with iridescent refraction, midtones transition through dither dots.
6. **Edge Protection & 2D Integrity**:
   - 100% alpha transparency preserved from original PNG.
   - No 3D conversion, no 3D rotation, no perspective distortion.
   - Subtle 2D mouse parallax (±4px) and smooth hover amplification.
7. **Accessibility & Graceful Fallback**:
   - Respects `prefers-reduced-motion: reduce`.
   - Fallback to the original 2D image if WebGL is unavailable.

## Configuration Parameters (`LEGO_EFFECT_CONFIG`)
```javascript
window.LEGO_EFFECT_CONFIG = {
  cycleDuration: 4.8,         // Seconds per complete loop (default ~4.8s)
  sweepWidth: 0.28,           // ~28% of character height
  distortionStrength: 0.014,  // Subtle organic liquid UV displacement
  chromaticStrength: 0.005,   // Subtle RGB channel separation inside sweep
  ditherScale: 1.0,           // Dither dot resolution scale
  hoverStrength: 1.0,         // Hover amplification
  parallaxStrength: 4.0,      // Max 2D parallax in pixels (±4px)
  mobileDprCap: 1.5           // Max DPR cap on mobile for 60fps
};
```
