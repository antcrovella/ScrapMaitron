if (jour != "dimanche" and heure in [9:19]) or (jour == "dimanche" and heure in [9:19] and zoneTouristique == true)
    or (jours != "dimanche" and heure in [9:22] and nocturne == true)
    or (jour == "dimanche" and heure in [9:22] and zoneTouristique == True and nocture == True):
    print("Le magasin est ouvert.")
else
    print("Le magasin est fermé.")
