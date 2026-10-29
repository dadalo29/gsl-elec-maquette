"""Équipements, fiches, étapes, réalisations, financement, à propos, conseils, article, FAQ, contact, mentions."""
from common import ico, ARROW, WA, TEL, TEL_TXT, WA_TXT_AFF, MAIL, cta_band, crumbs
from data import EQUIP, TINT, FAQ_ALL, equip_card, faq_items, contact_form


def chips(group, cats, word):
    b = "".join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if i == 0 else "false"}">{l}</button>' for i, (k, l) in enumerate(cats))
    return f'<div class="chips" role="group" aria-label="Filtrer" data-filter-group="{group}">{b}</div>'


def hero_pale(label, h1, lead, extra=""):
    return f'''<section class="page-hero bg-pale"><div class="container">
{crumbs((label, None))}
<h1 class="h1" style="max-width:900px">{h1}</h1>
<p class="lead">{lead}</p>{extra}
</div></section>'''


def equipements():
    cats = [("tous", "Tous"), ("maison", "Maison"), ("commerce", "Commerce"), ("pro", "Industrie & hôtel"), ("agri", "Agriculture")]
    cards = "".join(equip_card(e) for e in EQUIP)
    return hero_pale("Nos équipements", 'Du matériel de qualité, <span class="accent-vert">expliqué simplement</span>',
                     "Découvrez les équipements que nous installons, à quoi ils servent et pour qui ils sont faits. Chaque fiche technique est disponible au téléchargement.") + f'''
<section class="section-tight"><div class="container stack-l">
<div style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px">{chips("equip-grid", cats, "équipement")}<span class="small muted" data-count-for="equip-grid" data-word="équipement" aria-live="polite">{len(EQUIP)} équipements</span></div>
<div class="grid grid-fill" id="equip-grid">{cards}</div>
<a class="card bg-nuit" href="batteries-haute-tension.html" style="border:0;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:18px;color:#fff;padding:clamp(22px,3vw,40px)">
<div class="stack" style="gap:6px;flex:1 1 420px"><span class="eyebrow">Hôtels et industries</span><strong style="font-size:clamp(21px,2vw,28px);line-height:1.25">Tout savoir sur les batteries haute tension</strong></div>
<span class="btn btn-orange btn-s">Découvrir la page dédiée</span></a>
<p class="small muted">Les marques et modèles exacts vous sont communiqués dans votre devis. Tous nos équipements sont livrés avec leur fiche technique et leurs conditions de garantie.</p>
</div></section>
{cta_band()}'''


def fiche(e):
    bg, ink = TINT[e["t"]]
    uses = "".join(f'<span class="tag">{u}</span>' for u in e["uses"])
    pros = "".join(f'<li>{ico("check", 22, 2.4)}{p}</li>' for p in e["pros"])
    others = "".join(f'<a class="chip" style="display:inline-flex;align-items:center" href="{o["href"]}">{o["title"]}</a>' for o in EQUIP if o["key"] != e["key"])
    hv = '<a class="link-arrow" href="batteries-haute-tension.html">Voir la page complète sur les batteries haute tension' + ico("arrow", 16, 2.2) + '</a>' if e["key"] == "batteries-haute-tension" else ""
    return f'''
<section class="section-tight"><div class="container stack-l">
{crumbs(("Nos équipements", "equipements.html"), (e["title"], None))}
<div class="row" style="align-items:flex-start">
<div class="col" style="flex-basis:440px"><div style="aspect-ratio:1/1;max-height:520px;border-radius:var(--rayon-xl);background:{bg};color:{ink};display:flex;align-items:center;justify-content:center;position:relative">{ico(e["icon"], 160, 0.9)}
<span style="position:absolute;bottom:18px;left:18px;right:18px;text-align:center;background:rgba(255,255,255,.92);color:var(--texte);border-radius:12px;padding:8px 12px;font-size:12.5px;font-weight:600">Photo produit fournie par GSL-ELEC</span></div></div>
<div class="col stack" style="flex-basis:460px;gap:20px">
<span class="badge badge-vert">Pour : {e["who"]}</span>
<h1 class="h1" style="font-size:clamp(30px,3.8vw,50px)">{e["title"]}</h1>
<p class="lead">{e["long"]}</p>
<div class="stack" style="gap:10px"><strong>Usages</strong><div class="chips">{uses}</div></div>
<ul class="check-list">{pros}</ul>
<dl class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:12px;margin:0">
<div class="card card-soft" style="padding:14px 16px;gap:4px"><dt class="small muted">Gammes disponibles</dt><dd style="margin:0;font-weight:600">{e["range"]}</dd></div>
<div class="card card-soft" style="padding:14px 16px;gap:4px"><dt class="small muted">Garantie</dt><dd class="todo" style="margin:0">Selon fiche fabricant</dd></div>
</dl>
<div class="btns"><a class="btn btn-vert" href="contact.html">Demander un devis{ARROW}</a><a class="btn btn-contour-vert" href="#" aria-disabled="true">{ico("download", 18, 2)}Fiche technique (PDF)</a></div>
{hv}
</div>
</div>
</div></section>
<section class="section-tight bg-gris"><div class="container stack">
<h2 style="font-size:clamp(24px,2.4vw,32px);font-weight:800">Les autres équipements</h2>
<div class="chips">{others}</div>
<a class="link-arrow" href="equipements.html">Retour au catalogue{ico("arrow", 16, 2.2)}</a>
</div></section>
{cta_band()}'''


