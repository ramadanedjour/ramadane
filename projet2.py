import random
def choi_de_niveau(niveau):
#choisi un nombre au hazard du borne du niveau choisi
    if niveau=="facile":
        return random.randint(1,50)
    elif niveau=="moyen":
        return random.randint(1,100)
    elif niveau=="difficile":
        return random.randint(1,200)
    else:
       return None
def devinette(niveau):
#cette fonction gère un tour de jeu
    secret=choi_de_niveau(niveau)
    if secret is None:
        return "invalide"
    if niveau=="facile":
        max_tentatives,max_nbres=10,50
    elif niveau=="moyen":
        max_tentatives,max_nbres=15,100
    elif niveau=="difficile":
        max_tentatives,max_nbres=20,200
    else:
        return "niveau invalide"
    print(f"bienvenue dans devinette niveau{niveau}")
    print(f"vous avez jusqu'a {max_tentatives} tenttatives pour gagner")
    tentative=0
    while tentative<max_tentatives:
        try:
            proposition=int(input("devine:"))
            tentative+=1
            if proposition!=secret:
                print("non c'est pas le bon choix essayez encor")
            else:
                print(f"felicitation vous avez gagnez le nombtre en {tentative} tentatives")
                return
            print(f"il vous reste {max_tentatives-tentative} tentative.\n")
        except ValueError:
            print("veuillez entrer un nombre valide")
    print(f"vous avez epuisez vos chonces le secret est {secret}.")
def main():
    print("jeux de devinette")
#ici on choisi le niveau de jeu souhaiter par le joueur
    while True:
        niveau_choisi=""
        while niveau_choisi not in ("facile","moyen","difficile"):
            niveau_choisi=input("choisissez lz niveau de votre choix parmi ('facile','moyen' et 'difficile')")
            if niveau_choisi not in ("facile","moyen","difficile"):
                print("niveau non valide choisissez entre facile moyen et difficile")
        devinette(niveau_choisi)
        while True:
#ici on demande au joueur s'il veut continue a jouer
            rejouer=input("voulez vous recommencer?")
            if rejouer=="oui":
                continue
            elif rejouer=="non":
                print("a la prochaine fois!")
                break
            else:
                print("oui ou non")
#commencez a jouer
main()
