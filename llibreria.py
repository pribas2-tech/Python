#Variables 1a part

material = []
preuArticle = []
preu = 0
materials = None


#Variables 2a part

material_Comprar = 1
preuComprar = []
materialComprar = []
preu_Final = 0


#1a part

while materials != "$":
    materials = input("Quins materials vols? ")
    
    if materials == "$":
        break
    material.append(materials)                              #Anexem el material a el array
    preu = float(input("Quin es el preu del material? "))
    preuArticle.append(preu)                                #Anexem el preu a el array


print("MATERIAL \n")
for i in range(len(material)):                              #Fem que recorri tot l'array
    print(f"{i+1}-{material[i]}--{preuArticle[i]}€")        


#2a part 


while material_Comprar != 0:
    material_Comprar = int(input("Escull un numero del material que vols comprar ")) #A els array nomes es poden utilitzar int no FLOAT
    if material_Comprar == 0:
        break
    materialComprar.append(material[material_Comprar-1])      #Posem -1 perque l'array comença al 0 i la taula que es mostra a el 1
    preuComprar.append(preuArticle[material_Comprar-1])


#Preu Final
preu_Final=sum(preuComprar)
print(f"\nEl preu final es {preu_Final}")
    

