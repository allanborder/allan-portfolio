/**
 * React Bits: TechText Component
 * Subtle, technical typography inspection with character resolution.
 * Built for high readability and editorial minimalism.
 */
(function (global) {
  'use strict';

  var GLYPHS = '01/_[]#*+<>~-';

  function scramble(el, targetText, duration, onComplete) {
    if (!el) return;
    var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) {
      el.textContent = targetText;
      if (onComplete) onComplete();
      return;
    }

    var originalChars = targetText.split('');
    var totalChars = originalChars.length;
    var startTime = performance.now();
    var animDuration = duration || Math.min(650, Math.max(250, totalChars * 22));

    function frame(now) {
      var elapsed = now - startTime;
      var progress = Math.min(1, elapsed / animDuration);
      var resolvedIndex = Math.floor(progress * totalChars);

      var output = '';
      for (var i = 0; i < totalChars; i++) {
        if (originalChars[i] === ' ' || originalChars[i] === '\n') {
          output += originalChars[i];
        } else if (i < resolvedIndex) {
          output += originalChars[i];
        } else if (i === resolvedIndex) {
          output += GLYPHS[Math.floor(Math.random() * GLYPHS.length)];
        } else {
          // Keep blank or subtle random glyph until reached
          output += Math.random() > 0.4 ? GLYPHS[Math.floor(Math.random() * GLYPHS.length)] : originalChars[i];
        }
      }

      el.textContent = output;

      if (progress < 1) {
        requestAnimationFrame(frame);
      } else {
        el.textContent = targetText;
        if (onComplete) onComplete();
      }
    }

    requestAnimationFrame(frame);
  }

  function initElement(el) {
    if (el._techTextInitialized) return;
    el._techTextInitialized = true;

    var rawText = el.getAttribute('data-tech-text') || el.textContent.trim();
    el.setAttribute('aria-label', rawText);
    el.classList.add('tech-text-ready');

    // Hover interaction: subtle re-scramble on pointer enter
    var isHovering = false;
    el.addEventListener('mouseenter', function () {
      if (isHovering) return;
      isHovering = true;
      scramble(el, rawText, 320, function () {
        isHovering = false;
      });
    });

    // Initial trigger when visible or manually invoked
    el.runScramble = function (dur) {
      scramble(el, rawText, dur);
    };
  }

  function initAll() {
    var nodes = document.querySelectorAll('[data-tech-text], .tech-text');
    for (var i = 0; i < nodes.length; i++) {
      initElement(nodes[i]);
    }
  }

  global.TechText = {
    init: initAll,
    initElement: initElement,
    scramble: scramble
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})(window);
