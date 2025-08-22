n=float(input("entrer un note entrer 0 et 20:"))
if n>20:
    print("syntaxe erreur")
else:
    if n>=10:
       print("passable")
    elif n>=12:
       print("a bien")
    else:
        if n>=16:
          print("excellent")
        else:
            print("insuffisant")
