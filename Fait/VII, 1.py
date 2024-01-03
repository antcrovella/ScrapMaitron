def traceLigne(longueurLigne=10):
    ligne = longueurLigne * "_"
    print(ligne)

def traceRectangle(hauteur, largeur):
    blancs = (largeur-2) * " "
    vertical = (hauteur - 2) * ("|" + blancs + "|" + "\n")
    horizontal = "+" + (largeur - 2) * "_" + "+"
    print("\n" + horizontal + "\n" + vertical + horizontal)
