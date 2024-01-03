import urllib.request as urlReq

numeroFiche = 0
while numeroFiche < 5:
    numeroFiche = numeroFiche + 1
    numeroTexte = str(numeroFiche)
    try:
        fiches = urlReq.urlopen("https://collegiales.applirecherche.unilim.fr/index.php?i=fiche&j=" + numeroTexte)
        source = fiches.read().decode("utf-8")
        chemin = "/users/antoinecrovella/Documents/Programmation/Collègiales/collègiale"+numeroTexte+".html"
        fichier = open(chemin, "w")
        fichier.write(source)
        fichier.close()
    except urllib.error.URLError:
        print(f"Echec du téléchargement de la notice n° {numeroTexte}.")
        continue
