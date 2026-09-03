# -*- coding: utf-8 -*-
"""
Tanuwijaya & Partners — static site builder
Anomali Studio · 2026

Section-for-section reconstruction of the existing twj.co.id, rebuilt on the
new brand (navy / luster white, Noto Serif + Noto Sans). Copy is taken verbatim
from the live pages; nothing has been added.

    python _tools/build.py     (run from Baldy/web)
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, ".."))

NAV = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("our-people.html", "Our People"),
    ("industries-services.html", "Industries &amp; Services"),
    ("contact.html", "Contact"),
]
WA = "https://wa.me/628119112147"

# ---------------------------------------------------------------- icons
I = {
    "audit": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/><circle cx="11" cy="13.2" r="2.7"/><path d="m12.9 15.1 2.5 2.5"/>',
    "tax": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/><path d="m9.2 17.2 5.6-6.4"/><circle cx="9.6" cy="11.4" r="1.1"/><circle cx="14.4" cy="16.6" r="1.1"/>',
    "legal": '<path d="M12 3.4v16.8"/><path d="M7.6 20.2h8.8"/><path d="M4.4 7.6h15.2"/><path d="M4.4 7.6 2 14h4.8z"/><path d="M19.6 7.6 17.2 14H22z"/><path d="m8.4 5.7 3.6-1.5 3.6 1.5"/>',
    "other": '<rect x="3.8" y="4.6" width="6.6" height="6.6"/><rect x="13.6" y="4.6" width="6.6" height="6.6"/><rect x="3.8" y="12.8" width="6.6" height="6.6"/><rect x="13.6" y="12.8" width="6.6" height="6.6"/>',
    "private": '<path d="M12 3.1 19 5.7v5.6c0 4.2-2.9 7.7-7 9.6-4.1-1.9-7-5.4-7-9.6V5.7z"/><circle cx="12" cy="10.1" r="2.1"/><path d="M8.7 16.1c.6-1.7 1.8-2.6 3.3-2.6s2.7.9 3.3 2.6"/>',
    "maritime": '<circle cx="12" cy="4.6" r="1.9"/><path d="M12 6.5V21"/><path d="M8.3 9.4h7.4"/><path d="M3.6 13.9c0 4 3.8 7.1 8.4 7.1s8.4-3.1 8.4-7.1"/><path d="M3.6 13.9h2.6M20.4 13.9h-2.6"/>',
    "trade": '<path d="M3 8.6h13.4"/><path d="m12.8 5 3.6 3.6-3.6 3.6"/><path d="M21 15.4H7.6"/><path d="M11.2 11.8 7.6 15.4l3.6 3.6"/>',
    "plantation": '<path d="M12 21v-7.6"/><path d="M12 13.4C12 9.8 9.3 6.9 6 6.9c0 3.6 2.7 6.5 6 6.5z"/><path d="M12 13.4c0-3 2.2-5.5 5-5.5 0 3-2.2 5.5-5 5.5z"/><path d="M7.6 21h8.8"/>',
    "retail": '<path d="M4.4 10.2V20h15.2v-9.8"/><path d="M3 10.2 4.8 4.4h14.4L21 10.2z"/><path d="M9.6 20v-5.4h4.8V20"/><path d="M3 10.2h18"/>',
}
SOCIAL = {
    "facebook": '<path d="M13.4 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.25-1.5 1.55-1.5h1.65V3.6c-.29-.04-1.27-.12-2.41-.12-2.38 0-4.01 1.45-4.01 4.12v2.3H7.5V13h2.68v8z"/>',
    "instagram": '<path fill-rule="evenodd" d="M7.6 2h8.8A5.6 5.6 0 0 1 22 7.6v8.8a5.6 5.6 0 0 1-5.6 5.6H7.6A5.6 5.6 0 0 1 2 16.4V7.6A5.6 5.6 0 0 1 7.6 2zm0 2A3.6 3.6 0 0 0 4 7.6v8.8A3.6 3.6 0 0 0 7.6 20h8.8a3.6 3.6 0 0 0 3.6-3.6V7.6A3.6 3.6 0 0 0 16.4 4zM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm5.6-2.7a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2z"/>',
    "linkedin": '<path d="M5 3.4a2.1 2.1 0 1 1 0 4.2 2.1 2.1 0 0 1 0-4.2zM3.2 9.2h3.6V21H3.2zM9.2 9.2h3.45v1.6h.05c.48-.9 1.65-1.85 3.4-1.85 3.63 0 4.3 2.2 4.3 5.05V21h-3.6v-5.35c0-1.28-.02-2.92-1.8-2.92-1.8 0-2.08 1.39-2.08 2.83V21H9.2z"/>',
    "whatsapp": '<path d="M12.04 2C6.6 2 2.16 6.44 2.16 11.9c0 1.75.46 3.45 1.33 4.95L2 22l5.3-1.38a9.87 9.87 0 0 0 4.73 1.2c5.46 0 9.9-4.44 9.9-9.9 0-2.64-1.03-5.13-2.9-7A9.82 9.82 0 0 0 12.04 2zm0 1.8c2.16 0 4.2.85 5.73 2.38a8.06 8.06 0 0 1 2.37 5.73c0 4.47-3.63 8.1-8.1 8.1a8.1 8.1 0 0 1-4.13-1.13l-.3-.18-3.07.8.82-3-.2-.31a8.03 8.03 0 0 1-1.23-4.29c0-4.47 3.64-8.1 8.11-8.1zm-3.2 4.1c-.15 0-.4.06-.6.29-.21.23-.8.78-.8 1.9s.82 2.2.93 2.36c.11.15 1.6 2.44 3.88 3.42.54.23.96.37 1.29.48.54.17 1.04.15 1.43.09.44-.07 1.34-.55 1.53-1.08.19-.53.19-.99.13-1.08-.06-.09-.21-.15-.44-.26-.23-.11-1.34-.66-1.55-.74-.21-.08-.36-.11-.5.11-.15.23-.58.74-.71.89-.13.15-.26.17-.49.06-.23-.12-.96-.36-1.83-1.13-.68-.6-1.13-1.35-1.27-1.58-.13-.23-.01-.35.1-.47.1-.1.23-.26.34-.4.11-.13.15-.23.23-.38.08-.15.04-.29-.02-.4-.06-.12-.5-1.23-.7-1.68-.18-.44-.37-.38-.5-.39h-.43z"/>',
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % I[name])


def social(name):
    return '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % SOCIAL[name]


def btn(href, label, cls=""):
    return ('<a class="btn%s" href="%s"><span>%s</span>'
            '<span class="arrow" aria-hidden="true">&#8594;</span></a>'
            % ((" " + cls) if cls else "", href, label))


# ---------------------------------------------------------------- copy
FOUNDING = ("Founded in 1989 by Linda Purnomo and Alvin Arthur, our founders have served clients in all "
            "aspect of their business and maintain the relationship for over 30 years. In 2026, the firm "
            "is rebranded into Tanuwijaya &amp; Partners, where it will be the umbrella brand for our "
            "various services.")
FAMILY = ("We provide you with direct and expert legal care so that you can resolve issues early and "
          "amicably. Tanuwijaya &amp; Partners is one of the few corporate services company that are "
          "family owned. This ensures that clients receive long lasting commitment that can be passed "
          "through generations. The relationship is long-term.")
CLIENTS_TEXT = ("Trusted by private and corporate clients, industry leaders, including local and "
                "foreign-owned, state-owned and public listed companies, multinational enterprises, "
                "and international organizations")

PARTNERS = [
    ("linda", "Linda Purnomo", "assets/img/people/linda-purnomo.webp", "LP"),
    ("david", "David Tanuwijaya", "assets/img/people/david-tanuwijaya.webp", "DT"),
    ("chaterine", "Chaterine Tanuwijaya", "", "CT"),
]

TEAM_PARTNERS = [
    ("david-tanuwijaya", "David Tanuwijaya", "Partner", "david.tanuwijaya@kaptwj.com"),
    ("joanita-b-salim", "Joanita B. Salim", "Manager", "joanita.salim@kaptwj.com"),
    ("yenny-gunawan", "Yenny Gunawan", "Manager", "yenny.gunawan@kaptwj.com"),
    ("muhammad-wisnu", "Muhammad Wisnu", "Manager", "muhammad.wisnu@kaptwj.com"),
]
ASSOCIATES = [
    ("krisna-sandy", "Krisna Sandy", "Supervisor", "krisna.sandy@kaptwj.com"),
    ("yosua-amos", "Yosua Amos", "Senior Associate", "yosua.amos@kaptwj.com"),
    ("nur-layinah", "Nur Layinah", "Senior Associate", "nur.layinah@kaptwj.com"),
    ("vani-puspita", "Vani Puspita", "Supervisor", "vani.dwi@kaptwj.com"),
]
COMPANIES = [
    ("Kantor Akuntan Publik Tanuwijaya", "kaptwj.com", "https://kaptwj.com"),
    ("Kantor Konsultan Hukum Tanuwijaya", "twjlaw.id", "https://twjlaw.id"),
    ("PT Arthurindo Management Consultant", "arthurindo.com", "https://arthurindo.com"),
    ("PT Purnomo Jasa Korporatama / Purnomo Consult", "purnomo-consult.com", "https://purnomo-consult.com"),
    ("PT Aurora Mitra Sejahtera", "&ndash;", ""),
    ("Aurora Corporate Services Pte Ltd", "auroracorpservices.com", "https://auroracorpservices.com"),
]

SERVICES = [
    ("audit", "Audit", ["Fraud Audit", "Internal Audit"]),
    ("tax", "Tax", ["Advisory", "Tax Audit", "Tax Compliance", "Tax Structure", "Cross Border Tax"]),
    ("legal", "Legal", ["Incorporation", "Advisory", "Due Diligence", "Contract Drafting", "Compliance",
                        "Mergers Acquisition", "Liquidation", "Restructuring", "Family Law"]),
    ("other", "Other Services", ["Private Client Services", "Virtual &amp; Dedicated Office Space",
                                 "Immigration and Work Permit", "HR and Payroll Services"]),
]

INDUSTRIES = [
    ("private", "Private Client Services",
     "We serve private clients, high net-worth individuals (HNWI) and ultra-high net-worth individuals (UHNWI) both local and foreign in overseeing their tax compliance with the local regulations."),
    ("plantation", "Plantation",
     "Supporting plantation businesses with entity structuring, compliance, and investment facilitation to enhance sustainable growth and operational efficiency across agricultural sectors."),
    ("maritime", "Maritime",
     "Providing corporate advisory, ownership structuring, and compliance services for port, shipping, shipyard, and vessel operations to ensure smooth, globally compliant maritime ventures."),
    ("retail", "Retail",
     "Helping retail businesses expand with strategic structuring, franchise setup, and investment compliance for scalable, transparent, and adaptable growth in dynamic markets."),
    ("trade", "Import Export",
     "Assisting trading firms with corporate setup, trade licensing, and cross-border structuring to streamline operations, ensure compliance, and enhance global competitiveness."),
]

CLIENTS = [
    ("biofarma", "Bio Farma"), ("johnson-controls", "Johnson Controls"), ("goto", "GoTo"),
    ("generali", "Generali"), ("bill-and-melinda-gates-foundation", "Bill &amp; Melinda Gates Foundation"),
    ("waskita", "Waskita"), ("boskalis", "Boskalis"), ("japan-radio-co-ltd", "Japan Radio Co. Ltd"),
    ("crbc", "China Road and Bridge Corporation"), ("scg", "SCG"),
]
INSTITUTIONS = [
    ("iapi", "Institut Akuntan Publik Indonesia"), ("kemenkeu", "Kementerian Keuangan Republik Indonesia"),
    ("ojk", "Otoritas Jasa Keuangan"), ("caw", "Chartered Accountants Worldwide"),
    ("dbni", "Dutch Business Network Indonesia"),
]


# ---------------------------------------------------------------- shell
def head(title, desc):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s - Tanuwijaya &amp; Partners</title>
<meta name="description" content="%s">
<meta name="theme-color" content="#1F3A5F">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="%s - Tanuwijaya &amp; Partners">
<meta property="og:description" content="%s">
<meta property="og:image" content="assets/img/hero-home.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
""" % (title, desc, title, desc)