def etapes():
    S = [("Prise de contact", "Vous nous écrivez sur WhatsApp, nous appelez ou remplissez le formulaire. Nous échangeons sur votre besoin : appareils, coupures, facture, toit ou terrain disponible.", "un premier avis et un rendez-vous de visite"),
         ("Visite et étude de charge", "Un technicien se rend sur place pour relever vos appareils, leurs puissances et leurs horaires d’utilisation, et vérifier l’emplacement des panneaux.", "le calcul de votre besoin réel en énergie"),
         ("Devis détaillé", "Nous vous proposons la puissance adaptée, le matériel précis (marques, modèles, garanties) et les modalités de paiement, y compris en plusieurs fois.", "un devis clair, poste par poste, en FCFA"),
         ("Installation", "Nos équipes posent les structures, les panneaux, l’onduleur, les batteries et toutes les protections électriques, dans le respect des règles de sécurité.", "des photos du chantier à chaque étape"),
         ("Mise en service et explications", "Nous testons et réglons l’installation, puis nous vous montrons comment l’utiliser et la suivre sur votre téléphone.", "les fiches techniques, garanties et un guide simple"),
         ("Suivi et SAV", "Supervision à distance, visites d’entretien, nettoyage et dépannage : nous restons à vos côtés tout au long de la vie de l’installation.", "un contrat de maintenance adapté, si vous le souhaitez")]
    li = "".join(f'''<li><div class="rail"><span class="num{" o" if i == 5 else ""}">{i + 1}</span><i></i></div><div class="content"><h2>{t}</h2><p>{d}</p><div class="receive">{ico("doc", 18, 2.2)}<span><strong>Vous recevez :</strong> {r}</span></div></div></li>''' for i, (t, d, r) in enumerate(S))
    return hero_pale("Comment ça marche", 'Votre projet solaire, <span class="accent-vert">étape par étape</span>',
                     "Un processus clair, du premier message jusqu’au suivi de votre installation. Vous savez toujours où en est votre projet.") + f'''
<section class="section"><div class="container-narrow"><ol class="timeline">{li}</ol></div></section>
<section style="padding-bottom:clamp(24px,4vw,48px)"><div class="container"><div class="card bg-creme" style="border:0;flex-direction:row;flex-wrap:wrap;align-items:center;gap:24px;padding:clamp(24px,3.4vw,48px)">
<span class="icon-box lg ib-orange">{ico("globe", 32)}</span>
<div class="stack" style="gap:8px;flex:1 1 420px"><strong style="font-size:clamp(20px,2vw,26px)">Vous vivez en France ou en Europe ?</strong><p style="color:#4A3F2A">Les mêmes étapes, à distance : échanges sur WhatsApp, visite réalisée avec votre famille sur place, photos du chantier à chaque étape et suivi de la production depuis votre téléphone.</p></div>
<a class="btn btn-sombre btn-s" href="https://wa.me/33768026171?text=Bonjour%2C%20je%20vis%20%C3%A0%20l%27%C3%A9tranger%20et%20je%20souhaite%20%C3%A9quiper%20une%20maison">WhatsApp France</a>
</div></div></section>
{cta_band()}'''


def realisations():
    R = [("maison", "Maison", "Villa familiale", "Particulier", "Hybride + lithium", False), ("pro", "Hôtel", "Hôtel en bord de mer", "Hôtellerie", "Batteries HT", True),
         ("agri", "Agriculture", "Forage maraîcher", "Exploitation", "Pompe immergée", False), ("commerce", "Commerce", "Boutique de quartier", "Commerçant", "Hybride + lithium", False),
         ("pro", "Industrie", "Atelier de production", "Industrie", "Onduleur triphasé", True), ("maison", "Diaspora", "Maison familiale à distance", "Diaspora", "Hybride + supervision", False)]
    cards = "".join(f'''<article class="card card-media" data-tags="{f}"><div class="placeholder ratio-43{" orange" if o else ""}">{ico("image", 44, 1.4)}Photo du chantier</div>
<div class="card-body" style="padding:22px 24px;gap:14px"><span class="badge badge-vert">{c}</span><h2 style="font-size:19px;font-weight:700;letter-spacing:0">{t}</h2>
<dl class="grid" style="grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 14px;margin:0;font-size:13.5px">
<div><dt class="muted">Lieu</dt><dd class="todo" style="margin:2px 0 0">[Ville]</dd></div><div><dt class="muted">Client</dt><dd style="margin:2px 0 0;font-weight:600">{cl}</dd></div>
<div><dt class="muted">Puissance</dt><dd class="todo" style="margin:2px 0 0">[X] kWc</dd></div><div><dt class="muted">Matériel</dt><dd style="margin:2px 0 0;font-weight:600">{m}</dd></div></dl></div></article>''' for f, c, t, cl, m, o in R)
    quote = f'''<figure class="card" style="margin:0"><span style="color:var(--orange)">{ico("star", 28, 2)}</span><blockquote style="margin:0;font-size:16px;line-height:1.65;color:var(--texte)" class="todo">[Témoignage du client, publié avec son accord.]</blockquote><figcaption style="font-weight:600;font-size:14px">[Prénom N.] · <span class="muted" style="font-weight:400">[Ville]</span></figcaption></figure>'''
    cats = [("tous", "Toutes"), ("maison", "Maisons"), ("commerce", "Commerces"), ("pro", "Hôtels & industrie"), ("agri", "Agriculture")]
    return hero_pale("Réalisations", 'Nos installations <span class="accent-vert">au Sénégal</span>',
                     "Maisons, commerces, hôtels, exploitations agricoles : découvrez nos chantiers, avec pour chacun le lieu, le type de client, la puissance installée et le matériel utilisé.",
                     '<p class="tiny" style="background:var(--creme);border-radius:12px;padding:10px 14px;align-self:flex-start;color:#4A3F2A">Page prête, masquée au lancement : elle sera publiée dès les premiers chantiers photographiés.</p>') + f'''
<section class="section-tight"><div class="container stack-l">{chips("real-grid", cats, "réalisation")}<div class="grid grid-3" id="real-grid">{cards}</div></div></section>
<section class="section bg-gris"><div class="container stack-l">
<div class="section-head"><div><span class="eyebrow">Avis clients</span><h2 class="h2">Ils nous ont fait confiance</h2></div><a class="link-arrow" href="#">Voir les avis sur Google{ico("arrow", 16, 2.2)}</a></div>
<div class="grid grid-3">{quote * 3}</div>
</div></section>
{cta_band()}'''


