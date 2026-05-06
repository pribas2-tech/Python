#Creem totes les variables

DNI=int(input("Quin es el teu DNI?"))
Article=float(input("Preu de l'article?"))
Descompte=float(input("Quin es el descompte?"))
IVA=float(input("quin es l'IVA?"))

#Fem el calcul del preu final

Preufinal=(Article+(Article*IVA/100))-(Article*Descompte/100)

#Mostrem el resultat

print(Preufinal)
