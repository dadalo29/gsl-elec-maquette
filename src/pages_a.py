"""Accueil, solutions, pages service, batteries haute tension."""
from common import ico, ARROW, WA, TEL, TEL_TXT, WA_TXT_AFF, SERVICES, cta_band, crumbs
from data import EQUIP, FAQ_HOME, SERVICE_DATA, equip_card, faq_items, contact_form
from produits import bande, bess_cards, spec_table

CK = ico("check", 18, 2.4)


def solution_cards(compact=False):
    cards = [
        ("maison", "house", "5 à 50 kWc", "Solaire maison et commerce", "Villas, maisons, boutiques et bureaux : produisez votre électricité le jour et stockez-la pour le soir et les coupures.", ["Villas", "Boutiques", "Bureaux"], False),
        ("pro", "factory", "Jusqu’à 200 kWc", "Solaire professionnel et industriel", "Restaurants, hôtels, pharmacies, écoles, ateliers et industries, avec stockage par batteries haute tension.", ["Hôtels", "Industries", "Pharmacies"], True),
        ("pompage", "drop", "Sans gasoil", "Pompage solaire", "Forage, irrigation, élevage et maraîchage : pompez l’eau grâce au soleil, sans carburant ni réseau.", ["Maraîchage", "Élevage", "Forages"], False),
        ("appareils", "snow", "Moins de besoins", "Appareils à faible consommation", "Réfrigérateurs, congélateurs, climatiseurs inverter et LED : consommez moins, pour une installation plus petite et moins chère.", ["Froid", "Climatisation", "Éclairage"], False),
        ("maintenance", "shield", "Contrats annuels", "Maintenance et SAV", "Inspection, nettoyage des panneaux, contrôle des batteries et de l’installation, contrats d’entretien annuels.", ["Nettoyage", "Contrôle", "Dépannage"], False),
        ("electricite", "bolt", "Dépannage", "Installations électriques", "Électricité générale, automatisme et dépannage, pour particuliers et professionnels.", ["Tableaux", "Automatisme", "Mise à la terre"], False),
    ]
    href = {k: h for k, l, h in SERVICES}
    out = []
    for k, icon, badge, title, desc, tags, dark in cards:
        tagh = "" if compact else '<div class="chips" style="gap:6px">' + "".join(
            f'<span class="tag"{" style=\"background:rgba(255,255,255,.1)\"" if dark else ""}>{t}</span>' for t in tags) + "</div>"
        cls = "card card-sombre" if dark else "card"
        ib = "ib-orange" if dark else "ib-vert"
        bd = "badge-orange" if dark else "badge-vert"
        out.append(f'''<a class="{cls}" href="{href[k]}">
<div style="display:flex;justify-content:space-between;align-items:center;gap:10px"><span class="icon-box lg {ib}">{ico(icon, 30)}</span><span class="badge {bd}">{badge}</span></div>
<h3 class="h3">{title}</h3><p>{desc}</p>{tagh}
<span class="more">{"Découvrir l’offre pro" if dark else "Découvrir"}{ico("arrow", 16, 2.2)}</span></a>''')
    return "\n".join(out)


def simulateur():
    presets = "".join(f'<button type="button" class="chip" data-preset="{v}" aria-pressed="false">{l}</button>' for v, l in [(25000, "25 000 FCFA"), (45000, "45 000 FCFA"), (100000, "100 000 FCFA"), (250000, "250 000 FCFA")])
    return f'''<div class="simu" data-simu>
<div class="segmented" role="group" aria-label="Type de client"><button type="button" data-type="maison" aria-pressed="true">Maison</button><button type="button" data-type="commerce" aria-pressed="false">Commerce / bureau</button></div>
<div class="stack" style="gap:12px">
<label for="facture" style="font-size:15px;font-weight:600;color:var(--texte)">Votre facture d’électricité mensuelle</label>
<div class="simu-amount"><span data-out="facture">45 000</span> <small>FCFA</small></div>
<input id="facture" type="range" min="15000" max="600000" step="5000" value="45000">
<div class="chips">{presets}</div>
</div>
<div class="simu-results">
<div class="res main"><span>Économie / mois</span><strong data-out="eco-mois">—</strong><em>FCFA environ</em></div>
<div class="res"><span>Économie / an</span><strong data-out="eco-an">—</strong><em>FCFA environ</em></div>
<div class="res"><span>Puissance indicative</span><strong><span data-out="kwc">—</span> kWc</strong><em>à confirmer à l’étude</em></div>
</div>
<div class="bars" aria-hidden="true">
<div class="bar"><span class="lbl">Avant</span><span class="track"><span class="fill" style="width:100%;background:#C9B48A;display:block"></span></span><span class="val" data-out="facture">45 000</span></div>
<div class="bar"><span class="lbl">Après</span><span class="track"><span class="fill" data-out="bar-apres" style="width:30%;background:var(--vert);display:block"></span></span><span class="val" style="color:var(--vert-cta);font-weight:700" data-out="apres">—</span></div>
</div>
<a class="btn btn-vert btn-bloc" href="contact.html">Recevoir mon étude personnalisée{ARROW}</a>
<p class="tiny muted">Estimation indicative, non contractuelle. Calcul sur la grille Senelec 2026 (<span data-out="grille">usage domestique</span>), hors redevances, avec une production moyenne de 130 kWh par kWc et par mois. Les économies réelles dépendent de chaque installation.</p>
</div>'''


