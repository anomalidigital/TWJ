# -*- coding: utf-8 -*-
"""
Bundles the five static pages into ONE self-contained HTML preview
(all CSS/JS/images inlined, hash routing) for sharing as an Artifact.

    python _tools/bundle.py       (run from Baldy/web)
"""
import os, re, base64, mimetypes

import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUTFILE = os.path.join(HERE, "twj-preview.html")

ROUTES = [
    ("home", "index.html", build.page_home),
    ("about", "about.html", build.page_about),
    ("people", "our-people.html", build.page_people),
    ("services", "industries-services.html", build.page_industries),
    ("contact", "contact.html", build.page_contact),
]
HREF = {h: "#/" + k for k, h, _ in ROUTES}


def data_uri(rel):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    if path.endswith(".svg"):
        mime = "image/svg+xml"
    with open(path, "rb") as f:
        return "data:%s;base64,%s" % (mime, base64.b64encode(f.read()).decode())


CACHE = {}


def inline_assets(html):
    def sub(m):
        rel = m.group(1)
        if rel not in CACHE:
            CACHE[rel] = data_uri(rel)
        return 'src="%s"' % CACHE[rel]
    return re.sub(r'src="(assets/[^"]+)"', sub, html)


def rewrite_links(html):
    for page, target in HREF.items():
        html = html.replace('href="%s"' % page, 'href="%s"' % target)
    html = re.sub(r'\s+aria-current="page"', "", html)
    return html


def main():
    shell = rewrite_links(inline_assets(build.header("index.html")))
    foot = rewrite_links(inline_assets(build.footer()))
    foot = foot.replace('<script src="assets/js/main.js"></script>', "")
    foot = foot.replace("</body>\n</html>", "").strip()

    pages = []
    for key, _, fn in ROUTES:
        doc = fn()
        body = re.search(r'<main id="main">(.*?)</main>', doc, re.S).group(1)
        body = rewrite_links(inline_assets(body))
        pages.append('<div class="page" data-page="%s"%s>%s</div>' % (
            key, "" if key == "home" else " hidden", body))

    css = open(os.path.join(ROOT, "assets", "css", "style.css"), encoding="utf-8").read()
    css = css.split("/* ---------- 2. Reset")[0] + "/* ---------- 2. Reset" + \
        css.split("/* ---------- 2. Reset", 1)[1]
    js = open(os.path.join(ROOT, "assets", "js", "main.js"), encoding="utf-8").read()

    extra_css = """
/* ---------- preview shell (single-file artifact) ----------- */
#pages > .page[hidden] { display: none; }
#pages > .page { animation: pageIn .55s var(--ease) both; }
@keyframes pageIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@media (prefers-reduced-motion: reduce) { #pages > .page { animation: none; } }
"""

    router = """
(function () {
  var ROUTES = ['home', 'about', 'people', 'services', 'contact'];
  function current() {
    var k = (location.hash || '#/home').replace('#/', '').split('#')[0];
    return ROUTES.indexOf(k) > -1 ? k : 'home';
  }
  function paint() {
    var key = current();
    document.querySelectorAll('#pages > .page').forEach(function (p) {
      p.hidden = p.getAttribute('data-page') !== key;
    });
    document.querySelectorAll('a[href^="#/"]').forEach(function (a) {
      var on = a.getAttribute('href') === '#/' + key;
      if (on) { a.setAttribute('aria-current', 'page'); } else { a.removeAttribute('aria-current'); }
    });
    document.querySelectorAll('#pages > .page:not([hidden]) [data-reveal]').forEach(function (e) {
      if (e.getBoundingClientRect().top < window.innerHeight) e.classList.add('is-in');
    });
    window.scrollTo(0, 0);
    document.dispatchEvent(new CustomEvent('route'));
  }
  window.addEventListener('hashchange', paint);
  paint();
})();
"""

    html = """<title>Tanuwijaya &amp; Partners</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap">
<style>
%s
%s
</style>
%s
<div id="pages">
%s
</div>
%s
<script>
%s
%s
</script>
""" % (css, extra_css, shell, "\n".join(pages), foot, router, js)

    with open(OUTFILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %s  %.2f MB" % (OUTFILE, os.path.getsize(OUTFILE) / 1048576.0))


if __name__ == "__main__":
    main()
