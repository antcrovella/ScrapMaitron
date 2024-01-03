def titrePage(url, mode="dictionnaire"): #mode contient "affichage" ou "dictionnaire"
    import urllib.request as urlReq
    from bs4 import BeautifulSoup as bs
    page = urlReq.urlopen(url)
    source = page.read()
    soupe = bs(source, features="html.parser")
    titre = soupe.head.title.text
    balisesMeta = soupe.findAll("meta")
    print(f"Titre : {titre}")
    dicoAttributs = {}
    message = ""
    for chaquebaliseMeta in balisesMeta:
        try:
            nomAttribut = chaquebaliseMeta["name"]
            valeurAttribut = chaquebaliseMeta["content"]
            dicoAttributs[nomAttribut] = valeurAttribut
            message = message + "\n" + f"{nomAttribut} : {valeurAttribut}"
            #Deux options de sortie, sous la forme d'un dictionnaire ou sous la forme d'un message à imprimer)
        except:
            continue
    if mode == "affichage":
        print(message)
    else:
        return(dicoAttributs)