def financement():
    return f'''
<section class="page-hero bg-creme"><div class="container"><div class="row">
<div class="col stack" style="flex-basis:520px">
{crumbs(("Financement", None))}
<h1 class="h1">Passez au solaire, <span class="accent-orange">payez en plusieurs fois</span></h1>
<p class="lead" style="color:#4A3F2A">Le solaire ne doit pas être réservé à ceux qui peuvent tout payer d’un coup. Étalez le coût de votre installation, pendant que votre facture d’électricité baisse.</p>
<a class="btn btn-vert" style="align-self:flex-start" href="contact.html">Demander un devis avec paiement échelonné{ARROW}</a>
</div>
<div class="col-s"><div class="card" style="border:0;box-shadow:var(--ombre);gap:14px">
<strong style="font-size:18px">Exemple de paiement</strong>
<div style="display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid #F1E6CC;padding-bottom:12px"><span class="muted">Montant de l’installation</span><strong class="todo">[X] FCFA</strong></div>
<div style="display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid #F1E6CC;padding-bottom:12px"><span class="muted">Premier versement</span><strong class="todo">[Y] FCFA</strong></div>
<div style="display:flex;justify-content:space-between;gap:12px;border-bottom:1px solid #F1E6CC;padding-bottom:12px"><span class="muted">Nombre d’échéances</span><strong class="todo">[N] mois</strong></div>
<div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px"><span style="font-weight:600">Mensualité</span><strong style="font-size:28px;font-weight:800;color:var(--vert-cta)">[Z] FCFA</strong></div>
<span class="tiny muted">Exemple indicatif. Conditions définies par GSL-ELEC et précisées dans chaque devis.</span>
</div></div>
</div></div></section>
<section class="section"><div class="container stack-l">
<div class="stack" style="max-width:720px"><span class="eyebrow">Le principe</span><h2 class="h2">Simple, transparent, sans surprise</h2></div>
<div class="grid grid-3">
<div class="card card-soft"><span class="num">1</span><strong style="font-size:19px">Étude et devis</strong><p>Nous dimensionnons votre installation et vous présentons le prix total et l’échéancier proposé.</p></div>
<div class="card card-soft"><span class="num">2</span><strong style="font-size:19px">Premier versement</strong><p>Un premier versement au démarrage permet de lancer la commande du matériel et l’installation.</p></div>
<div class="card card-soft"><span class="num o">3</span><strong style="font-size:19px">Échéances mensuelles</strong><p>Vous réglez le solde en plusieurs fois, pendant que votre installation réduit déjà votre facture.</p></div>
</div></div></section>
<section class="section bg-vert"><div class="container row">
<div class="col stack" style="flex-basis:480px"><h2 class="h2">Vos économies aident à payer <span class="accent">vos mensualités</span></h2>
<p class="lead">Dès la mise en service, vous achetez moins d’électricité au réseau. Une partie de la somme que vous payiez chaque mois peut ainsi servir à régler votre installation.</p>
<a class="btn btn-orange btn-s" style="align-self:flex-start" href="index.html#simulateur">Estimer mes économies</a></div>
<div class="col-s stack" style="gap:12px">
<div class="stat" style="flex-direction:row;justify-content:space-between;align-items:center"><span>Facture avant</span><strong style="color:#fff">45 000 FCFA</strong></div>
<div class="stat" style="flex-direction:row;justify-content:space-between;align-items:center"><span>Facture après</span><strong>15 000 FCFA</strong></div>
<span class="tiny" style="color:var(--sur-vert-2)">Exemple indicatif — les économies réelles dépendent de chaque installation.</span></div>
</div></section>
<section class="section" style="padding-bottom:0"><div class="container-narrow stack">
<h2 style="font-size:clamp(26px,2.8vw,36px);font-weight:800;margin-bottom:8px">Questions sur le financement</h2>
<div class="card" style="gap:6px"><strong>Qui peut payer en plusieurs fois ?</strong><p>Les particuliers comme les professionnels. Les conditions sont étudiées pour chaque projet et précisées dans le devis.</p></div>
<div class="card" style="gap:6px"><strong>Quels documents fournir ?</strong><p class="todo">[Liste à fournir par GSL-ELEC : pièce d’identité, justificatif de domicile…]</p></div>
<div class="card" style="gap:6px"><strong>La diaspora peut-elle payer depuis l’étranger ?</strong><p class="todo">[Moyens de paiement acceptés à préciser par GSL-ELEC.]</p></div>
</div></section>
{cta_band()}'''


