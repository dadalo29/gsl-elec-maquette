"""Données du site : équipements, services, FAQ, et composants qui les affichent."""
from html import escape
from common import ico, ARROW, WA
from produits import PHOTOS, img_src, is_photo

TINT = {"g": ("var(--vert-pale)", "var(--vert-cta)"), "o": ("var(--creme-2)", "var(--orange-texte)"), "d": ("var(--vert-fonce)", "var(--orange-clair)")}

EQUIP = [
    dict(key="panneaux", img=PHOTOS["panneaux"], icon="panel", t="o", title="Panneaux solaires", who="tous les clients", tags="maison commerce pro agri",
         desc="Monocristallins haut rendement : ils transforment la lumière du soleil en électricité. Résistants à la chaleur et à la poussière.",
         long="Des panneaux monocristallins haut rendement qui transforment la lumière du soleil en électricité. Conçus pour résister à la chaleur et à la poussière, ils offrent une longue durée de vie.",
         uses=["Toitures", "Au sol", "Ombrières de parking"], pros=["Haut rendement, même par forte chaleur", "Résistants à la poussière et aux intempéries", "Longue durée de production"], range="Plusieurs puissances par panneau"),
    dict(key="onduleurs-hybrides", icon="inverter", t="g", img="p-onduleur-hybride.jpg", title="Onduleurs hybrides 8 à 24 kW", who="maisons, commerces, entreprises", tags="maison commerce pro",
         desc="Le cerveau de l’installation : solaire d’abord, charge des batteries, bascule automatique sur le réseau ou le groupe.",
         long="Le « cerveau » de l’installation : il utilise d’abord l’énergie solaire, charge les batteries et bascule automatiquement sur le réseau ou le groupe électrogène en cas de besoin.",
         uses=["Maison avec batteries", "Commerce", "Entreprise"], pros=["Priorité au solaire, économies maximales", "Bascule automatique sans coupure ressentie", "Suivi depuis le téléphone"], range="Monophasés et triphasés"),
    dict(key="onduleurs-reseau", img=PHOTOS["onduleurs-reseau"], icon="inverter", t="g", title="Onduleurs réseau", who="bureaux et commerces actifs le jour", tags="commerce pro",
         desc="Ils injectent la production solaire directement dans votre installation, sans batterie. La solution la plus économique en journée.",
         long="Ils injectent la production solaire directement dans votre installation pour consommer moins sur le réseau, sans batterie. C’est la solution la plus économique pour réduire la facture en journée.",
         uses=["Bureaux", "Commerces ouverts le jour", "Ateliers"], pros=["Investissement réduit, sans batterie", "Économies immédiates en journée", "Installation simple"], range="Monophasés et triphasés"),
    dict(key="batteries-lithium", icon="battery", t="g", img="p-bat-murale-512.jpg", title="Batteries lithium", who="maisons, boutiques, petits commerces", tags="maison commerce",
         desc="LiFePO4, de 5 à 61 kWh : au sol, murales ou empilables, pour la nuit et les coupures. Garantie jusqu’à 10 ans.",
         long="Des batteries LiFePO4 qui stockent l’énergie du jour pour la nuit et les coupures. Longue durée de vie, sans entretien et extensibles.",
         uses=["Nuit", "Coupures", "Petits commerces"], pros=["Sans entretien courant", "Extensibles en ajoutant des modules", "Gestion électronique intégrée (BMS)"], range="Plusieurs capacités, extensibles"),
    dict(key="batteries-haute-tension", icon="battery", t="d", img="p-bess-80kva.jpg", title="Stockage haute tension (BESS)", who="industries et grands hôtels", tags="pro", star=True,
         desc="Armoires de 64 à 209 kWh, onduleur, BMS et extinction incendie intégrés, pour hôtels et industries.",
         long="Des modules lithium LiFePO4 empilés et reliés en série pour fonctionner à plusieurs centaines de volts, associés à un onduleur hybride triphasé haute tension. Le stockage de grande capacité des gros consommateurs.",
         uses=["Hôtels", "Industries", "Chambres froides"], pros=["Grande capacité, extensible", "Meilleur rendement, moins de pertes", "Supervision et protection de chaque cellule"], range="Dimensionné sur mesure après étude"),
    dict(key="pompes-solaires", img=PHOTOS["pompes-solaires"], icon="drop", t="g", title="Pompes solaires", who="agriculteurs, éleveurs, forages", tags="agri",
         desc="Immergées ou de surface, alimentées par les panneaux, avec un contrôleur qui adapte le débit à l’ensoleillement.",
         long="Des pompes immergées ou de surface alimentées directement par les panneaux, avec un contrôleur qui adapte le débit à l’ensoleillement. Pas de gasoil, pas de réseau.",
         uses=["Forages", "Irrigation", "Abreuvement"], pros=["Zéro carburant", "Fonctionne loin du réseau", "Peu d’entretien"], range="Immergées et de surface"),
    dict(key="structures", img=PHOTOS["structures"], icon="bracket", t="g", title="Structures de fixation", who="tous les clients", tags="maison commerce pro agri",
         desc="Aluminium ou acier galvanisé pour toits, sols et ombrières de parking, résistants à la corrosion et au vent.",
         long="Des supports en aluminium ou en acier galvanisé pour toits, sols et ombrières de parking, résistants à la corrosion et au vent.",
         uses=["Toits", "Sols", "Ombrières"], pros=["Résistance à la corrosion", "Tenue au vent", "Orientation optimisée des panneaux"], range="Aluminium et acier galvanisé"),
    dict(key="protections", img=PHOTOS["protections"], icon="shieldbolt", t="g", title="Protections électriques", who="tous les clients", tags="maison commerce pro agri",
         desc="Coffrets AC/DC, disjoncteurs, parafoudres et mise à la terre : protègent l’installation, les appareils et les personnes.",
         long="Coffrets AC/DC, disjoncteurs, parafoudres et mise à la terre : ils protègent l’installation, les appareils et les personnes.",
         uses=["Coffrets AC/DC", "Parafoudres", "Mise à la terre"], pros=["Sécurité des personnes", "Protection des appareils", "Installation durable"], range="Adaptées à chaque installation"),
    dict(key="supervision", icon="monitor", t="g", title="Supervision à distance", who="tous, indispensable en industrie et pour la diaspora", tags="maison commerce pro agri",
         desc="Production, consommation et batteries suivies depuis une application ; GSL-ELEC peut surveiller et dépanner à distance.",
         long="Suivez la production, la consommation et l’état des batteries depuis une application mobile. GSL-ELEC peut aussi surveiller et dépanner votre installation à distance.",
         uses=["Application mobile", "Alertes", "Diaspora"], pros=["Tout voir depuis son téléphone", "Diagnostic à distance", "Suivi de la maison familiale depuis l’étranger"], range="Selon l’onduleur installé"),
    dict(key="appareils", icon="snow", t="o", title="Appareils basse consommation", who="maisons, commerces, hôtels", tags="maison commerce pro",
         desc="Réfrigérateurs et congélateurs économes, climatiseurs inverter, éclairage LED : moins de besoins, une installation plus petite.",
         long="Réfrigérateurs et congélateurs économes, climatiseurs inverter et éclairage LED : ils réduisent le besoin en énergie, donc la taille et le coût de l’installation.",
         uses=["Froid", "Climatisation", "Éclairage"], pros=["Moins de consommation", "Installation solaire plus petite", "Confort préservé"], range="Froid, climatisation, LED"),
]
for e in EQUIP:
    e["href"] = f"fiche-{e['key']}.html"


