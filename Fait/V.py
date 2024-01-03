listeEtudiants = ["Aymeric", "Maxime", "Claire", "Anais"]

for etudiants in listeEtudiants:
    print(etudiants + " suit le cours de Python.")
#itération

for i in range(10):
    print(f"Itération n° {i}")
#générateur, génère à la demande des valeurs (i, j, k pour nom de compteur)

for etudiants in enumerate(listeEtudiants):
    numero = etudiants[0]
    nom = etudiants[1]
    print(str(numero) + " : " + nom)
print("\n\n")

#nbX = 10
#nbY = 10
#for i in range(1, nbX+1):
    #for j in range(1, nbY+1):
        #produit = str(i) + " x " + str(j) + " = " + str(i*j)
        #print(produit)

#while : condition qui tant qu'elle est vérifiée, la boucle va s'exécuter.
#i=0
#while True:
    #print(i)
    #i = i + 1

reponse = " "
listeNoms = []
while reponse != "FIN":
    reponse = input("Entrer un nom (ou “FIN“ pour terminer) : \n")
    if reponse != "FIN":
        listeNoms.append(reponse)
    else:
        print("Saisie terminée")
        break

#continue ignore les instruction qui précèdent