def apropos():
    vals = [("eye", "ib-pale", "Transparence", "Des devis clairs, du matériel documenté, des économies présentées honnêtement."),
            ("shield", "ib-pale", "Qualité", "Du matériel garanti, une pose soignée et des protections électriques complètes."),
            ("pin", "ib-creme", "Proximité", "Une équipe locale, joignable facilement par téléphone et sur WhatsApp."),
            ("headset", "ib-pale", "Accompagnement", "De l’étude au SAV, nous restons à vos côtés dans la durée.")]
    vh = "".join(f'<div class="card"><span class="icon-box {c}" style="width:48px;height:48px">{ico(i, 24)}</span><strong style="font-size:17px">{t}</strong><p>{d}</p></div>' for i, c, t, d in vals)
    regs = "".join(f'<span class="badge badge-vert" style="font-weight:600;font-size:14px;padding:9px 15px">{r}</span>' for r in ["Dakar", "Thiès", "Diourbel", "Fatick", "Kaolack", "Kaffrine", "Louga", "Saint-Louis", "Matam", "Tambacounda", "Kédougou", "Kolda", "Sédhiou", "Ziguinchor"])
    return f'''
<section class="page-hero hero bg-vert"><div class="deco-cercle" style="right:-160px;bottom:-220px;width:560px;height:560px;background:var(--vert-cercle)" aria-hidden="true"></div><div class="container">
{crumbs(("À propos", None))}
<h1 class="h1" style="max-width:960px">Rendre l’énergie solaire <span class="accent">accessible à tous</span> au Sénégal</h1>
<p class="lead">GSL-ELEC — Gestion Solaire Locale et Électricité — aide les familles, les commerces et les entreprises à produire, stocker et économiser leur énergie.</p>
</div></section>
<section class="section"><div class="container row" style="align-items:flex-start">
<div class="col-s stack" style="gap:16px">
<figure style="margin:0;border-radius:var(--rayon-xl);overflow:hidden;background:var(--vert-pale);box-shadow:var(--ombre)">
<img src="assets/img/fondateur-bathie-sarr.jpg" alt="Bathie SARR, fondateur de GSL-ELEC, en uniforme d’officier sur le pont d’un bateau solaire" width="900" height="1048" loading="lazy" style="width:100%;height:auto">
</figure>
<div class="card" style="gap:12px">
<div class="stack" style="gap:2px"><strong style="font-size:20px">Bathie SARR</strong><span class="small muted">Fondateur de GSL-ELEC</span></div>
<ul class="check-list" style="gap:10px">
<li>{ico("check", 22, 2.4)}<span><strong>Officier</strong> de la marine marchande</span></li>
<li>{ico("check", 22, 2.4)}<span><strong>Ingénieur</strong> éco-gestion du navire</span></li>
<li>{ico("check", 22, 2.4)}<span><strong>Ingénieur énergie</strong> à bord du Porrima (ex-PlanetSolar)</span></li>
</ul>
</div>
</div>
<div class="col stack" style="flex-basis:560px;gap:22px">
<span class="eyebrow">Notre histoire</span>
<h2 class="h2">Du solaire en mer au solaire chez vous</h2>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">GSL-ELEC est née d’un constat simple : les factures d’électricité pèsent lourd sur les familles et les entreprises, et les coupures freinent l’activité. Le soleil, lui, est là toute l’année.</p>
<div class="stack" style="gap:10px">
<h3 class="h3">Une formation d’officier et d’ingénieur</h3>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Notre fondateur est officier de la marine marchande et ingénieur en éco-gestion du navire. Cette formation d’ingénieur, proposée par l’École nationale supérieure maritime (ENSM), apprend à exploiter un navire de façon propre et économe : réduire la consommation d’énergie et de carburant, optimiser les installations électriques et la propulsion, intégrer des énergies renouvelables à bord et suivre les performances environnementales. Sur un navire, chaque kilowattheure compte, et il faut produire, stocker et distribuer l’énergie sans jamais tomber en panne.</p>
</div>
<div class="stack" style="gap:10px">
<h3 class="h3">Ingénieur énergie sur un bateau 100&nbsp;% solaire</h3>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Il a ensuite travaillé comme ingénieur en gestion d’énergie à bord du Porrima, anciennement PlanetSolar. Ce catamaran est le premier bateau à avoir fait le tour du monde uniquement à l’énergie solaire, entre 2010 et 2012, avec plus de 500 m² de panneaux et plusieurs tonnes de batteries lithium.</p>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Son rôle : suivre la production des panneaux, gérer la charge et la décharge des batteries, répartir la puissance entre la propulsion et les équipements de bord, anticiper les besoins selon la météo et la route, et assurer la maintenance. En mer, le solaire n’est pas un complément : c’est la seule source d’énergie.</p>
</div>
<div class="stack" style="gap:10px">
<h3 class="h3">Pourquoi GSL-ELEC</h3>
<p style="font-size:16.5px;line-height:1.75;color:var(--texte)">Si un navire peut traverser les océans grâce au soleil, une maison, un commerce ou un hôtel au Sénégal peuvent aussi réduire leur facture et gagner en autonomie. GSL-ELEC applique la même méthode : bien mesurer les besoins, choisir du matériel fiable et dimensionner chaque installation au plus juste.</p>
</div>
<div class="card bg-creme" style="border:0;flex-direction:row;gap:14px;align-items:flex-start"><span class="icon-box ib-orange" style="width:44px;height:44px;border-radius:12px">{ico("globe", 22)}</span><p style="color:#4A3F2A;font-size:15.5px">Joignable à la fois en France et au Sénégal, notre fondateur accompagne aussi la diaspora qui souhaite équiper la maison familiale à distance : échanges sur WhatsApp, visite et installation sur place, suivi de la production sur téléphone.</p></div>
</div>
</div></section>
<section class="section bg-vert hero" style="padding:clamp(48px,6vw,88px) 0"><div class="deco-cercle" style="left:-160px;top:-200px;width:520px;height:520px;background:var(--vert-cercle)" aria-hidden="true"></div><div class="container-narrow" style="position:relative">
<figure style="margin:0;display:flex;flex-direction:column;gap:20px;text-align:center;align-items:center">
<blockquote style="margin:0;font-size:clamp(24px,3vw,38px);line-height:1.25;font-weight:800;letter-spacing:-0.015em;max-width:24ch">« Produire, stocker et économiser : l’énergie solaire, <span class="accent">pensée comme à bord.</span> »</blockquote>
<figcaption style="color:var(--sur-vert);font-size:15px"><strong style="color:#fff">Bathie SARR</strong>, fondateur de GSL-ELEC</figcaption>
</figure>
</div></section>
<section class="section bg-gris"><div class="container stack-l"><div class="stack"><span class="eyebrow">Nos valeurs</span><h2 class="h2">Ce qui guide notre travail</h2></div><div class="grid grid-4">{vh}</div></div></section>
<section class="section"><div class="container row" style="align-items:flex-start">
<div class="col-s stack"><span class="eyebrow">Zone d’intervention</span><h2 class="h2">Partout au Sénégal</h2><p style="color:var(--texte)">Nous intervenons dans toutes les régions du pays, de Dakar à Ziguinchor, pour les particuliers comme pour les professionnels.</p></div>
<div class="col chips" style="flex-basis:520px">{regs}</div>
</div>
<div class="container" style="margin-top:clamp(40px,5vw,72px)"><div class="card" style="border:2px solid var(--vert);flex-direction:row;flex-wrap:wrap;align-items:center;gap:24px;padding:clamp(24px,3.4vw,44px)">
<span class="icon-box lg ib-vert">{ico("doc", 32)}</span>
<div class="stack" style="gap:8px;flex:1 1 420px"><strong style="font-size:clamp(20px,2vw,26px)">Notre engagement qualité</strong><p>Étude de charge avant chaque installation, matériel documenté avec fiches techniques et garanties, mise en service expliquée, suivi et SAV.</p></div>
</div></div>
</section>
{cta_band()}'''


