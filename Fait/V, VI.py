import os
cheminDossier = "/users/antoinecrovella/Documents/Programmation/boucles/Discours"
ensembleDiscours = os.listdir(cheminDossier)
ContenuEnsembletexte = ""

for fichier in ensembleDiscours:
    if fichier != ".DS_Store" :
        discours = open("/users/antoinecrovella/Documents/Programmation/boucles/Discours/"+fichier)
        texte = discours.read()
        ContenuEnsembletexte = ContenuEnsembletexte + texte + "\n"

nouveauFichier = open("/users/antoinecrovella/Documents/Programmation/boucles/Discours/"+"Ensemble_discours", "w")
nouveauFichier.write(ContenuEnsembletexte)
nouveauFichier.close()
