import csv

def lire_csv(nom_fichier):
 with open (nom_fichier, "r" , newline="") as fichier:
   lecteur=csv.reader(fichier)
   for ligne in lecteur:
      print(ligne)
def lire_csv(nom_fichier):
 with open (nom_fichier, "r" , newline="") as fichier:
   lecteur=csv.reader(fichier)
   for ligne in lecteur:
      print(ligne)
      
def lire_csv_dict(nom_fichier)
    
