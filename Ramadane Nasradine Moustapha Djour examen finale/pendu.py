import random
liste=["python","programation","ordinateur","algorithme","fonction"]
secret=random.choice(liste)
tentative=0
print(liste)
while tentative<6:
     choisi=str(input("entrer le mot de votre choix parmis python,programation,ordinateur,algorithme,fonction:"))
     tentative+=1
     if choisi==secret:
          print("gagner")
          break
     elif choisi!=secret:
          print("perdue essaye encore il te reste encore de la chance")
     else:
         print("perdue")
