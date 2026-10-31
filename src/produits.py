"""Gamme réelle GSL ENERGY installée par GSL-ELEC (d'après les fiches fournies par le client)."""
from html import escape
from common import ico

ONDULEURS = [
    ("8 kW", "Maison moyenne", "2 à 3 clims"),
    ("10 kW", "Grande maison", "3 à 4 clims"),
    ("12 kW", "Villa", "4 à 5 clims, piscine"),
    ("16 kW", "Grande villa", "Clims + équipements"),
    ("20 kW", "Commerce, bureau", "Forte consommation"),
    ("24 kW", "Petite entreprise", "Atelier, hôtel"),
]
ONDULEUR_FORCES = [
    ("Secours en 10 ms", "Bascule automatique sur batterie en cas de coupure : ordinateurs et appareils ne s’éteignent pas."),
    ("2 entrées solaires (MPPT)", "Accepte un grand champ de panneaux, répartis sur deux orientations de toit."),
    ("Compatible lithium", "Fonctionne avec les batteries LiFePO4 48 V (et plomb), dialogue avec le BMS de la batterie."),
    ("Entrée groupe électrogène", "Démarrage et arrêt automatiques du groupe ; le solaire passe toujours en priorité."),
    ("Mise en parallèle", "Jusqu’à 6 onduleurs reliés pour les grosses installations (hôtels, ateliers)."),
    ("Écran tactile et Wi-Fi", "Suivi de la production et de la batterie sur téléphone, diagnostic et mises à jour à distance."),
    ("Sorties intelligentes", "Sortie dédiée pour délester ou programmer des appareils (pompe, chauffe-eau)."),
    ("Triple protection", "Protection arc électrique (AFCI), arrêt rapide et contrôle d’isolement."),
]
ONDULEUR_SPECS = [
    ("Puissance nominale", "12 000 W"), ("Puissance de pointe", "18 000 VA (5 s)"),
    ("Puissance solaire max.", "24 000 W (2 × 12 000 W)"), ("Plage MPPT", "90 à 450 V"),
    ("Tension batterie", "51,2 V (40 à 60 V)"), ("Courant batterie", "250 A charge / 270 A décharge"),
    ("Temps de bascule", "10 ms"), ("Mise en parallèle", "1 à 6 unités"),
    ("Rendement max.", "> 93,5 %"), ("Communication", "CAN, RS485, USB, Wi-Fi"),
    ("Dimensions / poids", "760 × 485 × 161 mm · 35,5 kg"), ("Température", "-10 à 55 °C"),
]

