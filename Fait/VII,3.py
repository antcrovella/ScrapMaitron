chemin = "/users/antoinecrovella/Documents/Programmation/DepensesEtat.csv"

#document = open(chemin)
#contenu = document.read()
#lignes = contenu.splitlines()

#for ligne in lignes:
    #items = ligne.split(";")
    #tableau.append(items)
#tableau = [ligne.split(";") for ligne in lignes]

tableau = []
def fichierCSV(chemin, séparateur=";"):
    document = open(chemin)
    contenu = document.read()
    lignes = contenu.splitlines()
    for ligne in lignes:
        items = ligne.split(séparateur)
        tableau.append(items)
    return tableau
