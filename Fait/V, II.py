chemin = "/users/antoinecrovella/Documents/Programmation/boucles/territoire.txt"
##Isoler les informations, nom de la région et date de son ajout. Considérer un nombre pour piuvoir le comparer aux bornes chronologiques.

fichierAgrendissements = open(chemin)
texteAgrandissements = fichierAgrendissements.read()

borneChronoInf = input("Quelle borne chronologique inférieure ? : ")
borneChronoInf = int(borneChronoInf)
borneChronoSup = input("Quelle borne chronologique supérieure ? : ")
borneChronoSup = int(borneChronoSup)

agrandissements = texteAgrandissements.splitlines()

for chaqueAgrandissement in agrandissements:
    infoAgrandissement = chaqueAgrandissement.split(" : ")
    date = int(infoAgrandissement[0])
    territoire = infoAgrandissement[1]
    if borneChronoInf <= date and date <= borneChronoSup:
        print(f"{territoire} en {date}.")