BATTERIES = [
    ("p-bat-tout-en-un.jpg", "10 à 20 kWh", "Système tout-en-un", "Onduleur et batteries réunis dans un seul appareil empilable. Installation rapide.", "Maisons, villas"),
    ("p-bat-haute-tension.jpg", "10 à 61 kWh", "Batterie haute tension", "Modules empilés en haute tension : meilleur rendement pour les grosses consommations.", "Villas, commerces"),
    ("p-bat-sol-20.jpg", "20 kWh", "Batterie au sol", "Grande capacité sur roulettes, écran de contrôle. Pour climatiseurs et coupures longues.", "Villas, bureaux"),
    ("p-bat-sol-16.jpg", "16 kWh", "Batterie au sol", "Format compact sur roulettes avec écran, facile à déplacer et à brancher.", "Maisons, boutiques"),
    ("p-bat-empilable.jpg", "5 / 10 kWh", "Batterie empilable", "Modules de 5 kWh à empiler : on commence petit et on ajoute des modules plus tard.", "Maisons, boutiques"),
    ("p-bat-sol-14-16.jpg", "14 à 16 kWh", "Batterie au sol", "Design élégant, indicateur lumineux, à poser au sol dans la maison ou le garage.", "Maisons, villas"),
    ("p-bat-murale-10.jpg", "10 kWh", "Batterie murale empilable", "Se fixe au mur ou s’empile, gain de place. Pour les petites et moyennes installations.", "Appartements"),
    ("p-bat-murale-512.jpg", "5,12 kWh · 51,2 V 100 Ah", "Batterie murale 5,12 kWh", "Notre batterie phare : écran tactile, Wi-Fi, extinction incendie, garantie 10 ans.", "Tous projets"),
]
BAT_FORCES = [
    ("Écran tactile", "Affichage en temps réel de l’état de la batterie, réglage des paramètres et des protocoles."),
    ("Connectée", "Wi-Fi et Bluetooth : suivi à distance sur téléphone et intégration avec l’onduleur."),
    ("Sûre et fiable", "Chimie LiFePO4, système d’extinction incendie intégré, longue durée de vie, très faible autodécharge."),
    ("BMS intelligent", "Protection contre surcharge, décharge profonde, surintensité et températures extrêmes ; équilibrage des cellules."),
    ("4 installations possibles", "Au sol, en rack, empilée ou murale. Capacité extensible en ajoutant des modules."),
    ("Adaptée au climat", "Fonctionne de -20 °C à 55 °C, idéal pour la chaleur du Sénégal."),
]
BAT_CHIFFRES = [("5 à 209 kWh", "de stockage selon le modèle"), ("≥ 6 000", "cycles de charge"), ("10 ans", "de garantie (selon modèle)"), ("-20 à 55 °C", "plage de fonctionnement")]
BAT_SPECS = [
    ("Chimie", "LiFePO4 (lithium fer phosphate)"), ("Énergie / utile", "5,12 kWh / 4,86 kWh"),
    ("Tension", "51,2 V (46 à 56 V)"), ("Capacité", "100 Ah"), ("Courant (recomm. / max.)", "100 A / 150 A"),
    ("Profondeur de décharge", "90 %"), ("Extension", "Jusqu’à 18 en parallèle (92,16 kWh)"),
    ("Durée de vie", "≥ 6 500 cycles (80 % fin de vie)"), ("Installation", "Au sol, rack, empilée ou murale"),
    ("Communication", "CAN, RS485, Bluetooth, Wi-Fi"), ("Dimensions / poids", "687 × 400 × 142 mm · 62,5 kg"),
    ("Température", "Charge 0–55 °C · décharge -20–55 °C"), ("Garantie", "10 ans"),
    ("Certifications", "IEC 62619, CE-EMC, UN38.3, MSDS"),
]
BESS = [
    ("p-bess-64-112.jpg", "64 à 112 kWh", "GSL-BESS 64 à 112 kWh", ["Armoire extérieure refroidie par air", "Onduleur, BMS, climatisation, extinction incendie intégrés", "Puissance DC 56 kW · ≥ 8 000 cycles", "IP55 · 4 modèles : 64, 80, 96, 112 kWh"]),
    ("p-bess-80kva.jpg", "128 à 209 kWh", "GSL-BESS 80 kVA", ["Système triphasé tout-en-un 380/400 V", "Onduleur 80 kW, 6 MPPT, jusqu’à 128 kW de panneaux", "≥ 10 000 cycles · garantie 10 ans", "Certifié CE, IEC 62619, VDE, UN38.3"]),
]

SOURCE = '<p class="tiny muted">Matériel du fabricant GSL ENERGY, installé par GSL-ELEC. Caractéristiques issues des fiches fabricant ; fiche technique de chaque modèle sur demande.</p>'


def photo(src, alt, h=200, bg="#fff"):
    return f'<div style="height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center;padding:14px"><img src="assets/img/{src}" alt="{escape(alt)}" loading="lazy" style="max-height:100%;width:auto;max-width:100%;object-fit:contain;border-radius:8px"></div>'


def bande(src, alt, w, h):
    return f'<figure style="margin:0;border-radius:var(--rayon-l);overflow:hidden;box-shadow:var(--ombre-s);background:#E8EEF2"><img src="assets/img/{src}" alt="{escape(alt)}" width="{w}" height="{h}" loading="lazy" style="width:100%;height:auto"></figure>'


