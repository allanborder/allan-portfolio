/**
 * React Bits: FlipCard Component
 * Editorial 3D tactile card with subtle lerped tilt, specular glare, and keyboard accessibility.
 */
(function (global) {
  'use strict';

  function initCard(card) {
    if (card._flipCardInitialized) return;
    card._flipCardInitialized = true;

    var inner = card.querySelector('.flip-card__inner');
    if (!inner) return;

    var glare = card.querySelector('.flip-card__glare');
    if (!glare) {
      glare = document.createElement('div');
      glare.className = 'flip-card__glare';
      inner.appendChild(glare);
    }

    var isFlipped = false;
    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function toggleFlip(e) {
      // Don't flip if user clicked an action link/button inside back face
      if (e && e.target && (e.target.closest('a') || e.target.closest('.flip-card-action'))) {
        return;
      }
      isFlipped = !isFlipped;
      card.classList.toggle('is-flipped', isFlipped);
      card.setAttribute('aria-expanded', isFlipped ? 'true' : 'false');

      // Reset tilt upon flip with smooth animation
      inner.style.transition = 'transform 0.65s cubic-bezier(0.16, 1, 0.3, 1)';
      inner.style.transform = isFlipped ? 'rotateY(180deg)' : 'rotateY(0deg)';
      if (glare) glare.style.opacity = '0';

      setTimeout(function () {
        if (!isHovering) {
          inner.style.transition = '';
        }
      }, 650);
    }

    // Toggle on click
    card.addEventListener('click', toggleFlip);

    // Keyboard accessibility
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'region');
    card.setAttribute('aria-expanded', 'false');

    card.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        if (e.target.closest('a') || e.target.closest('.flip-card-action')) return;
        e.preventDefault();
        toggleFlip(e);
      }
    });

    var flipTriggers = card.querySelectorAll('.flip-toggle-btn');
    flipTriggers.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleFlip(e);
      });
    });

    // 3D subtle damped lerp mouse tilt & glare
    var isHovering = false;
    if (!prefersReduced) {
      var rect = null;
      var targetTiltX = 0;
      var targetTiltY = 0;
      var currentTiltX = 0;
      var currentTiltY = 0;
      var targetGlareX = 50;
      var targetGlareY = 50;
      var currentGlareX = 50;
      var currentGlareY = 50;
      var rafId = null;

      function renderLoop() {
        if (!isHovering && Math.abs(currentTiltX) < 0.05 && Math.abs(currentTiltY) < 0.05) {
          currentTiltX = 0;
          currentTiltY = 0;
          var baseRot = isFlipped ? 180 : 0;
          inner.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(' + baseRot + 'deg)';
          if (glare) glare.style.opacity = '0';
          rafId = null;
          return;
        }

        // Silky smooth lerp damping factor 0.12
        currentTiltX += (targetTiltX - currentTiltX) * 0.12;
        currentTiltY += (targetTiltY - currentTiltY) * 0.12;
        currentGlareX += (targetGlareX - currentGlareX) * 0.12;
        currentGlareY += (targetGlareY - currentGlareY) * 0.12;

        var baseRot = isFlipped ? 180 : 0;
        inner.style.transform = 'perspective(1000px) rotateX(' + currentTiltX.toFixed(2) + 'deg) rotateY(' + (baseRot + currentTiltY).toFixed(2) + 'deg)';

        if (glare) {
          glare.style.background = 'radial-gradient(circle at ' + currentGlareX.toFixed(1) + '% ' + currentGlareY.toFixed(1) + '%, rgba(255,255,255,0.08) 0%, transparent 65%)';
          glare.style.opacity = isHovering ? '1' : Math.max(0, (glare.style.opacity || 1) - 0.08).toString();
        }

        rafId = requestAnimationFrame(renderLoop);
      }

      function onMouseMove(e) {
        if (!rect) rect = card.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;

        targetTiltX = -y * 8; // subtle max 8deg
        targetTiltY = x * 8;
        targetGlareX = (x + 0.5) * 100;
        targetGlareY = (y + 0.5) * 100;

        if (!rafId) {
          rafId = requestAnimationFrame(renderLoop);
        }
      }

      function onMouseEnter() {
        isHovering = true;
        rect = card.getBoundingClientRect();
        inner.style.transition = 'none'; // smooth continuous tracking
        if (!rafId) {
          rafId = requestAnimationFrame(renderLoop);
        }
      }

      function onMouseLeave() {
        isHovering = false;
        rect = null;
        targetTiltX = 0;
        targetTiltY = 0;
        if (!rafId) {
          rafId = requestAnimationFrame(renderLoop);
        }
      }

      card.addEventListener('mouseenter', onMouseEnter);
      card.addEventListener('mousemove', onMouseMove);
      card.addEventListener('mouseleave', onMouseLeave);
    }
  }

  function initAll() {
    var cards = document.querySelectorAll('.flip-card');
    for (var i = 0; i < cards.length; i++) {
      initCard(cards[i]);
    }
  }

  global.FlipCard = {
    init: initAll,
    initCard: initCard
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})(window);
