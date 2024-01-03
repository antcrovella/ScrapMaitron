listeLettres = {"a", "b", "c", "d", "e"}
#for lettres in liste:
    #print(lettres)

for lettres in enumerate(listeLettres):
    numero = lettres[0]
    item = lettres[1]
    print("Lettre n° " + str(numero+1) + " : " + item)
print("Fin de la liste")

nouvelleListe= enumerate(listeLettres)
nouvelleListe.reverse(" ")
for lettres in enumerate(nouvelleListe):
    numero = lettres[0]
    item = lettres[1]
    print("Lettre n° " + str(numero+1) + " : " + item)

