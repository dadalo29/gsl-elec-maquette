"""Éléments communs du site GSL-ELEC : icônes, en-tête, pied de page, gabarit."""
from html import escape

WA_NUM = "33768026171"
WA_TXT = "Bonjour%2C%20je%20souhaite%20un%20devis%20solaire"
WA = f"https://wa.me/{WA_NUM}?text={WA_TXT}"
TEL = "tel:+221777019883"
TEL_TXT = "+221 77 701 98 83"
WA_TXT_AFF = "+33 7 68 02 61 71"
MAIL = "contact@gsl-elec.sn"

P = {
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="m9 6 6 6-6 6"/>',
    "check": '<path d="m5 12 4.5 4.5L19 7"/>',
    "wa": '<path d="M3.5 20.5 5 16a8.5 8.5 0 1 1 3 3z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 1a4 4 0 0 1-2-2l1-1-1-2z"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h10"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "house": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "factory": '<path d="M3 21V10l6 4V10l6 4V6l6 3v12z"/><path d="M3 21h18"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5"/>',
    "snow": '<path d="M12 2v20M4.9 6.5l14.2 11M19.1 6.5 4.9 17.5"/><path d="m9.5 3.5 2.5 2 2.5-2M9.5 20.5l2.5-2 2.5 2"/>',
    "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "shieldbolt": '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6z"/><path d="m13 7.5-3 5h4l-3 5"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "gauge": '<path d="M4 15a8 8 0 1 1 16 0"/><path d="m12 15 4-4"/><path d="M4 19h16"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="m10 14 2 2 3-4"/>',
    "doclines": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h4"/>',
    "card": '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18"/><path d="M16 15h2"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
    "panel": '<path d="M5 5h16l-2.5 10H2.5z"/><path d="M3.8 10h16M10 5l-1.6 10M15.5 5l-1.6 10"/><path d="M10.5 15v4M7 21h7"/>',
    "inverter": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8.5 12c1-2 2-2 3.5 0s2.5 2 3.5 0"/><path d="M9 7h6"/>',
    "battery": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M6 8h12M6 14h12"/><path d="m12.5 4.5-1.5 2h2l-1.5 2"/>',
    "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/><path d="M10 21v-3h4v3"/>',
    "pylon": '<path d="M12 2 7 22M12 2l5 20M8.5 8h7M7.5 13h9M6.5 18h11"/>',
    "genset": '<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M7 7V5h4v2"/><path d="m12 10-2 3h3l-2 3"/>',
    "bracket": '<path d="M3 9 21 5"/><path d="M4 21h16"/><path d="M7 8.3V21M17 6V21"/>',
    "monitor": '<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="m9 14 2-3 2 2 2-4"/><path d="M11 18.5h2"/>',
    "image": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 8"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "upload": '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-3"/>',
    "download": '<path d="M12 4v12M7 11l5 5 5-5"/><path d="M4 20h16"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "eye": '<circle cx="12" cy="12" r="3"/><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/>',
    "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
    "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "stack": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M6 8h12M6 14h12"/><path d="M12 17v2M11 18h2"/>',
    "square": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 12h16"/>',
    "nogas": '<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M7 7V5h4v2"/><path d="M4 21 20 5"/>',
    "down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
}


