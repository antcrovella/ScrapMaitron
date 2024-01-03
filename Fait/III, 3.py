cheminDossier = "/users/antoinecrovella/Documents/Programmation/noticesBio/"
nomFichier = input("Quel fichier voulez-vous :")
fichier = open(cheminDossier + nomFichier + ".txt", "r")
contenu = fichier.read()
elements = contenu.splitlines()

nom = elements[0]
pays = elements[1]
dateDeNaissance = elements[2]

if len(elements) == 4:
    dateDeDeces = elements[3]
    age = dateDeDeces - dateDeNaissance
    nouveauContenu = f"{nom} : né en {dateDeNaissance} en {pays}, mort en {dateDeDeces} à l'âge de {age}"
    print(nouveauContenu)

else:
    nouveauContenu = f"{nom} : né en {dateDeNaissance} en {pays}, mort à une date inconnue et à un âge inconnu."
    print(nouveauContenu)

nouveauFichier = open(cheminDossier + "Nouveau" + nomFichier + ".txt", "w")
nouveauFichier.write(nouveauContenu)
nouveauFichier.close()
