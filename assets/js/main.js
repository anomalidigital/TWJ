/* Tanuwijaya & Partners — interactions
   Anomali Studio · vanilla JS, no dependencies */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. Header: transparent over hero, solid on scroll ---- */
  var header = document.querySelector('.header');
  var navRaf = 0;

  var solid = false;

  // The header only needs to know which side of the line the page is on; the
  // fade itself runs in CSS. The line is lower on the way back up (30 against
  // 65) so a scroll resting on it cannot flutter between the two states.
  function paintHeader() {
    navRaf = 0;
    if (!header) return;
    var y = window.scrollY;
    var next = solid ? y > 30 : y > 65;
    if (next === solid) return;
    solid = next;
    header.classList.toggle('is-solid', solid);
  }
  function onScroll() {
    if (!navRaf) navRaf = requestAnimationFrame(paintHeader);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  paintHeader();

  /* ---- 2. Mobile drawer ------------------------------------ */
  var burger = document.querySelector('.burger');
  var drawer = document.querySelector('.drawer');
  if (burger && drawer) {
    var links = drawer.querySelectorAll('nav a');
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      drawer.classList.toggle('is-open', !open);
      document.body.style.overflow = !open ? 'hidden' : '';
      var count = links.length;
      links.forEach(function (a, i) {
        // opening: cascade top-to-bottom; closing: reverse bottom-to-top
        a.style.transitionDelay = !open
          ? 100 + i * 40 + 'ms'
          : (count - 1 - i) * 25 + 'ms';
      });
    });
    links.forEach(function (a) {
      a.addEventListener('click', function () {
        burger.setAttribute('aria-expanded', 'false');
        drawer.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) burger.click();
    });
  }

  /* ---- 3. Scroll reveal ------------------------------------ */
  var revealables = document.querySelectorAll('[data-reveal]');
  if (reduce || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var winH = window.innerHeight || document.documentElement.clientHeight;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px 80px 0px', threshold: 0 });

    revealables.forEach(function (el) {
      var rect = el.getBoundingClientRect();
      var inView = rect.top < winH && rect.bottom > 0;
      var parent = el.parentElement;

      if (!inView && parent && !el.style.getPropertyValue('--d')) {
        var sibs = Array.prototype.slice.call(parent.children).filter(function (c) {
          return c.hasAttribute && c.hasAttribute('data-reveal');
        });
        if (sibs.length > 1) el.style.setProperty('--d', Math.min(sibs.indexOf(el), 6) * 45 + 'ms');
      }

      if (inView) {
        requestAnimationFrame(function () {
          el.classList.add('is-in');
        });
      } else {
        io.observe(el);
      }
    });
  }

  /* ---- 4. Accordion (home · partners) ---------------------- */
  /* CSS handles the panel's height; this only marks which row is open and
     shows that partner's portrait. */
  document.querySelectorAll('[data-accordion]').forEach(function (acc) {
    var buttons = acc.querySelectorAll('.acc__btn');

    function showFigure(btn) {
      var key = btn.getAttribute('data-figure');
      if (!key) return;
      var scope = acc.closest('[data-partners]') || document;
      scope.querySelectorAll('[data-figure-target]').forEach(function (node) {
        node.classList.toggle('is-active', node.getAttribute('data-figure-target') === key);
      });
    }

    var open = acc.querySelector('.acc__btn[aria-expanded="true"]');
    if (open) showFigure(open);

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        // one partner is always shown, so the portrait beside the list always
        // has an owner — clicking the open row keeps it open
        if (btn.getAttribute('aria-expanded') === 'true') return;
        buttons.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
        btn.setAttribute('aria-expanded', 'true');
        showFigure(btn);
      });
    });
  });

  /* ---- 5. Contact form → WhatsApp or e-mail ---------------- */
  var form = document.querySelector('[data-contact]');
  if (form) {
    var label = form.querySelector('[data-submit-label]');
    var radios = form.querySelectorAll('input[name="channel"]');
    function channel() {
      var picked = form.querySelector('input[name="channel"]:checked');
      return picked ? picked.value : 'whatsapp';
    }
    radios.forEach(function (r) {
      r.addEventListener('change', function () {
        if (label) label.textContent = channel() === 'email' ? 'Send Email' : 'Send Whatsapp Message';
      });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var name = ((d.get('first_name') || '') + ' ' + (d.get('last_name') || '')).trim();
      var lines = [
        'Name: ' + name,
        'Email: ' + (d.get('email') || ''),
        'Mobile: ' + (d.get('mobile') || ''),
        '',
        d.get('message') || ''
      ];
      if (channel() === 'email') {
        window.location.href = 'mailto:' + form.getAttribute('data-mail') +
          '?subject=' + encodeURIComponent('Consultation request — ' + (name || 'Website enquiry')) +
          '&body=' + encodeURIComponent(lines.join('\r\n'));
      } else {
        // noopener: the new tab gets no handle on this one, so it cannot
        // redirect it behind the visitor's back
        window.open(form.getAttribute('data-wa') + '?text=' + encodeURIComponent(lines.join('\n')),
          '_blank', 'noopener');
      }
    });
  }
})();