def spec_table(rows, caption):
    tr = "".join(f'<tr><th scope="row">{a}</th><td style="color:var(--texte)">{b}</td></tr>' for a, b in rows)
    return f'<div style="overflow-x:auto"><table class="table"><caption>{caption}</caption><tbody>{tr}</tbody></table></div>'


def forces(rows):
    return '<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:14px">' + "".join(
        f'<div class="card card-soft" style="gap:6px;padding:20px"><strong style="display:flex;gap:10px;align-items:center">{ico("check", 20, 2.4, extra=" style=\"color:var(--vert-cta);flex:0 0 20px\"")}{t}</strong><p style="font-size:14.5px">{d}</p></div>' for t, d in rows) + '</div>'


def onduleur_tiles():
    return '<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:12px">' + "".join(
        f'<div class="card" style="gap:4px;padding:18px;text-align:center;align-items:center"><strong style="font-size:26px;font-weight:800;color:var(--vert-cta)">{p}</strong><span style="font-weight:600;font-size:14.5px">{u}</span><span class="small muted">{c}</span></div>' for p, u, c in ONDULEURS) + '</div>'


def battery_cards(link="fiche-batteries-lithium.html"):
    return '<div class="grid grid-fill">' + "".join(
        f'''<a class="card card-media" href="{link}">{photo(src, t + " " + cap, 210, "#0E2A4A")}
<div class="card-body"><span class="badge badge-vert">{cap}</span><h3 style="font-size:17px;font-weight:700;letter-spacing:0">{t}</h3><p style="font-size:14px">{d}</p><span class="small muted"><strong style="color:var(--encre)">Idéal :</strong> {i}</span></div></a>''' for src, cap, t, d, i in BATTERIES) + '</div>'


def bess_cards():
    return '<div class="grid grid-2">' + "".join(
        f'''<div class="card card-media" style="flex-direction:row;flex-wrap:wrap">
<div style="flex:1 1 220px">{photo(src, t, 300)}</div>
<div class="card-body" style="flex:1 1 260px;justify-content:center"><span class="badge badge-orange">{cap}</span><h3 style="font-size:20px;font-weight:800;letter-spacing:0">{t}</h3>
<ul class="check-list" style="gap:8px">{"".join(f"<li style='font-size:14.5px'>{ico('check', 20, 2.4)}{x}</li>" for x in pts)}</ul></div></div>''' for src, cap, t, pts in BESS) + '</div>'


def chiffres():
    return '<div class="grid grid-4" style="gap:12px">' + "".join(
        f'<div class="card bg-pale" style="border:0;gap:2px;padding:18px"><strong style="font-size:26px;font-weight:800;color:var(--vert-hover)">{a}</strong><span class="small muted">{b}</span></div>' for a, b in BAT_CHIFFRES) + '</div>'


U = "https://images.unsplash.com/"
PHOTOS = {  # photos d'illustration libres de droits (licence Unsplash)
    "villa": U + "photo-1775686332316-8e1ce04d10d7",
    "hotel": U + "photo-1782141269306-95591212afdc",
    "pompage": U + "photo-1670519808965-16b9b2f724af",
    "boutique": U + "photo-1753881110611-00755160afd2",
    "atelier": U + "photo-1780445392528-4895da4b2cb8",
    "panneaux": U + "photo-1521618755572-156ae0cdd74d",
    "onduleurs-reseau": U + "photo-1780445392417-68b9dccc45f2",
    "structures": U + "photo-1509391366360-2e959784a276",
    "pompes-solaires": U + "photo-1561115867-be8460fbebfe",
    "protections": U + "photo-1544724569-5f546fd6f2b5",
}


def img_src(x, w=900):
    if x.startswith("http"):
        return f"{x}?w={w}&q=75&auto=format&fit=crop"
    return "assets/img/" + x


def is_photo(x):
    return x.startswith("http") or x == "maison-solaire.jpg"


CREDIT = '<p class="tiny muted">Photos d’illustration libres de droits (Unsplash) en attendant les photos de chantiers GSL-ELEC.</p>'