def equip_card(e, small=False):
    bg, ink = TINT[e["t"]]
    star = '<span class="badge" style="position:absolute;top:12px;left:12px;background:var(--encre);color:var(--orange-clair)">Offre phare</span>' if e.get("star") else ""
    h = (150 if small else 180) if e.get("img") else (120 if small else 150)
    return f'''<a class="card card-media" href="{e["href"]}" data-tags="{e["tags"]}">
<div style="height:{h}px;background:{"#fff" if e.get("img") else bg};color:{ink};display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;{"border-bottom:1px solid var(--bord);padding:10px" if e.get("img") and not is_photo(e["img"]) else ""}">{(f'<img src="{img_src(e["img"], 700)}" alt="" loading="lazy" style="width:100%;height:100%;object-fit:cover">' if is_photo(e["img"]) else f'<img src="{img_src(e["img"])}" alt="" loading="lazy" style="max-height:100%;max-width:100%;object-fit:contain">') if e.get("img") else ico(e["icon"], 56 if small else 64, 1.3)}{star}</div>
<div class="card-body"><h3 style="font-size:17px;font-weight:700;letter-spacing:0">{e["title"]}</h3><p style="font-size:14px">{e["desc"]}</p>
<span class="small muted"><strong style="color:var(--encre)">Pour :</strong> {e["who"]}</span>
<span class="more" style="font-size:14.5px">Voir la fiche{ico("arrow", 15, 2.2)}</span></div></a>'''