def header(page):
    links = "".join(
        '\n      <a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == page else "", label)
        for href, label in NAV)
    drawer_links = "".join(
        '\n      <a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == page else "", label)
        for href, label in NAV)
    return """
<header class="header">
  <div class="shell">
    <a class="brand" href="index.html" aria-label="Tanuwijaya &amp; Partners — home">
      <img class="logo-light" src="assets/logo/logo-light.svg" alt="Tanuwijaya &amp; Partners" width="720" height="144">
      <img class="logo-dark" src="assets/logo/logo-primary.svg" alt="Tanuwijaya &amp; Partners" width="720" height="144">
    </a>
    <nav class="nav" aria-label="Primary">%s
    </nav>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<div class="drawer" id="drawer">
  <nav aria-label="Mobile">%s
  </nav>
  <div class="drawer__foot">
    Ciputra World 2, Tokopedia Tower Unit 20D,<br>
    Jl. Prof. DR. Satrio No.Kav. 11 Jakarta 12950 - Indonesia<br>
    <a href="tel:02183780660">021-8378 0660/0770</a>
  </div>
</div>
""" % (links, drawer_links)


def hero(title_top, title_thin, lead, button, img, alt):
    return """
<section class="hero">
  <div class="hero__media"><img src="assets/img/%s" alt="%s" fetchpriority="high" width="2000" height="1180"></div>
  <div class="hero__scrim"></div>
  <img class="hero__mark" src="assets/logo/mark-light.svg" alt="" aria-hidden="true">
  <div class="shell hero__inner">
    <h1 data-reveal>%s<span class="thin">%s</span></h1>
    <p class="lead" data-reveal style="--d:120ms">%s</p>
    <div class="btn-row" data-reveal style="--d:220ms">%s</div>
  </div>
</section>
""" % (img, alt, title_top, title_thin, lead, button)