def ico(name, size=24, sw=1.8, cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{P[name]}</svg>')


ARROW = ico("arrow", 18, 2.2)

NAV = [
    ("solutions", "Nos solutions", "solutions.html"),
    ("equipements", "Équipements", "equipements.html"),
    ("etapes", "Comment ça marche", "comment-ca-marche.html"),
    ("realisations", "Réalisations", "realisations.html"),
    ("financement", "Financement", "financement.html"),
    ("apropos", "À propos", "a-propos.html"),
    ("conseils", "Conseils", "conseils.html"),
]

SERVICES = [
    ("maison", "Solaire maison et commerce", "solaire-maison-commerce.html"),
    ("pro", "Solaire pro et industriel", "solaire-professionnel-industriel.html"),
    ("pompage", "Pompage solaire", "pompage-solaire.html"),
    ("appareils", "Appareils basse consommation", "appareils-basse-consommation.html"),
    ("maintenance", "Maintenance et SAV", "maintenance-sav.html"),
    ("electricite", "Installations électriques", "installations-electriques.html"),
]


CUR = ' aria-current="page"'


def header(active):
    items = "".join(
        f'<li><a href="{h}"{CUR if k == active else ""}>{escape(l)}</a></li>' for k, l, h in NAV)
    mitems = "".join(
        f'<li><a class="nav-link" href="{h}"{CUR if k == active else ""}>{escape(l)}{ico("chev", 18, 2)}</a></li>'
        for k, l, h in [("accueil", "Accueil", "index.html")] + NAV + [("faq", "FAQ", "faq.html"), ("contact", "Contact", "contact.html")])
    return f'''<a class="skip-link" href="#contenu">Aller au contenu</a>
<div class="topbar"><div class="container">
<span>{ico("pin", 16, 2)}Interventions partout au Sénégal<span class="hide-m">&nbsp;· Diaspora : interlocuteur joignable en France</span></span>
<span class="links"><a href="{TEL}">{ico("phone", 15, 2)}{TEL_TXT}</a><a class="hide-m" href="{WA}">{ico("wa", 15, 2)}WhatsApp {WA_TXT_AFF}</a></span>
</div></div>
<header class="site-header"><div class="container">
<a class="brand" href="index.html" aria-label="GSL-ELEC, retour à l’accueil"><img src="assets/img/gsl-logo.png" alt="GSL-ELEC — Gestion Solaire Locale et Électricité" width="816" height="212"></a>
<nav class="main-nav" aria-label="Menu principal"><ul>{items}</ul></nav>
<div class="header-actions">
<a class="btn btn-vert btn-s" href="contact.html">Demander un devis{ico("arrow", 16, 2.2)}</a>
<a class="icon-btn call" href="{TEL}" aria-label="Appeler GSL-ELEC">{ico("phone", 21, 1.9)}</a>
<button class="icon-btn" type="button" data-menu-toggle aria-controls="mobile-nav" aria-expanded="false" aria-label="Ouvrir le menu"><span class="i-open">{ico("menu", 22, 2)}</span><span class="i-close" hidden>{ico("close", 22, 2)}</span></button>
</div>
</div>
<nav class="mobile-nav" id="mobile-nav" aria-label="Menu mobile"><ul>{mitems}</ul><a class="btn btn-vert btn-bloc" href="contact.html">Demander un devis gratuit</a></nav>
</header>'''


def footer():
    svc = "".join(f'<a href="{h}">{escape(l)}</a>' for k, l, h in SERVICES[:2]) + \
        '<a href="batteries-haute-tension.html">Batteries haute tension</a>' + \
        "".join(f'<a href="{h}">{escape(l)}</a>' for k, l, h in SERVICES[2:])
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div class="footer-brand">
<span class="footer-logo"><img src="assets/img/gsl-logo.png" alt="GSL-ELEC" width="816" height="212" loading="lazy"></span>
<p>Gestion Solaire Locale et Électricité. Étude, installation et suivi de solutions solaires et électriques partout au Sénégal.</p>
<div class="stack" style="gap:10px"><strong style="color:#fff;font-size:13px">Suivez-nous</strong>
<div class="socials"><a href="#">Facebook</a><a href="#">Instagram</a><a href="#">TikTok</a><a href="#">LinkedIn</a></div>
<a href="#" style="color:var(--orange-clair);font-weight:600;display:inline-flex;align-items:center;gap:6px">{ico("star", 15, 2)}Notre fiche Google — laissez-nous un avis</a></div>
</div>
<div class="footer-col"><strong>Nos solutions</strong>{svc}</div>
<div class="footer-col"><strong>GSL-ELEC</strong><a href="a-propos.html">À propos</a><a href="comment-ca-marche.html">Comment ça marche</a><a href="equipements.html">Nos équipements</a><a href="realisations.html">Réalisations</a><a href="financement.html">Financement</a><a href="conseils.html">Conseils</a><a href="faq.html">FAQ</a></div>
<div class="footer-col"><strong>Contact</strong><a href="{TEL}">Mobile : {TEL_TXT}</a><a href="{WA}">WhatsApp : {WA_TXT_AFF}</a><a href="mailto:{MAIL}">{MAIL}</a><span>Partout au Sénégal</span>
<a class="btn btn-orange btn-s" href="contact.html" style="align-self:flex-start;margin-top:6px">Demander un devis</a></div>
</div>
<div class="footer-bottom"><span>© <span data-year>2026</span> GSL-ELEC — Gestion Solaire Locale et Électricité</span><span style="display:flex;gap:20px;flex-wrap:wrap"><a href="mentions-legales.html">Mentions légales</a><a href="mentions-legales.html#confidentialite">Politique de confidentialité</a></span></div>
</div></footer>
<a class="wa-float" href="{WA}" aria-label="Écrire à GSL-ELEC sur WhatsApp">{ico("wa", 30, 1.9)}</a>
<nav class="action-bar" aria-label="Actions rapides">
<a href="{TEL}">{ico("phone", 22, 1.9)}Appeler</a>
<a class="wa" href="{WA}">{ico("wa", 22, 1.9)}WhatsApp</a>
<a class="devis" href="contact.html">{ico("doclines", 22, 1.9)}Devis</a>
</nav>'''


def cta_band():
    return f'''<section class="section-tight"><div class="container"><div class="cta-band">
<div class="deco-cercle" style="right:-120px;top:-160px;width:420px;height:420px;background:var(--vert-cercle)" aria-hidden="true"></div>
<div style="flex:1 1 420px;min-width:0"><h2>Prêt à réduire votre facture <span class="accent">d’électricité ?</span></h2><p>Devis gratuit, réponse rapide, partout au Sénégal.</p></div>
<div class="btns"><a class="btn btn-orange" href="contact.html">Demander un devis gratuit{ARROW}</a><a class="btn btn-contour" href="{WA}">{ico("wa", 20, 1.9)}WhatsApp</a><a class="btn btn-contour" style="border-color:rgba(255,255,255,.35)" href="{TEL}">{ico("phone", 18, 1.9)}Appeler</a></div>
</div></div></section>'''


def crumbs(*items):
    out = ['<nav class="breadcrumb" aria-label="Fil d’Ariane"><a href="index.html">Accueil</a>']
    for label, href in items:
        out.append('<span aria-hidden="true">›</span>')
        out.append(f'<a href="{href}">{escape(label)}</a>' if href else f'<span aria-current="page">{escape(label)}</span>')
    out.append('</nav>')
    return "".join(out)


def page(title, desc, active, body, canonical):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#0E5A2F">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_SN">
<meta property="og:image" content="assets/img/hero-famille.jpg">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" type="image/png" href="assets/img/gsl-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header(active)}
<main id="contenu">
{body}
</main>
{footer()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
