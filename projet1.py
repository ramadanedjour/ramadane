#bienvenu_dans _ta_calculatrice
def addition(a,b):
    return a+b
def soutraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def calculette ():
   while True:
#ce passage nous affiche le menu dans le quelle les multiples choix sont afficher
       print("1.addition(+)")
       print("2.soustraction(-)")
       print("3.multiplication(*)")
       print("4.division(/)")
       print("5.quitter")
#ici on choisi notre operation
       operation=input("entrer votre operation (1-5):")
#si le choix est 5 l'operation s'arrete immediatement
       if operation=='5':
          break
#cette operation s'effectue jusqu'a ce qu'on le quite d'ou l'utilisation de la bocle while.
       try:
          a=float(input("entrer le premier nombre:"))
          b=float(input("entrer le deuxieme nombre:"))
       except ValueError:
          print("choix non valide reesayer")
          continue
       if operation=="1":
          print(a+b)
       elif operation=="2":
          print(a-b)
       elif operation=="3":
          print(a*b)
       elif operation=="4":
          print(a/b)
       else:
          print("choix non valable")
calculette()