def sec_head(title, text=""):
    return '<div class="sec-head" data-reveal><h2 class="h2">%s</h2>%s</div>' % (
        title, ('<p>%s</p>' % text) if text else "")


def services_grid():
    items = []
    for ic, title, lis in SERVICES:
        items.append("""<div class="svc" data-reveal>
        <div class="svc__head"><span class="svc__icon">%s</span><h3>%s</h3></div>
        <div class="svc__rule"></div>
        <ul>%s</ul>
      </div>""" % (icon(ic), title, "".join("<li>%s</li>" % i for i in lis)))
    return '<div class="svc-grid">%s</div>' % "".join(items)


def industries_grid():
    items = []
    for ic, title, desc in INDUSTRIES:
        items.append("""<div class="svc" data-reveal>
        <div class="svc__head"><span class="svc__icon">%s</span><h3>%s</h3></div>
        <div class="svc__rule"></div>
        <p>%s</p>
      </div>""" % (icon(ic), title, desc))
    return '<div class="svc-grid">%s</div>' % "".join(items)


def client_row(items):
    return '<div class="clients">%s</div>' % "".join(
        '<div class="clients__cell" data-reveal><img src="assets/img/clients/%s.webp" alt="%s" loading="lazy"></div>'
        % (slug, name) for slug, name in items)


