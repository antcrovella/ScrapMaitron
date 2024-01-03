livres = float(input("Livres : "))
sous = float(input("Sous : "))
deniers = float(input("Deniers : "))

valeurMonetaire = livres + sous/20 + deniers/240
message = f"Vous avez actuellement {round(valeurMonetaire, 2)} livres."
print(message)
