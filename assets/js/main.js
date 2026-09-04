/* Tanuwijaya & Partners — interactions
   Anomali Studio · vanilla JS, no dependencies */
(function () {
  'use strict';

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. Header: transparent over hero, solid on scroll ---- */
  var header = document.querySelector('.header');
  function onScroll() {
    if (!header) return;
    // transparent only while the page is at rest at the top; the moment it
    // moves the navy ground fades in, so the banner headline never runs
    // underneath a see-through bar
    header.classList.toggle('is-solid', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

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
      links.forEach(function (a, i) {
        a.style.transitionDelay = !open ? 120 + i * 55 + 'ms' : '0ms';
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
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    revealables.forEach(function (el, i) {
      var parent = el.parentElement;
      if (parent && !el.style.getPropertyValue('--d')) {
        var sibs = Array.prototype.slice.call(parent.children).filter(function (c) {
          return c.hasAttribute && c.hasAttribute('data-reveal');
        });
        if (sibs.length > 1) el.style.setProperty('--d', Math.min(sibs.indexOf(el), 6) * 90 + 'ms');
      }
      io.observe(el);
    });
  }

  /* ---- 4. Accordion (home · partners) ---------------------- */
  document.querySelectorAll('[data-accordion]').forEach(function (acc) {
    var buttons = acc.querySelectorAll('.acc__btn');
    function sync(btn) {
      var key = btn.getAttribute('data-figure');
      if (!key) return;
      var scope = acc.closest('[data-partners]') || document;
      scope.querySelectorAll('[data-figure-target]').forEach(function (node) {
        node.classList.toggle('is-active', node.getAttribute('data-figure-target') === key);
      });
    }
    function measure(panel) {
      panel.style.height = panel.firstElementChild.offsetHeight + 'px';
    }
    function remeasure() {
      buttons.forEach(function (b) {
        if (b.getAttribute('aria-expanded') === 'true') {
          var p = document.getElementById(b.getAttribute('aria-controls'));
          if (p) measure(p);
        }
      });
    }
    // the first measurement happens before the webfont lands, which reflows the
    // copy taller and clips it against overflow:hidden — so measure again after
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(remeasure);
    if ('ResizeObserver' in window) {
      var ro = new ResizeObserver(remeasure);
      acc.querySelectorAll('.acc__panel > div').forEach(function (c) { ro.observe(c); });
    }
    buttons.forEach(function (btn) {
      var panel = document.getElementById(btn.getAttribute('aria-controls'));
      if (!panel) return;
      if (btn.getAttribute('aria-expanded') === 'true') { measure(panel); sync(btn); }
      btn.addEventListener('click', function () {
        // one partner is always shown, so the portrait beside the list always
        // has an owner — clicking the open row keeps it open
        if (btn.getAttribute('aria-expanded') === 'true') return;
        buttons.forEach(function (b) {
          var p = document.getElementById(b.getAttribute('aria-controls'));
          b.setAttribute('aria-expanded', 'false');
          if (p) p.style.height = '0px';
        });
        btn.setAttribute('aria-expanded', 'true');
        measure(panel);
        sync(btn);
      });
    });
    window.addEventListener('resize', remeasure);
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
        window.open(form.getAttribute('data-wa') + '?text=' + encodeURIComponent(lines.join('\n')), '_blank');
      }
    });
  }
})();