def person_card(slug, name, role, mail):
    return """<article class="person" data-reveal>
        <div class="person__media"><img src="assets/img/people/%s.webp" alt="%s" loading="lazy" width="760" height="880"></div>
        <h3>%s</h3>
        <span class="person__role">%s</span>
        <a class="person__mail" href="mailto:%s">%s</a>
      </article>""" % (slug, name, name, role, mail, mail)


def cta(title, text):
    return """
<section class="cta">
  <div class="cta__bg"><img src="assets/img/cta-band.webp" alt="" aria-hidden="true" loading="lazy" width="1840" height="520"></div>
  <div class="shell">
    <h2 class="h2" data-reveal>%s</h2>
    <p data-reveal style="--d:80ms">%s</p>
    <div class="btn-row" data-reveal style="--d:160ms">%s</div>
  </div>
</section>
""" % (title, text, btn("contact.html", "Schedule Consultation", "btn--solidLight"))


def footer():
    return """
<footer class="footer">
  <div class="shell">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/logo/logo-light.svg" alt="Tanuwijaya &amp; Partners" width="720" height="144">
      </div>
      <div>
        <h4>Contact Details</h4>
        <address>
          Ciputra World 2, Tokopedia Tower Unit 20D,<br>
          Jl. Prof. DR. Satrio No.Kav. 11<br>
          Jakarta 12950 - Indonesia<br><br>
          <a href="tel:02183780660">021-8378 0660/0770</a><br>
          <a href="%s">08119112147</a>
        </address>
      </div>
      <div>
        <h4>Office Hours</h4>
        <dl class="footer__hours">
          <dt>Monday to Friday</dt><dd>9:00 am to 6:00 pm</dd>
          <dt>Saturday</dt><dd>9:00 am to 12 noon</dd>
          <dt>Closed on Sundays</dt><dd></dd>
        </dl>
      </div>
      <div>
        <h4>Follow Us</h4>
        <div class="social">
          <a href="https://www.facebook.com" target="_blank" rel="noopener" aria-label="Facebook">%s</a>
          <a href="https://www.instagram.com" target="_blank" rel="noopener" aria-label="Instagram">%s</a>
          <a href="https://www.linkedin.com" target="_blank" rel="noopener" aria-label="LinkedIn">%s</a>
        </div>
      </div>
    </div>
  </div>
</footer>

<a class="wa" href="%s" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">%s</a>
<script src="assets/js/main.js"></script>
</body>
</html>
""" % (WA, social("facebook"), social("instagram"), social("linkedin"), WA,
       '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % SOCIAL["whatsapp"])


# ---------------------------------------------------------------- pages
def page_home():
    acc, figs = [], []
    for i, (key, name, img, initials) in enumerate(PARTNERS):
        acc.append("""<div class="acc__item">
        <button class="acc__btn" type="button" aria-expanded="%s" aria-controls="p-%s" data-figure="%s">
          <span>%s</span><span class="acc__sign" aria-hidden="true"></span>
        </button>
        <div class="acc__panel" id="p-%s"><div><p>%s</p></div></div>
      </div>""" % ("true" if i == 0 else "false", key, key, name, key, FOUNDING))
        if img:
            figs.append('<img data-figure-target="%s" class="%s" src="%s" alt="%s" loading="lazy">'
                        % (key, "is-active" if i == 0 else "", img, name))
        else:
            figs.append('<div class="partner-figure__placeholder" data-figure-target="%s"><b>%s</b></div>'
                        % (key, initials))

    return (
        head("Home", "Tanuwijaya &amp; Partners is a boutique corporate services firm delivering accounting, audit, tax and legal solutions.")
        + header("index.html")
        + '<main id="main">'
        + hero("Corporate Services", "Redefined",
               "Tanuwijaya &amp; Partners is a boutique corporate services firm. Our team of experts delivers comprehensive corporate services, including accounting, audit, tax, and legal solutions, tailored to your unique needs. With our expertise and personalized approach, you&rsquo;ll gain clarity, efficiency, and peace of mind, allowing you to focus on driving growth and innovation.",
               btn("industries-services.html", "Explore Services"),
               "hero-home.webp", "Advisers reviewing financial reports with a client")
        + """
<section class="section section--luster" id="story">
  <div class="shell">
    <div class="duo duo--center">
      <div class="figure figure--inset" data-reveal>
        <img class="ratio-3x4" src="assets/img/story-building.webp" alt="Office towers in the Jakarta business district" loading="lazy" width="1100" height="1467">
      </div>
      <div class="duo__text">
        <h2 class="h2" data-reveal>Founding Story</h2>
        <p class="lead mt-m" data-reveal style="--d:80ms">%s</p>
        <div class="btn-row" data-reveal>%s</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" data-partners>
  <div class="shell">
    <div class="duo duo--top">
      <div class="duo__text">
        <h2 class="h2" data-reveal>Our Partners</h2>
        <p class="lead mt-s" data-reveal style="--d:60ms">Trusted by clients since 1999</p>
        <div class="accordion mt-l" data-accordion data-reveal style="--d:120ms">%s</div>
        <div class="btn-row" data-reveal>%s</div>
      </div>
      <div class="partner-figure" data-reveal style="--d:120ms">
        <div class="partner-figure__img">%s</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--luster" id="services">
  <div class="shell">
    <div class="split-label">
      <div class="split-label__aside">
        <h2 class="h2" data-reveal>Our Services</h2>
        <p data-reveal style="--d:60ms">Trusted by clients since 1999</p>
      </div>
      <div>%s</div>
    </div>
  </div>
</section>
""" % (FOUNDING, btn("contact.html", "Get in touch", "btn--ghost"),
       "".join(acc), btn("our-people.html", "Get to know our team", "btn--ghost"),
       "".join(figs), services_grid())
        + cta("Ready to Partner with us?",
              "Let&rsquo;s discuss how our tailored corporate services can support your business objectives and drive sustainable growth")
        + "</main>" + footer())


def page_about():
    return (
        head("About Us", "Since 1989, Tanuwijaya &amp; Partners has built lasting relationships through expert care and trusted corporate services.")
        + header("about.html")
        + '<main id="main">'
        + hero("Our Humble", "Beginning",
               "Since 1989, Tanuwijaya &amp; Partners has built lasting relationships through expert legal care and trusted corporate services. As a family-owned firm, we are dedicated to long-term partnerships&mdash;supporting businesses and individuals from local enterprises to global organizations.",
               btn("#story", "Learn more about us"),
               "hero-about.webp", "Office facade in the Jakarta business district")
        + """
<section class="section section--luster" id="story">
  <div class="shell">
    <div class="duo">
      <div class="duo__text">
        <h2 class="h2" data-reveal>Founding Story</h2>
        <p class="lead mt-m" data-reveal style="--d:80ms">%s</p>
      </div>
      <div class="figure figure--layered" data-reveal style="--d:120ms">
        <img class="ratio-3x2" src="assets/img/about-founding.webp" alt="The Tanuwijaya &amp; Partners team" loading="lazy" width="1500" height="1000">
      </div>
    </div>
    <div class="duo duo--flip mt-l" style="margin-top:clamp(3rem,6vw,5.5rem)">
      <div class="duo__text">
        <p class="lead" data-reveal>%s</p>
      </div>
      <div class="figure" data-reveal style="--d:120ms">
        <img class="ratio-3x2" src="assets/img/about-office.webp" alt="The Tanuwijaya &amp; Partners office" loading="lazy" width="1500" height="1000">
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="clients">
  <div class="shell">
    %s
    %s
    %s
  </div>
</section>
""" % (FOUNDING, FAMILY, sec_head("Clients", CLIENTS_TEXT), client_row(CLIENTS), client_row(INSTITUTIONS))
        + cta("Get to know us better",
              "Let&rsquo;s discuss how our tailored corporate services can support your business objectives and drive sustainable growth")
        + "</main>" + footer())


def page_people():
    return (
        head("Our People", "Partners, managers and associates of Tanuwijaya &amp; Partners.")
        + header("our-people.html")
        + '<main id="main">'
        + hero("Trusted by clients", "since 1999", FAMILY,
               btn("#partners", "Get to know our team"),
               "hero-people.webp", "The Tanuwijaya &amp; Partners team in discussion")
        + """
<section class="section section--luster" id="partners">
  <div class="shell">
    %s
    <div class="people">%s</div>
  </div>
</section>

<section class="section section--white">
  <div class="shell">
    %s
    <div class="people">%s</div>
  </div>
</section>

<section class="section section--luster">
  <div class="shell">
    %s
    <div class="companies">%s</div>
  </div>
</section>
""" % (sec_head("Partners"),
       "".join(person_card(*p) for p in TEAM_PARTNERS),
       sec_head("Associates", "Our associates are highly qualified professionals who deliver exceptional service quality and technical precision across all practice areas."),
       "".join(person_card(*a) for a in ASSOCIATES),
       sec_head("Companies"),
       "".join(
           '<div class="company" data-reveal><span class="company__name">%s</span>%s</div>' % (
               name,
               ('<a class="company__url" href="%s" target="_blank" rel="noopener">%s</a>' % (url, label)) if url
               else '<span class="company__url">%s</span>' % label)
           for name, label, url in COMPANIES))
        + cta("Work with our team",
              "Connect with our professionals to discuss how we can support your business objectives with tailored solutions")
        + "</main>" + footer())


def page_industries():
    return (
        head("Industries &amp; Services", "Private client services, maritime, import export, plantation and retail &mdash; supported by audit, tax, legal and corporate services.")
        + header("industries-services.html")
        + '<main id="main">'
        + hero("Top-notch", "Corporate Services",
               "Trusted by generations, we deliver professional corporate solutions with personalized care, confidentiality, and unwavering integrity",
               btn("#industries", "Learn more"),
               "hero-industries.webp", "Jakarta business district")
        + """
<section class="section section--white" id="industries">
  <div class="shell">
    <div class="split-label">
      <div class="split-label__aside"><h2 class="h2" data-reveal>Industries</h2></div>
      <div>%s</div>
    </div>
  </div>
</section>

<section class="section section--luster" id="services">
  <div class="shell">
    <div class="split-label">
      <div class="split-label__aside"><h2 class="h2" data-reveal>Our Services</h2></div>
      <div>%s</div>
    </div>
  </div>
</section>
""" % (industries_grid(), services_grid())
        + cta("Learn more about our services",
              "Get to know more how we can assist your industry with our available services tailored specifically for you.")
        + "</main>" + footer())


def page_contact():
    offices = """<div class="office" data-reveal>
        <span class="office__country">Indonesia</span>
        <h3>Main Office</h3>
        <address>Ciputra World 2, Tokopedia Tower Unit 20D<br>Jl. Prof. DR. Satrio Kav 11, Jakarta 12950</address>
        <dl><div><dt>Tel</dt><dd><a href="tel:02183780660">021-8378 0660 / 0770</a></dd></div></dl>
      </div>
      <div class="office" data-reveal>
        <span class="office__country" aria-hidden="true"></span>
        <h3>Public Accounting Firm Tanuwijaya (KAP TWJ)</h3>
        <address>Citiloft Sudirman #10-17<br>Jl. KH Mas Mansyur Kav 121, Jakarta 10220</address>
        <dl>
          <div><dt>Email</dt><dd><a href="mailto:kap@twj.co.id">kap@twj.co.id</a></dd></div>
          <div><dt>Tel</dt><dd><a href="tel:02125558456">021-2555 8456</a></dd></div>
        </dl>
      </div>
      <div class="office" data-reveal>
        <span class="office__country">Singapore</span>
        <h3>Aurora Corporate Services Pte Ltd</h3>
        <address>133 Cecil Street, #10-02<br>Keck Seng Tower, Singapore 069535</address>
        <dl>
          <div><dt>Email</dt><dd><a href="mailto:auroracorporateservices@gmail.com">auroracorporateservices@gmail.com</a></dd></div>
          <div><dt>Tel</dt><dd><a href="tel:6568096226">+65 6809 6226 / 6227 / 6228</a></dd></div>
          <div><dt>Fax</dt><dd>+65 6809 6201</dd></div>
        </dl>
      </div>"""

    return (
        head("Contact", "Schedule a consultation with Tanuwijaya &amp; Partners &mdash; offices in Jakarta and Singapore.")
        + header("contact.html")
        + '<main id="main">'
        + hero("Let&rsquo;s start a", "Conversation",
               "Schedule a consultation and get to know us more and let us be your solution to your problem.",
               btn("#message", "Schedule Consultation"),
               "hero-contact.webp", "Reviewing documents with a client")
        + """
<section class="section section--luster" id="message">
  <div class="shell">
    <div class="contact-grid">
      <div>
        <h2 class="h2" data-reveal>Leave a Message</h2>
        <p class="lead mt-m" data-reveal style="--d:60ms">Send us a message and schedule a consultation. We&rsquo;ll get back to you as soon as possible</p>
      </div>
      <div>
        <form data-contact data-wa="%s" data-mail="info@twj.co.id" data-reveal style="--d:120ms">
          <div class="channel">
            <label><input type="radio" name="channel" value="whatsapp" checked><span class="dot"></span><span class="txt">Send Whatsapp Message</span></label>
            <label><input type="radio" name="channel" value="email"><span class="dot"></span><span class="txt">Send Email</span></label>
          </div>
          <div class="field-row">
            <div class="field"><label for="fn">First Name</label><input id="fn" name="first_name" type="text" autocomplete="given-name" required></div>
            <div class="field"><label for="ln">Last Name</label><input id="ln" name="last_name" type="text" autocomplete="family-name"></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="em">Email</label><input id="em" name="email" type="email" autocomplete="email"></div>
            <div class="field"><label for="mb">Mobile Number</label><input id="mb" name="mobile" type="tel" autocomplete="tel"></div>
          </div>
          <div class="field"><label for="ms">Message</label><textarea id="ms" name="message" rows="5" required></textarea></div>
          <div class="btn-row mt-0">
            <button class="btn" type="submit"><span data-submit-label>Send Whatsapp Message</span><span class="arrow" aria-hidden="true">&#8594;</span></button>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="offices">
  <div class="shell">
    %s
    <div class="offices">%s</div>
  </div>
</section>
""" % (WA, sec_head("Our Offices"), offices)
        + "</main>" + footer())


PAGES = {
    "index.html": page_home,
    "about.html": page_about,
    "our-people.html": page_people,
    "industries-services.html": page_industries,
    "contact.html": page_contact,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        html = fn()
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote %-26s %6d bytes" % (name, len(html.encode("utf-8"))))