ARTICLES = [
    ("entretien", "Entretien", "4 min", "panel", "o", "Poussière et harmattan : bien nettoyer ses panneaux solaires", "Quand et comment nettoyer vos panneaux pour retrouver toute leur production, sans les abîmer."),
    ("batteries", "Batteries", "6 min", "battery", "g", "Batterie lithium ou plomb : laquelle choisir pour votre maison ?", "Durée de vie, entretien, profondeur de décharge : les différences qui comptent vraiment."),
    ("comprendre", "Comprendre", "5 min", "bolt", "d", "Coupures de courant : comment rester alimenté avec le solaire", "Onduleur hybride, batteries, bascule automatique : ce qui se passe quand le réseau s’arrête."),
    ("agriculture", "Agriculture", "5 min", "drop", "g", "Pompage solaire : en finir avec le gasoil pour irriguer", "Comment fonctionne une pompe solaire et comment la dimensionner pour votre forage."),
    ("economies", "Économies", "4 min", "snow", "o", "Climatiseur inverter : pourquoi il consomme moins", "Le principe de l’inverter expliqué simplement, et son impact sur la taille de votre installation."),
    ("comprendre", "Diaspora", "4 min", "globe", "g", "Équiper la maison familiale au Sénégal depuis la France", "Étapes, suivi du chantier et supervision à distance : comment ça se passe concrètement."),
]


