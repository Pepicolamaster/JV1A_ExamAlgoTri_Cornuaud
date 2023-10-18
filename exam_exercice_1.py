#je génère un tableau
myTable=[5,9,6,7,1,10,2,8,4,3]

#je défini une variable stock
stock=0

print("Voici votre tableau :")
print(myTable)

#je demande la position des valeurs qui vont être échangées
premierIndice=int(input("Choissisez la position de la première valeur à échanger dans le tableau."))
deuxiemeIndice=int(input("Choissisez la position de la deuxième valeur à échanger dans le tableau."))

#j'inverse mesz valeurs à l'aide du stock
stock=myTable[premierIndice]
myTable[premierIndice]=myTable[deuxiemeIndice]
myTable[deuxiemeIndice]=stock

print(myTable)