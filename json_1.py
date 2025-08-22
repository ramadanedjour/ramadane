import json
def lire_json(nom_fichier)
    try:
        with open(nom_fichier,"r")as fichier:
            donnees=json.load(fichier)
            return donnees
    except json.JSONDecodeError:
        print("erreur:JSON invalide")
        return None
    def ecrire_json(titainique-parquet.json1,donnees):
        with open(nom_fichier,"w") as fichier:
            json.dump(donnees,fichier,indent=4)
donnees={
    "nom"="ali",
    "age"=25,
    "ville"="ati",
}
ecrire_json("noms.json",donnees)