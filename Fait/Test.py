nom = input("Quel est votre prénom ? : ")
anneeNaissance = input("En quelle année êtes-vous né ? : ")
anneeConvertie = int(anneeNaissance)
anneeActuelle = 2023
age = anneeActuelle - anneeConvertie
message = "Bonjour " + nom + ", vous avez " + str(age) + " ans."
print(message)
