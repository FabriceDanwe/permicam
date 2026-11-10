"""
Permicam - Application Flask
Portail d'enrôlement à la demande de permis de conduire et badge.
Recréé en Python/Flask à partir du site HTML statique original.
"""

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


# Données du demandeur (identiques à celles du site original)
DEMANDEUR = {
    "etat_demande": "Traitement en cours",
    "etat_couleur": "green",
    "photo": "permicam_files/1000208285-removebg-preview.png",
    "nom": "BADAWE",
    "prenoms": "JUDICAEL",
    "lieu_naissance": "LAMOUDAM",
    "date_naissance": "06/01/2003",
    "genre": "M",
    "nationalite": "CAMEROUNAISE",
    "numero_permis": "NO-105380-24",
    "numero_capacite": "",
    "categories_permis": "   B C",
    "date_creation_demande": "03/09/2026",
}


@app.route("/")
@app.route("/consultation/check")
def index():
    """Route principale - affiche le récapitulatif de la demande."""
    return render_template("index.html", demandeur=DEMANDEUR)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