def conseils():
    cards = "".join(f'''<a class="card card-media" href="article-kwc-kwh.html" data-tags="{f}"><div style="height:180px;background:{TINT[t][0]};color:{TINT[t][1]};display:flex;align-items:center;justify-content:center">{ico(i, 64, 1.3)}</div>
<div class="card-body"><span class="small accent-orange" style="font-weight:600">{c} · {m}</span><h2 style="font-size:18px;line-height:1.35;font-weight:700;letter-spacing:0">{ti}</h2><p style="font-size:14.5px">{ex}</p><span class="more" style="font-size:14.5px">Lire le conseil{ico("arrow", 15, 2.2)}</span></div></a>''' for f, c, m, i, t, ti, ex in ARTICLES)
    cats = [("tous", "Tous"), ("comprendre", "Comprendre"), ("batteries", "Batteries"), ("entretien", "Entretien"), ("economies", "Économies"), ("agriculture", "Agriculture")]
    return hero_pale("Conseils", 'Conseils solaires, <span class="accent-vert">simplement expliqués</span>',
                     "Comprendre son installation, bien l’entretenir, choisir ses batteries : nos guides pour vous aider à faire les bons choix.") + f'''
<section class="section-tight"><div class="container stack-l">
<a class="card card-media" href="article-kwc-kwh.html" style="flex-direction:row;flex-wrap:wrap">
<div style="flex:1 1 420px;min-height:260px;background:var(--vert-fonce);display:flex;align-items:center;justify-content:center;gap:20px;color:var(--orange-clair);font-size:clamp(40px,5vw,64px);font-weight:800">kWc<span style="color:#fff;font-size:.6em">≠</span>kWh</div>
<div class="stack" style="flex:1 1 420px;padding:clamp(24px,3.4vw,48px);justify-content:center;gap:14px"><span class="badge badge-orange">À la une</span><h2 style="font-size:clamp(24px,2.6vw,34px);line-height:1.2;font-weight:800">kWc, kWh : comprendre votre installation solaire en 5 minutes</h2><p class="muted">Puissance, énergie, production, stockage : les quatre notions à connaître avant de demander un devis.</p><span class="small muted">Comprendre · 5 min de lecture</span></div></a>
{chips("blog-grid", cats, "article")}
<div class="grid grid-3" id="blog-grid">{cards}</div>
<p class="tiny muted">Les articles autres que « kWc, kWh » sont des sujets proposés : ils renvoient pour l’instant vers l’article modèle.</p>
</div></section>
{cta_band()}'''


def article():
    return f'''
<article>
<header class="section-tight" style="padding-bottom:clamp(24px,3vw,40px)"><div class="container stack">
{crumbs(("Conseils", "conseils.html"), ("kWc et kWh", None))}
<h1 class="h1" style="font-size:clamp(30px,4.2vw,56px);max-width:960px">kWc, kWh : comprendre votre installation solaire en 5 minutes</h1>
<div style="display:flex;flex-wrap:wrap;gap:8px 18px" class="small muted"><span class="accent-orange" style="font-weight:600">Comprendre</span><span>5 min de lecture</span><span>Par l’équipe GSL-ELEC</span></div>
</div></header>
<div class="container"><div style="border-radius:clamp(20px,2.4vw,32px);background:var(--vert-fonce);min-height:clamp(180px,22vw,340px);display:flex;align-items:center;justify-content:center;gap:clamp(14px,2vw,32px);color:var(--orange-clair);font-size:clamp(44px,7vw,104px);font-weight:800" role="img" aria-label="kWc n’est pas égal à kWh">kWc<span style="color:#fff;font-size:.55em">≠</span>kWh</div></div>
<div class="container row section-tight" style="align-items:flex-start">
<div class="prose" style="flex:1 1 600px;min-width:0">
<p class="intro">Avant de demander un devis solaire, deux unités reviennent sans cesse : le kWc et le kWh. Elles se ressemblent, mais ne mesurent pas du tout la même chose. Voici l’essentiel, sans jargon.</p>
<h2>1. Le kWc : la puissance de vos panneaux</h2>
<p>Le kilowatt-crête (kWc) indique la puissance maximale que vos panneaux peuvent fournir dans des conditions de test standardisées : un ensoleillement de 1 000 W/m² et une température de cellule de 25 °C. C’est la « taille » de votre installation.</p>
<p>Exemple : 10 panneaux de 500 Wc forment une installation de 5 kWc.</p>
<h2>2. Le kWh : l’énergie que vous consommez</h2>
<p>Le kilowattheure (kWh) mesure une quantité d’énergie : une puissance utilisée pendant une durée. Un appareil de 1 000 W qui fonctionne une heure consomme 1 kWh ; un ventilateur de 50 W allumé 10 heures consomme 0,5 kWh. C’est l’unité de votre facture d’électricité.</p>
<div class="grid grid-2" style="gap:14px">
<div class="card bg-creme" style="border:0;gap:8px"><strong style="font-size:22px;color:var(--orange-texte)">kWc</strong><p style="color:#4A3F2A">C’est le <strong>débit du robinet</strong> : la quantité d’électricité que vos panneaux peuvent produire à un instant donné.</p></div>
<div class="card bg-pale" style="border:0;gap:8px"><strong style="font-size:22px;color:var(--vert-cta)">kWh</strong><p style="color:#2F4238">C’est <strong>l’eau dans le seau</strong> : la quantité d’énergie produite, consommée ou stockée sur une durée.</p></div>
</div>
<h2>3. Combien produit 1 kWc au Sénégal ?</h2>
<p>Grâce à un ensoleillement important toute l’année, 1 kWc bien installé produit en moyenne autour de 4 à 5 kWh par jour au Sénégal, soit environ 120 à 150 kWh par mois. Ce chiffre varie selon l’orientation et l’inclinaison des panneaux, la saison et leur propreté.</p>
<h2>4. Et les batteries ?</h2>
<p>La capacité d’une batterie s’exprime en kWh. En théorie, une batterie de 10 kWh peut alimenter des appareils totalisant 1 000 W pendant 10 heures. En pratique, on garde une réserve pour préserver la batterie et il y a de légères pertes : comptez un peu moins.</p>
<aside class="callout"><span class="icon-box ib-orange" style="width:44px;height:44px;border-radius:12px">{ico("bulb", 22, 2)}</span><span><strong>Notre conseil :</strong> réduisez d’abord vos besoins (LED, climatiseur inverter, froid économe). Chaque kWh économisé, c’est moins de panneaux et de batteries à acheter.</span></aside>
<h2>5. Comment dimensionne-t-on votre installation ?</h2>
<p>C’est le rôle de l’étude de charge : nous listons vos appareils, leur puissance et leurs heures d’utilisation. On obtient votre besoin en kWh par jour, puis on en déduit la puissance de panneaux (kWc) et la capacité de batteries (kWh) adaptées.</p>
<div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px;border-top:1px solid var(--bord);padding-top:20px;margin-top:12px">
<strong class="small">Partager :</strong>
<a class="chip" style="display:inline-flex;align-items:center" href="https://wa.me/?text=kWc%2C%20kWh%20%3A%20comprendre%20votre%20installation%20solaire">WhatsApp</a>
<a class="chip" style="display:inline-flex;align-items:center" href="#">Facebook</a>
</div>
</div>
<aside aria-label="À lire aussi" class="stack" style="flex:1 1 300px;min-width:0">
<div class="card bg-pale" style="border:0"><strong style="font-size:19px;line-height:1.3">Combien pourriez-vous économiser ?</strong><p>Estimez la puissance adaptée et vos économies à partir de votre facture.</p><a class="btn btn-vert btn-s" style="align-self:flex-start" href="index.html#simulateur">Utiliser le simulateur</a></div>
<div class="card" style="gap:2px"><strong style="margin-bottom:6px">À lire aussi</strong>
<a href="conseils.html" style="color:var(--encre);font-weight:600;padding:10px 0;border-bottom:1px solid #EEF4F0">Batterie lithium ou plomb : laquelle choisir ?</a>
<a href="conseils.html" style="color:var(--encre);font-weight:600;padding:10px 0;border-bottom:1px solid #EEF4F0">Coupures de courant : rester alimenté avec le solaire</a>
<a href="conseils.html" style="color:var(--encre);font-weight:600;padding:10px 0">Poussière et harmattan : nettoyer ses panneaux</a></div>
</aside>
</div>
</article>
{cta_band()}'''


