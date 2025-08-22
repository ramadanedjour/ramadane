import json
def gestionnaire():
    try:
        return json.load(open("inventaire.json")
        except:{}
def inventair(i):
    json.dump(i,open("inventaire.json","w"))
def main():
    while True:
        print("\n1.ajouter 2.voir 3.supprimer 4.modifier 5.quiter")
        c,i=input("choix"),g=()
        if c=="1":
            n=input("nom")
       
