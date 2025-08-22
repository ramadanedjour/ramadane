import random
liste=["pierre","papier","sizo"]
i=random.choice(liste)
choisi=str(input("entrer votre choix:"))
while choisi==i:
    continue
if choisi=="papier" and i=="pierre":
   print(f"felicitation vous avez gagnez")
elif choisi=="papier" and i=="sizo":
    print(f"desolé vous avez perdue c'est sizo contre papier")
elif choisi=="pierre" and i=="sizo":
    print("felicitation vous avez gagné")
elif choisi=="pierre" and i=="papier":
    print("perdue")
elif choisi=="sizo" and i=="pierre":
    print("perdue")
elif choisi=="sizo" and i=="papier":
    print ("gagne")
else:
    print("ni perdue ni gagné")