def faq():
    cats = [("tous", "Toutes"), ("panneaux", "Panneaux"), ("batteries", "Batteries"), ("coupures", "Coupures"), ("garantie", "Paiement & garantie"), ("entretien", "Entretien"), ("diaspora", "Diaspora")]
    return f'''
<section class="page-hero bg-pale"><div class="container-narrow stack center" style="text-align:center;align-items:center">
{crumbs(("FAQ", None))}
<h1 class="h1">Questions fréquentes</h1>
<p class="lead">Tout ce qu’il faut savoir avant de passer au solaire : panneaux, batteries, coupures, garanties, entretien.</p>
<div style="width:100%;max-width:620px;position:relative;margin-top:6px"><label for="faq-q" class="visually-hidden">Rechercher une question</label>
<span style="position:absolute;left:20px;top:50%;transform:translateY(-50%);color:var(--texte-doux)">{ico("search", 20, 2)}</span>
<input id="faq-q" class="input" type="search" placeholder="Rechercher : batterie, garantie, coupure…" style="border-radius:999px;padding-left:52px;min-height:56px"></div>
</div></section>
<section class="section-tight"><div class="container-narrow stack" style="gap:22px">
<div style="display:flex;justify-content:center">{chips("faq-list", cats, "question")}</div>
<div class="faq-list" id="faq-list">{faq_items(FAQ_ALL, first_open=True, show_cat=True)}</div>
<div class="card card-soft" style="flex-direction:row;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:16px;margin-top:10px">
<div class="stack" style="gap:4px"><strong style="font-size:18px">Vous ne trouvez pas votre réponse ?</strong><span class="small muted">Posez-nous votre question directement.</span></div>
<a class="btn btn-vert btn-s" href="https://wa.me/33768026171?text=Bonjour%2C%20j%27ai%20une%20question">{ico("wa", 18, 1.9)}Écrire sur WhatsApp</a></div>
</div></section>'''


def contact():
    return f'''
<section class="page-hero hero bg-vert" style="padding-bottom:clamp(96px,10vw,160px)"><div class="deco-cercle" style="right:-180px;top:-200px;width:600px;height:600px;background:var(--vert-cercle)" aria-hidden="true"></div><div class="container">
{crumbs(("Contact et devis", None))}
<h1 class="h1" style="max-width:900px">Demandez votre <span class="accent">devis gratuit</span></h1>
<p class="lead">Disponibles partout au Sénégal. Écrivez-nous sur WhatsApp, appelez-nous ou remplissez le formulaire : nous vous recontactons rapidement.</p>
</div></section>
<section style="margin-top:clamp(-120px,-7vw,-64px);position:relative;z-index:2"><div class="container grid grid-3" style="gap:16px">
<a class="contact-tile on-light" href="{WA}"><span class="icon-box ib-vert">{ico("wa", 26, 1.9)}</span><span><span class="lbl">WhatsApp (France)</span><strong>{WA_TXT_AFF}</strong></span></a>
<a class="contact-tile on-light" href="{TEL}"><span class="icon-box ib-orange">{ico("phone", 24, 1.9)}</span><span><span class="lbl">Mobile (Sénégal)</span><strong>{TEL_TXT}</strong></span></a>
<a class="contact-tile on-light" href="mailto:{MAIL}"><span class="icon-box ib-pale">{ico("mail", 24, 1.9)}</span><span><span class="lbl">E-mail</span><strong>{MAIL}</strong></span></a>
</div></section>
<section class="section-tight"><div class="container row" style="align-items:flex-start">
<div style="flex:2 1 560px;min-width:0">{contact_form("c")}</div>
<aside class="col-s stack">
<div class="placeholder" style="aspect-ratio:4/3;border-radius:var(--rayon-l);border:1px dashed #9FC9AE">{ico("map", 48, 1.4)}<strong style="font-size:15px">Carte de la zone d’intervention</strong><span style="color:var(--texte);font-weight:400">Carte Google intégrée — adresse à confirmer</span></div>
<div class="card card-soft" style="gap:10px"><strong>Zone d’intervention</strong><p>Partout au Sénégal : Dakar, Thiès, Mbour, Saint-Louis, Touba, Kaolack, Ziguinchor et toutes les autres régions.</p></div>
<div class="card bg-creme" style="border:0;gap:10px"><strong>Vous êtes en France ?</strong><p style="color:#4A3F2A">Écrivez-nous sur WhatsApp au {WA_TXT_AFF} : nous gérons votre projet à distance.</p></div>
</aside>
</div></section>'''