SERVICE_DATA = {
    "maison": dict(title="Solaire maison et commerce", badge="De 5 à 50 kWc",
        lead="Produisez votre propre électricité pendant la journée, stockez-la pour le soir et ne subissez plus les coupures. Pour les villas, maisons, boutiques, commerces et bureaux.",
        who=["Villas et maisons familiales", "Boutiques et commerces de quartier", "Bureaux et cabinets"],
        benefits=[("Une facture réduite", "Vous consommez d’abord l’énergie de vos panneaux ; le réseau ne sert plus qu’en appoint."), ("Fini les coupures", "Les batteries prennent le relais automatiquement : lumière et froid restent allumés."), ("Paiement en plusieurs fois", "Étalez le coût de votre installation, selon les modalités de votre devis."), ("Suivi sur téléphone", "Production, consommation et batteries consultables à distance.")],
        examples=[("Villa familiale à Dakar", "Éclairage, ventilateurs, réfrigérateur et télévision alimentés jour et nuit, même pendant les délestages."), ("Boutique de quartier", "Congélateurs et caisse toujours en marche : plus de marchandise perdue pendant les coupures."), ("Cabinet ou bureau", "Ordinateurs, connexion internet et climatisation en journée sur l’énergie solaire.")],
        equip=["panneaux", "onduleurs-hybrides", "batteries-lithium", "protections", "supervision"]),
    "pro": dict(title="Solaire professionnel et industriel", badge="Jusqu’à 200 kWc",
        lead="Réduisez vos charges d’énergie et sécurisez votre activité avec une installation dimensionnée pour de gros volumes, associée à des batteries haute tension.",
        who=["Hôtels, résidences et restaurants", "Pharmacies, cliniques et écoles", "Ateliers, industries et supermarchés"],
        benefits=[("Charges réduites", "Moins de kWh achetés au réseau et moins de gasoil pour vos groupes électrogènes."), ("Activité continue", "Chambres, cuisines, chaîne du froid et machines alimentées sans interruption."), ("Batteries haute tension", "Stockage de grande capacité, extensible au rythme de votre croissance."), ("Maintenance sous contrat", "Visites programmées et supervision à distance par nos équipes.")],
        examples=[("Hôtel en bord de mer", "Climatisation des chambres, cuisine et chambres froides sécurisées, même lors des coupures."), ("Pharmacie", "Réfrigérateurs à médicaments maintenus à température, jour et nuit."), ("Atelier ou petite industrie", "Machines alimentées en journée par le solaire, appoint réseau ou groupe automatique.")],
        equip=["panneaux", "onduleurs-hybrides", "batteries-haute-tension", "supervision", "structures"]),
    "pompage": dict(title="Pompage solaire", badge="Sans gasoil ni réseau",
        lead="Pompez l’eau de votre forage grâce au soleil, sans carburant ni raccordement au réseau, pour l’irrigation, l’élevage et le maraîchage.",
        who=["Maraîchers et agriculteurs", "Éleveurs", "Forages villageois et communautaires"],
        benefits=[("Zéro carburant", "Plus d’achat ni de transport de gasoil pour faire tourner la pompe."), ("Autonomie totale", "Fonctionne loin du réseau électrique, directement avec les panneaux."), ("Débit adapté", "Le contrôleur ajuste le pompage à l’ensoleillement de la journée."), ("Peu d’entretien", "Moins de pièces mécaniques qu’un groupe motopompe.")],
        examples=[("Maraîchage", "Irrigation des parcelles en journée, avec stockage de l’eau dans un bassin ou un château d’eau."), ("Élevage", "Abreuvement du bétail assuré sans dépendre d’un approvisionnement en carburant."), ("Forage communautaire", "Eau disponible pour le village, avec un coût d’exploitation très réduit.")],
        equip=["pompes-solaires", "panneaux", "structures", "protections"]),
    "appareils": dict(title="Appareils à faible consommation", badge="Moins de besoins",
        lead="Des appareils économes réduisent votre consommation… et donc la taille et le coût de votre installation solaire.",
        who=["Maisons et villas", "Commerces et restaurants", "Hôtels et résidences"],
        benefits=[("Installation plus petite", "Moins de consommation, c’est moins de panneaux et de batteries à acheter."), ("Économies immédiates", "Même raccordé au réseau, vous payez moins chaque mois."), ("Froid fiable", "Réfrigérateurs et congélateurs adaptés à la chaleur."), ("Confort préservé", "Climatisation inverter et éclairage LED de qualité.")],
        examples=[("Climatiseur inverter", "Il module sa puissance au lieu de s’arrêter et redémarrer : moins d’énergie pour le même confort."), ("Froid économe", "Réfrigérateurs et congélateurs basse consommation pour la maison et le commerce."), ("Éclairage LED", "La même lumière pour une fraction de la consommation des anciennes ampoules.")],
        equip=["appareils", "panneaux", "onduleurs-hybrides"]),
    "maintenance": dict(title="Maintenance et SAV", badge="Contrats annuels",
        lead="Une installation bien entretenue produit plus et dure plus longtemps. Nous assurons l’inspection, le nettoyage, le contrôle et le dépannage.",
        who=["Clients GSL-ELEC", "Installations existantes à remettre en état", "Professionnels sous contrat"],
        benefits=[("Production préservée", "La poussière et le sable réduisent la production : un nettoyage régulier la rétablit."), ("Contrôles complets", "Batteries, onduleurs, câblage et protections vérifiés à chaque visite."), ("Dépannage", "Diagnostic à distance grâce à la supervision, puis intervention sur place."), ("Contrat annuel", "Visites programmées et suivi tout au long de l’année.")],
        examples=[("Visite annuelle", "Inspection complète, nettoyage des panneaux et rapport de l’état de l’installation."), ("Après la saison sèche", "Nettoyage des panneaux encrassés par la poussière pour retrouver toute la production."), ("Alerte à distance", "Une anomalie détectée sur l’application déclenche une intervention.")],
        equip=["supervision", "protections"]),
    "electricite": dict(title="Installations électriques", badge="Électricité & automatisme",
        lead="Électricité générale, automatisme et dépannage pour particuliers et professionnels, réalisés dans les règles de l’art.",
        who=["Particuliers", "Commerces et bureaux", "Entreprises et bâtiments"],
        benefits=[("Installation sécurisée", "Câblage, tableaux et protections adaptés pour les personnes et les appareils."), ("Mise à la terre", "Indispensable pour la sécurité et la durée de vie du matériel."), ("Automatisme", "Inverseur automatique réseau / groupe, commandes et éclairage."), ("Dépannage", "Diagnostic et réparation des pannes électriques.")],
        examples=[("Rénovation de tableau", "Remplacement d’un tableau vétuste par un tableau protégé et lisible."), ("Inverseur réseau / groupe", "Bascule automatique sur le groupe électrogène en cas de coupure."), ("Éclairage extérieur", "Éclairage de cour, de parking ou de façade, avec commande automatique.")],
        equip=["protections", "structures"]),
}

