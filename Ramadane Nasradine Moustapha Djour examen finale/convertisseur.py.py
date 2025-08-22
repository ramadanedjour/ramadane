resultats=0
temperature=int(input("entrer in temperature:"))
unite=str(input("entrer l'unité"))
conversion=str(input("la conversion voulue"))
if unite==c and conversion==f:
    resultats=unite*(9/5)+32
    print(resultats)
elif unite==f and conversion==c:
    resultats=(unite-32)*5/9
    print(resultats)
elif unite==c and conversion==k:
    resultats=unite+273.15
else:
    print("erreur!")
