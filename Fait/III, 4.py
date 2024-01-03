#a
print("Texte complet")
chemin = "/users/antoinecrovella/Documents/Programmation/Poèmes/"
nom = input("Nom du poème à resumer : ")
fichier = open(chemin + nom + ".txt", "r")
contenu = fichier.read()
print(contenu, "\n")
lignes = contenu.splitlines()

#b
print("Texte résumé")
premiereLigne = lignes[2]
derniereLigne = lignes[-1]
print(f'La première ligne du poème est : "{premiereLigne}"')
print(f'La dernière ligne du poème est : "{derniereLigne}"')

#c
print("Mots")
mots = premiereLigne.split(" ")
premiersMots = mots[0:3]
mots = derniereLigne.split(" ")
derniersMots = mots[-3:]
print(f'Les premiers mots du poème sont : "{premiersMots}"')
print(f'Les derniers mots du poème sont : "{derniersMots}"')