def mentions():
    T = lambda s: f'<span class="todo">{s}</span>'
    return f'''
<section class="page-hero bg-gris" style="border-top:0"><div class="container">
{crumbs(("Mentions légales et confidentialité", None))}
<h1 class="h1" style="font-size:clamp(30px,4vw,52px)">Mentions légales et politique de confidentialité</h1>
<span class="small muted">Dernière mise à jour : {T("[date de mise en ligne]")}</span>
</div></section>
<section class="section-tight"><div class="container row legal" style="align-items:flex-start">
<nav class="toc" aria-label="Sommaire" style="flex:1 1 240px;max-width:300px"><strong class="small muted" style="letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px">Sommaire</strong>
<a href="#editeur">1. Éditeur du site</a><a href="#hebergement">2. Hébergement</a><a href="#propriete">3. Propriété intellectuelle</a><a href="#confidentialite">4. Données personnelles</a><a href="#droits">5. Vos droits</a><a href="#cookies">6. Statistiques et cookies</a></nav>
<div class="prose" style="flex:3 1 600px;font-size:16px;gap:36px">
<div id="editeur" class="stack" style="gap:12px"><h2 style="margin:0">1. Éditeur du site</h2><dl>
<dt>Raison sociale</dt><dd>GSL-ELEC — Gestion Solaire Locale et Électricité</dd><dt>Forme juridique</dt><dd>{T("[À compléter]")}</dd><dt>NINEA</dt><dd>{T("[À compléter]")}</dd><dt>RCCM</dt><dd>{T("[À compléter]")}</dd>
<dt>Siège social</dt><dd>{T("[Adresse au Sénégal]")}</dd><dt>Directeur de la publication</dt><dd>Bathie SARR</dd><dt>Contact</dt><dd>{MAIL} · {TEL_TXT}</dd></dl></div>
<div id="hebergement" class="stack" style="gap:12px"><h2 style="margin:0">2. Hébergement</h2><p>Le site est hébergé par {T("[nom de l’hébergeur, adresse, téléphone]")}.</p></div>
<div id="propriete" class="stack" style="gap:12px"><h2 style="margin:0">3. Propriété intellectuelle</h2><p>Le logo, les textes, les visuels et l’ensemble des contenus de ce site sont la propriété de GSL-ELEC ou utilisés avec autorisation. Toute reproduction sans accord écrit préalable est interdite.</p></div>
<div id="confidentialite" class="stack" style="gap:12px"><h2 style="margin:0">4. Données personnelles</h2>
<p>Lorsque vous remplissez un formulaire, nous recueillons les informations nécessaires pour traiter votre demande : nom, téléphone, e-mail (facultatif), ville, type de client, service souhaité, montant de facture, message et, si vous le souhaitez, une photo de votre facture.</p>
<ul><li><strong>Finalité :</strong> vous recontacter, préparer votre étude et votre devis.</li><li><strong>Base :</strong> votre consentement, donné en cochant la case du formulaire.</li><li><strong>Destinataires :</strong> uniquement l’équipe GSL-ELEC.</li><li><strong>Durée de conservation :</strong> {T("[à définir]")}.</li></ul>
<p>Ces traitements respectent la loi sénégalaise n° 2008-12 du 25 janvier 2008 sur la protection des données à caractère personnel.</p>
<p class="small" style="background:var(--creme);border-radius:14px;padding:14px 16px;color:#4A3F2A">Texte à faire valider par un juriste avant la mise en ligne, notamment les éventuelles formalités auprès de la Commission de Protection des Données Personnelles (CDP).</p></div>
<div id="droits" class="stack" style="gap:12px"><h2 style="margin:0">5. Vos droits</h2><p>Vous pouvez demander à accéder à vos données, les faire rectifier ou supprimer, ou vous opposer à leur utilisation, en écrivant à {MAIL}.</p></div>
<div id="cookies" class="stack" style="gap:12px"><h2 style="margin:0">6. Statistiques et cookies</h2><p>Le site utilise un outil de mesure d’audience pour comprendre sa fréquentation et améliorer ses contenus (pages vues, clics sur les boutons WhatsApp et d’appel, envois de formulaire). {T("[Outil et paramétrage à préciser.]")}</p></div>
</div>
</div></section>'''