FAQ_ALL = [
    ("panneaux", "Panneaux", "Combien de temps durent les panneaux solaires ?", "Des panneaux de qualité produisent pendant plusieurs décennies, avec une baisse de rendement très progressive. La garantie exacte du fabricant figure sur chaque fiche technique remise avec votre devis."),
    ("panneaux", "Panneaux", "Mon toit convient-il à des panneaux ?", "Lors de la visite, nous vérifions l’orientation, l’ombrage, la surface et la solidité du support. Si le toit ne convient pas, une pose au sol ou en ombrière est souvent possible."),
    ("panneaux", "Panneaux", "Les panneaux produisent-ils quand il fait nuageux ?", "Oui, mais moins. La production dépend de l’ensoleillement : elle est plus forte en milieu de journée et par temps clair."),
    ("batteries", "Batteries", "Les batteries lithium demandent-elles de l’entretien ?", "Les batteries LiFePO4 ne demandent pas d’entretien courant. Leur système de gestion électronique (BMS) protège chaque cellule, et nous les contrôlons lors des visites de maintenance."),
    ("batteries", "Batteries", "Combien de temps tiennent les batteries pendant une coupure ?", "Tout dépend de leur capacité et des appareils allumés. L’étude de charge permet de dimensionner les batteries selon vos besoins et la durée habituelle des coupures."),
    ("coupures", "Coupures", "Que se passe-t-il pendant une coupure de courant ?", "Avec batteries, l’onduleur hybride prend le relais automatiquement : lumière, froid et appareils essentiels continuent de fonctionner. Sans batterie, l’onduleur réseau s’arrête par sécurité."),
    ("coupures", "Coupures", "Puis-je garder mon groupe électrogène ?", "Oui. L’onduleur hybride peut basculer automatiquement sur le groupe quand le soleil et les batteries ne suffisent pas, ce qui réduit fortement sa consommation de gasoil."),
    ("garantie", "Paiement & garantie", "Quelle garantie sur le matériel ?", "Chaque équipement est livré avec sa fiche technique et ses conditions de garantie fabricant, précisées dans votre devis."),
    ("garantie", "Paiement & garantie", "Puis-je payer en plusieurs fois ?", "Oui, le paiement en plusieurs fois est possible. Les modalités adaptées à votre projet sont détaillées dans votre devis."),
    ("entretien", "Entretien", "À quelle fréquence nettoyer les panneaux ?", "La poussière réduit la production. Un nettoyage régulier, plus fréquent en saison sèche, permet de la maintenir. Nous proposons des contrats d’entretien annuels."),
    ("entretien", "Entretien", "Combien de temps dure une installation ?", "Le délai dépend de la taille du projet. Il est précisé dans votre devis, après la visite et l’étude de charge."),
    ("diaspora", "Diaspora", "Je vis en France : comment suivre le chantier ?", "Votre interlocuteur est joignable en France sur WhatsApp. Vous recevez les photos du chantier et pouvez suivre la production depuis votre téléphone grâce à la supervision à distance."),
]
FAQ_HOME = [FAQ_ALL[i] for i in (0, 5, 3, 8, 10)]

