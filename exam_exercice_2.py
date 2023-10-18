#je génère un tableau
myTable=[5,9,6,7,1,10,2,8,4,3]

#je défini une variable stock
stock=0

print("Voici votre tableau :")
print(myTable)

#je parcours mon tableau
for i in range (9):
    #je compare la valeur à la position i avec la valeur en position i+1
    #si elle est supérieure, j'inverse leurs positions
    if myTable[i]>myTable[i+1]:
        #j'inverse mes valeurs à l'aide du stock
        stock=myTable[i+1]
        myTable[i+1]=myTable[i]
        myTable[i]=stock

print(myTable)