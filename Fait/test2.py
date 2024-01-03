tout = input("Le tout : ")
partie = input("La partie : ")

toutConverti = int(tout)
partieConvertie = int(partie)

resultat = ((partieConvertie * 100) / toutConverti)

resultatConverti = round(resultat, 2)

print("Votre résultat est : " + str(resultatConverti))

