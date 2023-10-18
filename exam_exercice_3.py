#je génère un tableau
myTable=[3,1,6,10,5,9,2,8,7,4]

#je défini une variable stock
stock=0

print("Voici votre tableau :")
print(myTable)

#je parcours mon tableau dans son entièreté
for i in range (9):
    j=0
    for j in range (9):
        #je compare la valeur à la position i avec la valeur en position i+1
        #si elle est supérieure, j'inverse leurs positions
        if myTable[j]>myTable[j+1]:
            #j'inverse mes valeurs à l'aide du stock
            stock=myTable[j+1]
            myTable[j+1]=myTable[j]
            myTable[j]=stock

print ("Voici le tableau trié par ordre croissant :")
print(myTable)