def flow_figure(vertical_backup=True):
    a = ico("arrow", 26, 2.2)
    return f'''<figure class="figure" aria-label="Schéma : panneaux, onduleur, batteries haute tension, bâtiment, avec secours réseau et groupe électrogène">
<figcaption style="font-size:15px;font-weight:700;color:var(--vert-hover)">Comment ça fonctionne</figcaption>
<div class="flow">
<div class="flow-step" style="background:var(--creme-2)"><span style="color:var(--orange-texte)">{ico("panel", 36, 1.6)}</span><strong>1. Panneaux solaires</strong><span class="muted">Sur toiture, au sol ou en ombrière, ils produisent l’électricité dès le lever du soleil.</span></div>
<div class="flow-step" style="background:var(--vert-fonce);color:#fff"><span style="color:var(--orange-clair)">{ico("inverter", 36, 1.6)}</span><strong>2. Onduleur hybride</strong><span style="color:var(--sur-vert-2)">Le cerveau : il alimente vos équipements, charge les batteries et bascule automatiquement.</span></div>
<div class="flow-step" style="background:var(--vert-pale-2)"><span style="color:var(--vert-cta)">{ico("battery", 36, 1.6)}</span><strong>3. Batteries haute tension</strong><span style="color:var(--texte)">Elles stockent le surplus de la journée pour la nuit et les coupures.</span></div>
<div class="flow-step" style="background:#fff;border:2px solid var(--vert)"><span style="color:var(--vert-cta)">{ico("building", 36, 1.6)}</span><strong>4. Votre bâtiment</strong><span class="muted">Hôtel, usine, clinique : alimenté sans interruption.</span></div>
</div>
<div class="flow-backup"><span>En secours, l’onduleur bascule automatiquement sur :</span><span class="pill">{ico("pylon", 18)}Réseau Senelec</span><span class="pill">{ico("genset", 18)}Groupe électrogène</span></div>
</figure>'''


