individus = {"Nom":["Crovella", "Palissot", "Latuile"], "Prenom":["Fabio", "Oscar", "Valerian"]}
numero = input("Numéro de l'individu recherché : \n")
i = int(numero)-1

nomRecherche = individus["Nom"][i]
print(f"Nom {nomRecherche}")
prenomRecherche = individus["Prenom"][i]
print(f"Prenom {prenomRecherche}")
