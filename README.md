# GSL-ELEC — maquette du site

Maquette cliquable du site de **GSL-ELEC — Gestion Solaire Locale et Électricité** (solaire et électricité au Sénégal).

- **Site en ligne :** servi par GitHub Pages depuis le dossier `docs/`.
- **29 pages** : accueil, solutions, 6 pages service, batteries haute tension, équipements + 10 fiches, comment ça marche, réalisations, financement, à propos, conseils + article, FAQ, contact, mentions légales.
- HTML/CSS/JS statique, responsive (ordinateur et mobile), sans dépendance.

## Modifier et regénérer

Les pages sont générées par `src/build.py` (Python 3.10+) :

```bash
python3 src/build.py images-source
rm -rf docs && cp -r site docs
```

Prévisualiser en local :

```bash
python3 -m http.server 8000 -d docs
# puis ouvrir http://localhost:8000
```

## À savoir

- Maquette : les formulaires n'envoient rien (message de confirmation simulé).
- Le simulateur utilise la grille Senelec 2026 (hors redevances) et des hypothèses provisoires (130 kWh/kWc/mois, 60 % / 70 % de couverture solaire) à valider avec le client.
- Les éléments entre crochets et en orange sont à fournir par le client (NINEA, RCCM, fondateur, conditions de paiement, chiffres batteries, photos, témoignages, hébergeur).
- Pages non indexées (`noindex`) tant que c'est une maquette.
