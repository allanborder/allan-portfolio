/**
 * React Bits: Lanyard Component
 * Physical editorial ID credential with spring-rope pendulum mechanics.
 * Monochrome, tactile, restrained.
 */
(function (global) {
  'use strict';

  function initLanyard(container) {
    if (container._lanyardInitialized) return;
    container._lanyardInitialized = true;

    var badge = container.querySelector('.lanyard-badge');
    var strap = container.querySelector('.lanyard-strap');
    if (!badge) return;

    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) {
      badge.style.transform = 'translate3d(0, 0, 0) rotate(0deg)';
      return;
    }

    // Physics parameters
    var angle = 0;          // radians
    var angularVel = 0;     // rad/s
    var targetAngle = 0;
    var isDragging = false;
    var dragStartX = 0;
    var dragStartY = 0;
    var currentX = 0;
    var currentY = 0;
    var lastTime = performance.now();

    var gravity = 9.8;
    var length = 1.8;       // meters equivalent
    var damping = 0.965;    // angular friction
    var springK = 6.0;

    function updatePhysics(now) {
      var dt = Math.min((now - lastTime) / 1000, 0.05); // cap delta
      lastTime = now;

      if (!isDragging) {
        // Idle gentle breathing sway
        var idleSway = Math.sin(now * 0.0014) * 0.025; // ~1.5 deg
        var restoring = -springK * (angle - idleSway);
        var accel = restoring - (gravity / length) * Math.sin(angle);
        angularVel += accel * dt;
        angularVel *= damping;
        angle += angularVel * dt;

        // Smooth return for X/Y offsets
        currentX += (0 - currentX) * 0.1;
        currentY += (0 - currentY) * 0.1;
      }

      var deg = angle * (180 / Math.PI);
      badge.style.transform = 'translate3d(' + currentX.toFixed(2) + 'px, ' + currentY.toFixed(2) + 'px, 0) rotate(' + deg.toFixed(2) + 'deg)';

      if (strap) {
        strap.style.transform = 'translate3d(' + (currentX * 0.4).toFixed(2) + 'px, 0, 0) rotate(' + (deg * 0.45).toFixed(2) + 'deg)';
      }

      requestAnimationFrame(updatePhysics);
    }

    // Pointer events for interaction
    function onPointerDown(e) {
      isDragging = true;
      dragStartX = e.clientX - currentX;
      dragStartY = e.clientY - currentY;
      badge.classList.add('is-held');
      window.addEventListener('pointermove', onPointerMove);
      window.addEventListener('pointerup', onPointerUp);
      window.addEventListener('pointercancel', onPointerUp);
    }

    function onPointerMove(e) {
      if (!isDragging) return;
      var newX = e.clientX - dragStartX;
      var newY = e.clientY - dragStartY;

      // Bound drag displacement
      currentX = Math.max(-60, Math.min(60, newX));
      currentY = Math.max(-20, Math.min(50, newY));

      // Angle follows horizontal drag
      angle = (currentX / 140);
    }

    function onPointerUp() {
      if (!isDragging) return;
      isDragging = false;
      badge.classList.remove('is-held');
      angularVel = (currentX / 20); // give kick velocity upon release
      window.removeEventListener('pointermove', onPointerMove);
      window.removeEventListener('pointerup', onPointerUp);
      window.removeEventListener('pointercancel', onPointerUp);
    }

    // Hover impulse on desktop
    container.addEventListener('mousemove', function (e) {
      if (isDragging) return;
      var rect = container.getBoundingClientRect();
      var relX = (e.clientX - (rect.left + rect.width / 2)) / (rect.width / 2);
      angularVel += relX * 0.08;
    });

    badge.addEventListener('pointerdown', onPointerDown);

    requestAnimationFrame(updatePhysics);
  }

  function initAll() {
    var containers = document.querySelectorAll('.lanyard-container');
    for (var i = 0; i < containers.length; i++) {
      initLanyard(containers[i]);
    }
  }

  global.Lanyard = {
    init: initAll,
    initElement: initLanyard
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})(window);