_fid = [0]


def faq_items(items, first_open=False, show_cat=False):
    out = []
    for i, (tag, cat, q, a) in enumerate(items):
        _fid[0] += 1
        n = _fid[0]
        op = first_open and i == 0
        catl = f'<span class="cat">{cat}</span>' if show_cat else ""
        out.append(f'''<div class="faq-item{" open" if op else ""}" data-tags="{tag}">
<button type="button" aria-expanded="{"true" if op else "false"}" aria-controls="faq-a{n}" id="faq-q{n}"><span>{catl}{escape(q)}</span><span class="pm"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14"/><path class="v" d="M12 5v14"/></svg></span></button>
<div class="answer" id="faq-a{n}" role="region" aria-labelledby="faq-q{n}">{escape(a)}</div></div>''')
    return "\n".join(out)


SERVICE_OPTS = [("maison", "Solaire maison et commerce"), ("pro", "Solaire professionnel et industriel"), ("pompage", "Pompage solaire"), ("appareils", "Appareils à faible consommation"), ("maintenance", "Maintenance et SAV"), ("electricite", "Installations électriques")]


def contact_form(pfx, short=False, service=None, service_title=None):
    p = pfx
    if short:
        return f'''<form class="form-card" data-demo-form novalidate aria-label="Demande de devis : {escape(service_title)}" action="contact.html">
<div class="form-fields stack" style="gap:16px">
<strong style="font-size:22px;font-weight:800">Demander un devis pour ce service</strong>
<div class="prefill">{ico("check", 18, 2.4, extra=' style="color:var(--vert-cta)"')}<span>Service pré-sélectionné : <strong>{escape(service_title)}</strong></span></div>
<div class="form-grid">
<div class="field"><label for="{p}-nom">Nom complet</label><input class="input" id="{p}-nom" type="text" placeholder="Awa Diop" autocomplete="name"></div>
<div class="field"><label for="{p}-tel">Téléphone *</label><input class="input" id="{p}-tel" type="tel" placeholder="+221 7X XXX XX XX" autocomplete="tel" data-required><span class="err-msg" data-err-for="{p}-tel">Indiquez un numéro de téléphone valide.</span></div>
</div>
<label class="consent" for="{p}-ok"><input id="{p}-ok" type="checkbox" data-required><span>J’accepte d’être recontacté(e) par GSL-ELEC au sujet de ma demande.</span></label>
<span class="err-msg" data-err-for="{p}-ok">Merci de cocher cette case.</span>
<button class="btn btn-vert btn-bloc" type="submit">Être rappelé{ARROW}</button>
<a class="link-arrow" style="justify-content:center" href="contact.html?service={service}">Ou remplir le formulaire complet</a>
</div>
<div class="success" role="status"><span class="tick">{ico("check", 40, 2.4)}</span><strong>Merci, demande bien envoyée !</strong><p>Nous vous rappelons très vite au sujet de : {escape(service_title)}.</p><button class="btn btn-contour-vert btn-s" type="button" data-reset-form>Nouvelle demande</button></div>
</form>'''
    types = "".join(f"<option>{t}</option>" for t in ["Particulier (maison, villa)", "Commerce / bureau", "Entreprise / hôtel / industrie", "Agriculteur / éleveur", "Diaspora (maison au Sénégal)"])
    svcs = "".join(f'<option value="{k}">{l}</option>' for k, l in SERVICE_OPTS)
    sid = "c-service" if p == "c" else f"{p}-service"
    return f'''<form class="form-card" data-demo-form novalidate aria-label="Demande de devis">
<div class="form-fields stack" style="gap:16px">
<div class="stack" style="gap:4px"><strong style="font-size:22px;font-weight:800">Demande de devis gratuit</strong><span class="small muted">Les champs marqués * sont obligatoires.</span></div>
<div class="form-grid">
<div class="field"><label for="{p}-nom">Nom complet</label><input class="input" id="{p}-nom" name="nom" type="text" placeholder="Awa Diop" autocomplete="name"></div>
<div class="field"><label for="{p}-tel">Téléphone *</label><input class="input" id="{p}-tel" name="telephone" type="tel" placeholder="+221 7X XXX XX XX" autocomplete="tel" data-required><span class="err-msg" data-err-for="{p}-tel">Indiquez un numéro de téléphone valide.</span></div>
<div class="field"><label for="{p}-mail">E-mail <span class="opt">(facultatif)</span></label><input class="input" id="{p}-mail" name="email" type="email" placeholder="vous@exemple.com" autocomplete="email"></div>
<div class="field"><label for="{p}-ville">Ville / région</label><input class="input" id="{p}-ville" name="ville" type="text" placeholder="Dakar, Thiès…" autocomplete="address-level2"></div>
<div class="field"><label for="{p}-type">Vous êtes</label><select class="input" id="{p}-type" name="type">{types}</select></div>
<div class="field"><label for="{sid}">Service souhaité</label><select class="input" id="{sid}" name="service">{svcs}</select></div>
<div class="field"><label for="{p}-facture">Facture mensuelle (FCFA)</label><input class="input" id="{p}-facture" name="facture" type="text" inputmode="numeric" placeholder="45 000"></div>
</div>
<div class="field"><label for="{p}-msg">Votre message</label><textarea class="input" id="{p}-msg" name="message" rows="3" placeholder="Décrivez votre besoin : appareils, coupures, toit disponible…"></textarea></div>
<label class="upload" for="{p}-photo">{ico("upload", 24, 1.8, extra=' style="color:var(--vert-cta);flex:0 0 24px"')}<span data-file-name><strong>Ajouter une photo de votre facture</strong> (facultatif) · JPG, PNG ou PDF</span><input id="{p}-photo" name="photo" type="file" accept="image/*,application/pdf"></label>
<label class="consent" for="{p}-ok"><input id="{p}-ok" type="checkbox" data-required><span>J’accepte que GSL-ELEC utilise ces informations pour me recontacter au sujet de ma demande, conformément à la <a href="mentions-legales.html#confidentialite">politique de confidentialité</a>.</span></label>
<span class="err-msg" data-err-for="{p}-ok">Merci de cocher cette case pour envoyer votre demande.</span>
<button class="btn btn-vert btn-bloc" type="submit">Envoyer ma demande{ARROW}</button>
<span class="form-note">{ico("lock", 14, 2)}Formulaire protégé contre le spam. Vos données servent uniquement à traiter votre demande.</span>
</div>
<div class="success" role="status"><span class="tick">{ico("check", 40, 2.4)}</span><strong>Merci, votre demande est bien envoyée !</strong><p>Notre équipe vous recontacte très vite par téléphone ou sur WhatsApp pour préparer votre étude.</p>
<a class="btn btn-vert btn-s" href="https://wa.me/33768026171?text=Bonjour%2C%20je%20viens%20d%27envoyer%20une%20demande%20de%20devis">{ico("wa", 18, 1.9)}Accélérer sur WhatsApp</a>
<button class="btn btn-contour-vert btn-s" type="button" data-reset-form>Envoyer une autre demande</button></div>
</form>'''
