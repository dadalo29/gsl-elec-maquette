"""Génère le site statique GSL-ELEC dans ../site"""
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import page, SERVICES  # noqa: E402
from data import EQUIP, SERVICE_DATA  # noqa: E402
import pages_a as A  # noqa: E402
import pages_b as B  # noqa: E402

OUT = HERE.parent / "site"
if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(HERE / "assets", OUT / "assets")
IMG = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if IMG:
    (OUT / "assets/img").mkdir(parents=True, exist_ok=True)
    for f in IMG.iterdir():
        if "crop" not in f.name:
            shutil.copy(f, OUT / "assets/img" / f.name)

S = " — GSL-ELEC, solaire et électricité au Sénégal"
pages = [
    ("index.html", "GSL-ELEC — Réduisez votre facture d’électricité avec le solaire", "Installation solaire au Sénégal pour maisons, commerces, hôtels, industries et agriculture : étude de charge, batteries, pompage solaire, maintenance. Devis gratuit.", "accueil", A.index()),
    ("solutions.html", "Nos solutions solaires" + S, "Solaire maison et commerce, solaire professionnel et industriel, pompage solaire, appareils économes, maintenance et installations électriques au Sénégal.", "solutions", A.solutions()),
    ("batteries-haute-tension.html", "Batteries haute tension pour hôtels et industries" + S, "Batteries lithium haute tension et onduleurs hybrides triphasés pour hôtels et industries au Sénégal : énergie continue, moins de gasoil. Demande d’étude pro.", "solutions", A.batteries()),
    ("equipements.html", "Nos équipements solaires" + S, "Panneaux solaires, onduleurs, batteries lithium et haute tension, pompes solaires, protections et supervision : le matériel installé par GSL-ELEC.", "equipements", B.equipements()),
    ("comment-ca-marche.html", "Comment ça marche" + S, "De la prise de contact au SAV : les 6 étapes de votre projet solaire avec GSL-ELEC.", "etapes", B.etapes()),
    ("realisations.html", "Réalisations" + S, "Installations solaires réalisées par GSL-ELEC au Sénégal : maisons, commerces, hôtels, agriculture.", "realisations", B.realisations()),
    ("financement.html", "Financement et paiement en plusieurs fois" + S, "Payez votre installation solaire en plusieurs fois avec GSL-ELEC.", "financement", B.financement()),
    ("a-propos.html", "À propos" + S, "GSL-ELEC rend l’énergie solaire accessible aux familles, commerces et entreprises au Sénégal, et accompagne la diaspora.", "apropos", B.apropos()),
    ("conseils.html", "Conseils solaires" + S, "Guides pratiques sur le solaire au Sénégal : kWc et kWh, batteries, entretien, pompage, économies.", "conseils", B.conseils()),
    ("article-kwc-kwh.html", "kWc, kWh : comprendre votre installation solaire" + S, "La différence entre kWc et kWh expliquée simplement, et ce que produit 1 kWc au Sénégal.", "conseils", B.article()),
    ("faq.html", "Questions fréquentes" + S, "Panneaux, batteries, coupures, garanties, entretien, paiement : les réponses à vos questions sur le solaire.", "faq", B.faq()),
    ("contact.html", "Contact et devis gratuit" + S, "Demandez votre devis solaire gratuit : WhatsApp, téléphone ou formulaire. Partout au Sénégal.", "contact", B.contact()),
    ("mentions-legales.html", "Mentions légales et confidentialité" + S, "Mentions légales et politique de confidentialité du site GSL-ELEC.", "", B.mentions()),
]
for k, label, href in SERVICES:
    d = SERVICE_DATA[k]
    pages.append((href, d["title"] + S, d["lead"], "solutions", A.service(k)))
for e in EQUIP:
    pages.append((e["href"], e["title"] + S, e["desc"], "equipements", B.fiche(e)))

for fn, title, desc, active, body in pages:
    (OUT / fn).write_text(page(title, desc, active, body, fn), encoding="utf-8")

(OUT / ".nojekyll").write_text("")
(OUT / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
print(f"{len(pages)} pages générées dans {OUT}")
