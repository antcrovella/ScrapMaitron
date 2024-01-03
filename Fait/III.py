contenu = input("Entrez le texte : ")
nomFichier = input("Entrez le nom du fichier : ")

chemin = "/users/antoinecrovella/Documents/Programmation/"


fichier = open(chemin + nomFichier + ".txt", "w+")
fichier.write(contenu)
fichier.close()