def index():
    strengths = [("gauge", "ib-pale", "Étude de charge", "Nous calculons votre besoin réel avant toute installation."),
                 ("doc", "ib-pale", "Matériel documenté et garanti", "Fiches techniques et garanties remises pour chaque équipement."),
                 ("card", "ib-creme", "Paiement en plusieurs fois", "Le solaire accessible, sans tout payer d’un coup."),
                 ("headset", "ib-pale", "Suivi et SAV", "Maintenance, nettoyage et contrats annuels.")]
    st = "".join(f'<div class="strength"><span class="icon-box {c}" style="width:48px;height:48px">{ico(i, 24)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i, c, t, d in strengths)
    home_equip = [e for e in EQUIP][:8]
    eq = "".join(equip_card(e, small=True) for e in home_equip)
    steps = [("Prise de contact", "WhatsApp, appel ou formulaire : vous nous parlez de votre besoin."),
             ("Visite et étude de charge", "Nous mesurons vos appareils et votre consommation réelle."),
             ("Devis détaillé", "Matériel, puissance, prix et modalités de paiement, en toute clarté."),
             ("Installation", "Pose soignée des panneaux, onduleurs, batteries et protections."),
             ("Mise en service", "Tests, réglages et explications pour bien utiliser votre système."),
             ("Suivi et SAV", "Supervision, entretien et dépannage tout au long de la vie de l’installation.")]
    sl = "".join(f'<li class="{"last" if i == 5 else ""}"><span class="num{" o" if i == 5 else ""}">{i + 1}</span><strong>{t}</strong><span class="d">{d}</span></li>' for i, (t, d) in enumerate(steps))
    reals = [("Maison", "Villa familiale — [Ville]", "[Puissance] kWc · onduleur hybride · batteries lithium", False),
             ("Hôtel", "Hôtel — [Ville]", "[Puissance] kWc · batteries haute tension", True),
             ("Agriculture", "Pompage solaire — [Ville]", "Forage · pompe immergée · [Puissance] kWc", False)]
    rl = "".join(f'''<a class="card card-media" href="realisations.html"><div class="placeholder ratio-43{" orange" if o else ""}">{ico("image", 40, 1.5)}Photo du chantier</div>
<div class="card-body"><span class="badge {"badge-orange" if o else "badge-vert"}">{c}</span><strong style="font-size:17px">{t}</strong><span class="small muted">{d}</span></div></a>''' for c, t, d, o in reals)
    return f'''
<section class="hero hero-home">
<div class="deco-cercle" style="right:-180px;top:-220px;width:720px;height:720px;background:var(--vert-cercle)" aria-hidden="true"></div>
<div class="deco-cercle" style="left:-120px;bottom:-260px;width:520px;height:520px;background:#0C5129" aria-hidden="true"></div>
<div class="container"><div class="row">
<div class="col stack" style="flex-basis:520px;gap:24px">
<span class="badge badge-verre">{ico("sun", 16, 2, extra=' style="color:var(--orange)"')}Solaire &amp; électricité au Sénégal</span>
<h1 class="h1">Réduisez votre facture d’électricité <span class="accent">avec le solaire.</span></h1>
<p class="lead"><strong style="color:#fff;font-weight:600">Produire, stocker et économiser.</strong> GSL-ELEC étudie votre consommation, installe un système solaire dimensionné pour vous et en assure le suivi — pour les maisons, commerces, hôtels, industries et exploitations agricoles.</p>
<div class="btns"><a class="btn btn-orange" href="contact.html">Demander un devis gratuit{ARROW}</a><a class="btn btn-contour" href="{WA}">{ico("wa", 20, 1.9)}Écrire sur WhatsApp</a></div>
<div class="hero-checks"><span>{CK}Devis gratuit</span><span>{CK}Paiement en plusieurs fois</span><span>{CK}Suivi et SAV</span></div>
</div>
<div class="col" style="flex-basis:440px">
<div class="hero-photo">
<div class="frame"><img src="assets/img/hero-famille-maison.jpg" alt="Une famille sourit en comparant sa facture d’électricité, devant une maison équipée de panneaux solaires" width="1200" height="860" fetchpriority="high"></div>
<div class="bill-card"><span class="label">Exemple de facture mensuelle</span><span class="vals"><s>45 000</s>{ico("arrow", 18, 2.4, extra=' style="color:var(--vert-cta)"')}<strong>15 000 <small>FCFA</small></strong></span><span class="tiny" style="color:#5B6B62">Exemple indicatif — selon chaque installation</span></div>
<div class="pill-float">{ico("bolt", 18, 2.2)}Jusqu’à 200 kWc</div>
</div>
</div>
</div></div>
</section>

<section class="strengths" aria-label="Nos engagements"><div class="container"><div class="strengths-box">{st}</div></div></section>

<section class="section" id="solutions"><div class="container stack-l">
<div class="section-head"><div><span class="eyebrow">Nos solutions</span><h2 class="h2">Une solution solaire pour chaque besoin</h2></div>
<p class="muted" style="max-width:440px;font-size:17px">De la villa familiale à l’usine, chaque projet commence par une étude de votre consommation réelle.</p></div>
{bande("bande-stockage.jpg", "Gamme de solutions de stockage d’énergie GSL-ELEC : batteries et armoires pour maisons, commerces, hôtels et industries", 1600, 577)}
<div class="grid grid-3">{solution_cards(compact=True)}</div>
{bande("bande-onduleurs.jpg", "Onduleurs solaires hybrides GSL ENERGY installés par GSL-ELEC", 1600, 383)}
</div></section>

<section class="section bg-pale" id="simulateur"><div class="container"><div class="row">
<div class="col stack" style="flex-basis:400px">
<span class="eyebrow">Simulateur d’économies</span>
<h2 class="h2">Combien pouvez-vous économiser chaque mois ?</h2>
<p style="font-size:17px;line-height:1.65;color:var(--texte)">Indiquez le montant moyen de votre facture d’électricité. Le simulateur estime la puissance solaire adaptée et l’économie possible. Votre étude personnalisée affinera ce résultat.</p>
<div class="card" style="gap:12px;padding:20px 22px"><div style="display:flex;gap:12px"><strong style="flex:0 0 52px;color:var(--vert-cta)">kWc</strong><span class="muted">La puissance de vos panneaux solaires.</span></div><div style="display:flex;gap:12px"><strong style="flex:0 0 52px;color:var(--vert-cta)">kWh</strong><span class="muted">L’énergie que vous consommez ou que vos batteries stockent.</span></div></div>
<a class="link-arrow" href="article-kwc-kwh.html">Comprendre le kWc et le kWh{ico("arrow", 16, 2.2)}</a>
</div>
<div class="col" style="flex-basis:520px">{simulateur()}</div>
</div></div></section>

<section class="section bg-nuit hero" id="hv">
<div class="deco-cercle" style="right:-240px;bottom:-300px;width:760px;height:760px;border:90px solid #0F4D2A" aria-hidden="true"></div>
<div class="container stack-l">
<div class="row" style="align-items:flex-start">
<div class="col stack" style="flex-basis:520px">
<span class="badge badge-orange" style="letter-spacing:.12em;text-transform:uppercase">Hôtels &amp; industries</span>
<h2 class="h2">Une énergie stable et continue, <span class="accent">même pendant les coupures.</span></h2>
<p class="lead">Nos batteries lithium haute tension stockent de grandes quantités d’énergie pour vos chambres, cuisines, chambres froides et machines. Associées à un onduleur hybride triphasé, elles prennent le relais du réseau sans interruption.</p>
</div>
<div class="col grid" style="flex-basis:380px;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px">
<div class="stat"><strong>200 kWc</strong><span>puissance solaire maximale</span></div>
<div class="stat"><strong>Sur mesure</strong><span>stockage dimensionné après étude</span></div>
<div class="stat"><strong>LiFePO4</strong><span>modules empilables et extensibles</span></div>
<div class="stat"><strong>À distance</strong><span>supervision depuis l’application</span></div>
</div>
</div>
{flow_figure()}
<div class="row" style="justify-content:space-between">
<ul class="check-list grid" style="flex:1 1 640px;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:14px 32px">
<li>{ico("check", 22, 2.4)}Capacité extensible au rythme de votre activité</li><li>{ico("check", 22, 2.4)}Meilleur rendement, moins de pertes et de chaleur</li>
<li>{ico("check", 22, 2.4)}Moins de gasoil pour vos groupes électrogènes</li><li>{ico("check", 22, 2.4)}Système de gestion (BMS) qui protège chaque cellule</li>
<li>{ico("check", 22, 2.4)}Armoires compactes, peu d’entretien</li><li>{ico("check", 22, 2.4)}Contrat de maintenance et suivi à distance</li>
</ul>
<a class="btn btn-orange" href="batteries-haute-tension.html">Découvrir l’offre pro{ARROW}</a>
</div>
</div></section>

<section class="section" id="equipements"><div class="container stack-l">
<div class="section-head"><div><span class="eyebrow">Nos équipements</span><h2 class="h2">Du matériel de qualité, expliqué simplement</h2></div>
<a class="link-arrow" href="equipements.html">Voir tout le catalogue{ico("arrow", 16, 2.2)}</a></div>
<div class="grid grid-fill">{eq}</div>
</div></section>

<section class="section bg-gris" id="etapes"><div class="container stack-l">
<div class="stack center" style="text-align:center"><span class="eyebrow">Comment ça marche</span><h2 class="h2" style="max-width:760px">Votre projet solaire en 6 étapes claires</h2></div>
<ol class="steps-mini">{sl}</ol>
<a class="link-arrow center" href="comment-ca-marche.html" style="align-self:center">Le détail de chaque étape{ico("arrow", 16, 2.2)}</a>
</div></section>

<section class="section"><div class="container grid grid-2">
<div class="card bg-creme" style="border:0;padding:clamp(26px,3.4vw,44px);gap:18px">
<span class="icon-box lg ib-orange">{ico("globe", 28)}</span>
<h2 style="font-size:clamp(24px,2.4vw,30px);font-weight:800">Vous vivez en France ou en Europe ?</h2>
<p style="color:#4A3F2A;font-size:16px">Équipez la maison familiale au Sénégal à distance. Votre interlocuteur est joignable en France sur WhatsApp, vous recevez les photos du chantier et pouvez suivre la production depuis votre téléphone.</p>
<a class="btn btn-sombre btn-s" style="align-self:flex-start" href="https://wa.me/33768026171?text=Bonjour%2C%20je%20souhaite%20%C3%A9quiper%20une%20maison%20au%20S%C3%A9n%C3%A9gal">{ico("wa", 18, 1.9)}WhatsApp France · {WA_TXT_AFF}</a>
</div>
<div class="card bg-pale" style="border:0;padding:clamp(26px,3.4vw,44px);gap:18px">
<span class="icon-box lg ib-vert">{ico("card", 28)}</span>
<h2 style="font-size:clamp(24px,2.4vw,30px);font-weight:800">Payez votre installation en plusieurs fois</h2>
<p style="color:var(--texte);font-size:16px">Le solaire ne doit pas être réservé à ceux qui peuvent tout payer d’un coup. Étalez le coût de votre installation : les modalités vous sont présentées clairement dans votre devis.</p>
<a class="btn btn-vert btn-s" style="align-self:flex-start" href="financement.html">Découvrir le financement{ico("arrow", 16, 2.2)}</a>
</div>
</div></section>

<section class="section" style="padding-top:0" id="realisations"><div class="container stack-l">
<div class="section-head"><div><span class="eyebrow">Nos réalisations</span><h2 class="h2">Des installations réelles, partout au Sénégal</h2></div>
<a class="link-arrow" href="realisations.html">Voir toutes les réalisations{ico("arrow", 16, 2.2)}</a></div>
<div class="grid grid-3">{rl}</div>
</div></section>

<section class="section bg-gris" id="conseils"><div class="container stack-l">
<div class="section-head"><div><span class="eyebrow">Conseils solaires</span><h2 class="h2">Bien comprendre avant de vous équiper</h2></div>
<a class="link-arrow" href="conseils.html">Tous les conseils{ico("arrow", 16, 2.2)}</a></div>
<div class="grid grid-3">
<a class="card card-media" href="article-kwc-kwh.html"><div style="height:170px;background:var(--vert-fonce);display:flex;align-items:center;justify-content:center;gap:18px;color:var(--orange-clair);font-size:34px;font-weight:800">kWc<span style="color:#fff;font-size:22px">≠</span>kWh</div><div class="card-body"><span class="small accent-orange" style="font-weight:600">Comprendre · 5 min</span><strong style="font-size:18px;line-height:1.35">kWc, kWh : comprendre votre installation solaire en 5 minutes</strong></div></a>
<a class="card card-media" href="conseils.html"><div style="height:170px;background:var(--creme-2);display:flex;align-items:center;justify-content:center;color:var(--orange-texte)">{ico("panel", 64, 1.3)}</div><div class="card-body"><span class="small accent-orange" style="font-weight:600">Entretien · 4 min</span><strong style="font-size:18px;line-height:1.35">Poussière et harmattan : bien nettoyer ses panneaux solaires</strong></div></a>
<a class="card card-media" href="conseils.html"><div style="height:170px;background:var(--vert-pale);display:flex;align-items:center;justify-content:center;color:var(--vert-cta)">{ico("battery", 64, 1.3)}</div><div class="card-body"><span class="small accent-orange" style="font-weight:600">Batteries · 6 min</span><strong style="font-size:18px;line-height:1.35">Batterie lithium ou plomb : laquelle choisir pour votre maison ?</strong></div></a>
</div>
</div></section>

<section class="section" id="faq"><div class="container row" style="align-items:flex-start">
<div class="col-s stack"><span class="eyebrow">Questions fréquentes</span><h2 class="h2">Tout savoir avant de passer au solaire</h2><p class="muted">Une autre question ? Écrivez-nous, nous répondons rapidement.</p><a class="link-arrow" href="faq.html">Voir toutes les questions{ico("arrow", 16, 2.2)}</a></div>
<div class="faq-list" style="flex:2 1 560px">{faq_items(FAQ_HOME, first_open=True)}</div>
</div></section>

<section class="section bg-vert hero" id="devis">
<div class="deco-cercle" style="left:-200px;top:-200px;width:600px;height:600px;background:var(--vert-cercle)" aria-hidden="true"></div>
<div class="container row" style="align-items:flex-start">
<div class="col-s stack" style="gap:22px">
<span class="eyebrow">Contactez-nous dès aujourd’hui</span>
<h2 class="h2">Parlons de votre projet solaire</h2>
<p class="lead">Disponibles partout au Sénégal. Réponse rapide par WhatsApp ou par téléphone.</p>
<a class="contact-tile on-dark" href="{WA}"><span class="icon-box ib-vert">{ico("wa", 24, 1.9)}</span><span><span class="lbl">WhatsApp (France)</span><strong>{WA_TXT_AFF}</strong></span></a>
<a class="contact-tile on-dark" href="{TEL}"><span class="icon-box ib-orange">{ico("phone", 24, 1.9)}</span><span><span class="lbl">Mobile (Sénégal)</span><strong>{TEL_TXT}</strong></span></a>
</div>
<div class="col" style="flex-basis:520px">{contact_form("h", short=False)}</div>
</div></section>
'''


def solutions():
    return f'''
<section class="page-hero bg-pale"><div class="container">
{crumbs(("Nos solutions", None))}
<h1 class="h1" style="max-width:900px">Des solutions solaires et électriques <span class="accent-vert">pour chaque besoin</span></h1>
<p class="lead">Maison, commerce, hôtel, industrie ou exploitation agricole : chaque projet commence par une étude de votre consommation réelle, pour installer la bonne puissance au bon prix.</p>
<div class="chips"><span class="chip" style="cursor:default"><span class="accent-vert">5 à 50 kWc</span>&nbsp;· maisons et commerces</span><span class="chip" style="cursor:default"><span class="accent-orange">Jusqu’à 200 kWc</span>&nbsp;· industries et hôtels</span><span class="chip" style="cursor:default">Partout au Sénégal</span></div>
</div></section>
<section class="section-tight" style="padding-bottom:0"><div class="container">{bande("bande-stockage.jpg", "Gamme de solutions de stockage d’énergie GSL-ELEC : batteries et armoires pour maisons, commerces, hôtels et industries", 1600, 577)}</div></section>
<section class="section"><div class="container stack-l"><div class="grid grid-3">{solution_cards()}</div>
{bande("bande-onduleurs.jpg", "Onduleurs solaires hybrides GSL ENERGY installés par GSL-ELEC", 1600, 383)}</div></section>
<section class="section bg-gris"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Comment choisir ?</span><h2 class="h2">Quelle installation correspond à votre situation ?</h2></div>
<div class="grid grid-3">
<div class="card"><span class="small muted" style="font-weight:600">Vous subissez des coupures ?</span><strong style="font-size:20px">Onduleur hybride + batteries</strong><p>Les batteries stockent l’énergie du jour et prennent le relais automatiquement pendant les coupures et la nuit.</p></div>
<div class="card"><span class="small muted" style="font-weight:600">Vous consommez surtout la journée ?</span><strong style="font-size:20px">Onduleur réseau, sans batterie</strong><p>La solution la plus économique pour réduire la facture des bureaux et commerces ouverts le jour.</p></div>
<div class="card"><span class="small muted" style="font-weight:600">Vous êtes loin du réseau ?</span><strong style="font-size:20px">Site autonome ou pompage solaire</strong><p>Panneaux, batteries ou pompe solaire : de l’énergie et de l’eau sans gasoil, même loin de tout.</p></div>
</div>
<div class="btns" style="align-items:center"><a class="btn btn-vert" href="contact.html">Demander une étude de charge{ARROW}</a><span class="muted small">Nous vous conseillons la solution adaptée, sans engagement.</span></div>
</div></section>
{cta_band()}'''


def service(key):
    d = SERVICE_DATA[key]
    title = d["title"]
    dark = key == "pro"
    hero_cls = "bg-vert" if dark else "bg-pale"
    icon = {"maison": "house", "pro": "factory", "pompage": "drop", "appareils": "snow", "maintenance": "shield", "electricite": "bolt"}[key]
    tabs = "".join(
        f'<a class="chip" style="white-space:nowrap;display:inline-flex;align-items:center" href="{h}"{" aria-current=\"page\" aria-selected=\"true\"" if k == key else ""}>{l}</a>'
        for k, l, h in SERVICES)
    who = "".join(f'<li style="background:var(--gris-fond);border-radius:14px;padding:12px 14px">{ico("check", 20, 2.4)}{w}</li>' for w in d["who"])
    ben = "".join(f'<div class="card card-soft"><span class="num" style="border-radius:12px">{i + 1}</span><strong style="font-size:17px">{t}</strong><p>{x}</p></div>' for i, (t, x) in enumerate(d["benefits"]))
    bars = ["var(--vert)", "var(--orange)", "var(--vert-fonce)"]
    ex = "".join(f'<div class="card card-media"><div style="height:10px;background:{bars[i % 3]}"></div><div class="card-body" style="padding:26px"><strong style="font-size:19px;line-height:1.3">{t}</strong><p>{x}</p></div></div>' for i, (t, x) in enumerate(d["examples"]))
    eqmap = {e["key"]: e for e in EQUIP}
    eqs = "".join(f'<a class="chip" style="display:inline-flex;align-items:center;gap:8px" href="{eqmap[k]["href"]}">{eqmap[k]["title"]}{ico("chev", 14, 2.4)}</a>' for k in d["equip"])
    pro_block = f'''<section style="padding-bottom:var(--section)"><div class="container"><a class="card bg-nuit" href="batteries-haute-tension.html" style="border:0;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:20px;padding:clamp(24px,3.4vw,44px);color:#fff">
<div class="stack" style="gap:8px;flex:1 1 420px"><span class="eyebrow">Notre offre phare</span><strong style="font-size:clamp(22px,2.2vw,30px);line-height:1.2">Batteries haute tension pour hôtels et industries</strong><span style="color:var(--sur-vert-2)">Une énergie stable et continue, même pendant les coupures.</span></div>
<span class="btn btn-orange btn-s">Découvrir{ico("arrow", 16, 2.2)}</span></a></div></section>''' if dark else ""
    return f'''
<section class="page-hero hero {hero_cls}">
<div class="deco-cercle" style="right:-160px;top:-180px;width:560px;height:560px;background:{"var(--vert-cercle)" if dark else "var(--vert-pale-2)"}" aria-hidden="true"></div>
<div class="container">
{crumbs(("Nos solutions", "solutions.html"), (title, None))}
<div class="row">
<div class="col stack" style="flex-basis:520px;gap:20px">
<span class="badge badge-orange">{d["badge"]}</span>
<h1 class="h1">{title}</h1>
<p class="lead">{d["lead"]}</p>
<div class="btns"><a class="btn btn-orange" href="contact.html?service={key}">Demander un devis{ARROW}</a><a class="btn {"btn-contour" if dark else "btn-contour-vert"}" href="https://wa.me/33768026171?text=Bonjour%2C%20je%20souhaite%20un%20devis%20%3A%20{title.replace(" ", "%20")}">{ico("wa", 20, 1.9)}En parler sur WhatsApp</a></div>
</div>
<div class="col-s"><div class="card" style="box-shadow:var(--ombre);gap:18px;border:0">
<div style="display:flex;align-items:center;gap:14px"><span class="icon-box lg ib-vert">{ico(icon, 32)}</span><strong style="font-size:18px;line-height:1.3">À qui s’adresse cette solution ?</strong></div>
<ul class="check-list">{who}</ul>
</div></div>
</div>
</div></section>
<div style="border-bottom:1px solid var(--bord)"><nav class="container scroller" aria-label="Nos six solutions" style="padding-top:14px;padding-bottom:14px;gap:8px">{tabs}</nav></div>
<section class="section"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Les avantages</span><h2 class="h2">Ce que vous y gagnez</h2></div>
<div class="grid grid-4">{ben}</div>
</div></section>
<section class="section" style="padding-top:0"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Exemples d’usage au Sénégal</span><h2 class="h2">Concrètement, ça donne quoi ?</h2></div>
<div class="grid grid-3">{ex}</div>
</div></section>
{pro_block}
<section class="section bg-pale"><div class="container row" style="align-items:flex-start">
<div class="col stack"><span class="eyebrow">Le matériel utilisé</span><h2 style="font-size:clamp(26px,2.8vw,36px);font-weight:800">Des équipements documentés et garantis</h2><div class="chips">{eqs}</div><p class="muted">Les marques, modèles et fiches techniques vous sont communiqués dans votre devis.</p></div>
<div class="col">{contact_form("s-" + key, short=True, service=key, service_title=title)}</div>
</div></section>
'''


def batteries():
    feats = [("stack", "ib-pale", "Grande capacité, extensible", "Ajoutez des modules au rythme de la croissance de votre activité."),
             ("bolt", "ib-pale", "Meilleur rendement", "À haute tension, le courant est plus faible : moins de pertes, moins de chaleur, un câblage plus léger."),
             ("snow", "ib-pale", "Continuité d’alimentation", "Chambres, climatisation, cuisines, chambres froides et machines sans coupure."),
             ("nogas", "ib-creme", "Moins de gasoil, facture réduite", "Vos groupes électrogènes tournent moins, et vous achetez moins d’énergie au réseau."),
             ("shield", "ib-pale", "Protection électronique (BMS)", "Le système de gestion surveille et protège chaque cellule, et remonte les alertes à distance."),
             ("square", "ib-pale", "Compact et durable", "Armoires peu encombrantes, longue durée de vie, très peu d’entretien.")]
    fh = "".join(f'<div class="card"><span class="icon-box {c}" style="width:48px;height:48px">{ico(i, 24)}</span><strong style="font-size:17px">{t}</strong><p>{x}</p></div>' for i, c, t, x in feats)
    apps = "".join(f'<span class="card" style="padding:16px;font-weight:600;font-size:15px">{a}</span>' for a in ["Grands hôtels et résidences", "Industries et ateliers", "Cliniques", "Supermarchés", "Chambres froides", "Sites agro-industriels"])
    th = ""
    reas = "".join(f'<div style="display:flex;gap:12px;align-items:center;font-weight:600;font-size:15px">{ico("check", 22, 2.4, extra=" style=\"color:var(--vert-cta);flex:0 0 22px\"")}{t}</div>' for t in ["Étude de charge préalable", "Matériel documenté et garanti", "Mise en service par GSL-ELEC", "Contrat de maintenance"])
    return f'''
<section class="page-hero hero bg-nuit" style="padding-bottom:clamp(48px,6vw,96px)">
<div class="deco-cercle" style="right:-220px;top:-260px;width:720px;height:720px;border:100px solid #0F4D2A" aria-hidden="true"></div>
<div class="container" style="gap:22px">
{crumbs(("Nos solutions", "solutions.html"), ("Batteries haute tension", None))}
<span class="badge badge-orange" style="letter-spacing:.12em;text-transform:uppercase">Hôtels &amp; industries</span>
<h1 class="h1" style="max-width:980px">Une énergie stable et continue pour votre hôtel ou votre usine, <span class="accent">même pendant les coupures.</span></h1>
<p class="lead">Nos batteries lithium haute tension, associées à un onduleur hybride triphasé, stockent de grandes quantités d’énergie solaire et alimentent vos équipements sans interruption.</p>
<div class="btns"><a class="btn btn-orange" href="#etude">Demander une étude pro{ARROW}</a><a class="btn btn-contour" href="https://wa.me/33768026171?text=Bonjour%2C%20je%20souhaite%20une%20%C3%A9tude%20batteries%20haute%20tension">{ico("wa", 20, 1.9)}WhatsApp</a></div>
<div class="grid grid-4" style="margin-top:12px;gap:12px">
<div class="stat"><strong>200 kWc</strong><span>puissance solaire maximale</span></div><div class="stat"><strong>64 à 209 kWh</strong><span>par armoire de stockage</span></div>
<div class="stat"><strong>≥ 10 000</strong><span>cycles de charge (BESS 80 kVA)</span></div><div class="stat"><strong>10 ans</strong><span>de garantie (selon modèle)</span></div>
</div>
</div></section>

<section class="section"><div class="container row">
<div class="col stack" style="flex-basis:480px">
<span class="eyebrow">Ce que c’est</span>
<h2 class="h2">Des modules lithium empilés, reliés pour fonctionner à haute tension</h2>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Une batterie haute tension réunit plusieurs modules lithium (LiFePO4) empilés et reliés en série pour fonctionner à plusieurs centaines de volts. Elle est associée à un onduleur hybride triphasé haute tension, qui gère les panneaux, les batteries, le réseau et le groupe électrogène.</p>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Résultat : un grand stockage d’énergie, compact, efficace et pilotable à distance — idéal pour les gros consommateurs.</p>
</div>
<div class="col-s"><figure class="card" style="margin:0;padding:20px;align-items:center;gap:10px"><img src="assets/img/p-bess-80kva.jpg" alt="Armoire de stockage haute tension GSL-BESS 80 kVA, portes ouvertes sur les modules de batteries" width="619" height="582" loading="lazy" style="width:100%;height:auto;max-width:440px"><figcaption class="small muted" style="text-align:center">GSL-BESS 80 kVA : onduleur, batteries et protections dans une seule armoire.</figcaption></figure></div>
</div></section>

<section class="section bg-pale"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Comment ça fonctionne</span><h2 class="h2">Du soleil à votre bâtiment, en 4 étapes</h2></div>
{flow_figure()}
</div></section>

<section class="section"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Les avantages</span><h2 class="h2">Pourquoi la haute tension pour les gros consommateurs ?</h2></div>
<div class="grid grid-3">{fh}</div>
</div></section>

<section class="section" style="padding-top:0"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Nos armoires de stockage</span><h2 class="h2">Deux gammes pour les gros consommateurs</h2></div>
{bess_cards()}
</div></section>
<section class="section bg-gris"><div class="container row" style="align-items:flex-start">
<div class="col stack"><span class="eyebrow">Applications</span><h2 style="font-size:clamp(26px,2.8vw,36px);font-weight:800">Pour qui ?</h2><div class="grid" style="grid-template-columns:repeat(2,minmax(0,1fr));gap:10px">{apps}</div></div>
<div class="col stack"><span class="eyebrow">Caractéristiques</span><h2 style="font-size:clamp(26px,2.8vw,36px);font-weight:800">Les chiffres clés</h2>
{spec_table([("Puissance solaire", "Jusqu’à 200 kWc"), ("Chimie", "Lithium fer phosphate (LiFePO4)"), ("Capacité des armoires", "64 à 209 kWh"), ("Tension", "Triphasé 380/400 V"), ("Durée de vie", "≥ 8 000 à ≥ 10 000 cycles"), ("Garantie", "10 ans (selon modèle)"), ("Certifications", "CE, IEC 62619, VDE, UN38.3")], "Fiches fabricant GSL ENERGY.")}
<a class="link-arrow" href="assets/docs/GSL-ELEC_Batteries_lithium.pdf" target="_blank" rel="noopener">{ico("download", 18, 2)}Télécharger la fiche technique (PDF)</a></div>
</div></section>

<section class="section-tight"><div class="container grid grid-4" style="gap:14px">{reas}</div></section>

<section class="section" id="etude" style="padding-top:clamp(24px,3vw,40px)"><div class="container row" style="align-items:flex-start">
<div class="col-s stack">
<span class="eyebrow">Demande d’étude pour professionnels</span>
<h2 class="h2">Parlez-nous de votre site</h2>
<p style="font-size:16px;color:var(--texte)">Ces informations nous permettent de préparer une première estimation avant la visite et l’étude de charge sur place.</p>
<div class="card bg-pale" style="border:0;gap:6px"><strong>Vous préférez en parler directement ?</strong><a href="{TEL}" style="font-weight:700;font-size:18px">{TEL_TXT}</a></div>
</div>
<div style="flex:2 1 560px;min-width:0">{pro_form()}</div>
</div></section>
'''


def pro_form():
    sect = "".join(f"<option>{s}</option>" for s in ["Hôtel / résidence", "Industrie / atelier", "Clinique / pharmacie", "Supermarché / commerce", "Chambre froide / agro-industrie", "Autre"])
    coup = "".join(f"<option>{s}</option>" for s in ["Rarement", "Moins d’1 h", "1 à 3 h", "3 à 6 h", "Plus de 6 h"])
    radios = "".join(f'<label><input type="radio" name="toit" value="{v}">{v}</label>' for v in ["Toit", "Terrain", "Parking (ombrière)", "À vérifier"])
    return f'''<form class="form-card" data-demo-form novalidate aria-label="Demande d’étude professionnelle">
<div class="form-fields stack" style="gap:16px">
<div class="form-grid">
<div class="field"><label for="p-soc">Société *</label><input class="input" id="p-soc" name="societe" type="text" placeholder="Nom de l’établissement" autocomplete="organization" data-required><span class="err-msg" data-err-for="p-soc">Indiquez le nom de votre société.</span></div>
<div class="field"><label for="p-sect">Secteur</label><select class="input" id="p-sect" name="secteur">{sect}</select></div>
<div class="field"><label for="p-ville">Ville</label><input class="input" id="p-ville" name="ville" type="text" placeholder="Saly, Thiès…" autocomplete="address-level2"></div>
<div class="field"><label for="p-nom">Nom du contact</label><input class="input" id="p-nom" name="nom" type="text" placeholder="Prénom et nom" autocomplete="name"></div>
<div class="field"><label for="p-tel">Téléphone *</label><input class="input" id="p-tel" name="telephone" type="tel" placeholder="+221 7X XXX XX XX" autocomplete="tel" data-required><span class="err-msg" data-err-for="p-tel">Indiquez un numéro de téléphone valide.</span></div>
<div class="field"><label for="p-mail">E-mail <span class="opt">(facultatif)</span></label><input class="input" id="p-mail" name="email" type="email" placeholder="contact@societe.sn" autocomplete="email"></div>
<div class="field"><label for="p-conso">Facture mensuelle (FCFA) ou consommation (kWh)</label><input class="input" id="p-conso" name="consommation" type="text" placeholder="Ex. 1 500 000 FCFA"></div>
<div class="field"><label for="p-groupe">Puissance du groupe électrogène (kVA)</label><input class="input" id="p-groupe" name="groupe" type="text" inputmode="numeric" placeholder="Ex. 100"></div>
<div class="field"><label for="p-coup">Heures de coupure par jour</label><select class="input" id="p-coup" name="coupures">{coup}</select></div>
</div>
<fieldset class="field"><legend style="margin-bottom:10px">Toit ou terrain disponible pour les panneaux ?</legend><div class="radio-pills">{radios}</div></fieldset>
<div class="field"><label for="p-msg">Précisions</label><textarea class="input" id="p-msg" name="message" rows="3" placeholder="Équipements critiques, horaires d’activité, projets d’extension…"></textarea></div>
<label class="consent" for="p-ok"><input id="p-ok" type="checkbox" data-required><span>J’accepte que GSL-ELEC utilise ces informations pour traiter ma demande, conformément à la <a href="mentions-legales.html#confidentialite">politique de confidentialité</a>.</span></label>
<span class="err-msg" data-err-for="p-ok">Merci de cocher cette case pour envoyer votre demande.</span>
<button class="btn btn-vert btn-bloc" type="submit">Demander mon étude{ARROW}</button>
</div>
<div class="success" role="status"><span class="tick">{ico("check", 40, 2.4)}</span><strong>Demande d’étude bien reçue</strong><p>Un responsable vous contacte pour organiser la visite de votre site et l’étude de charge.</p><button class="btn btn-contour-vert btn-s" type="button" data-reset-form>Envoyer une autre demande</button></div>
</form>'''
