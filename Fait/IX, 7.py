import urllib.request as urlReq
from bs4 import BeautifulSoup as bs

i=1
lien = "http://plunkett.hautetfort.com/archive/2007/04/30/turquie-europe-le-malaise-augmente.html"

contenuFichierSortie = "Titre;NbCommentaires\n"

while i<=10:
    page = urlReq.urlopen(lien)
    source = page.read()
    soupe = bs(source, features="html.parser")


    #Récuperer le nombre de commentaires
    commentaire = soupe.findAll("div", class_="commentparent")
    nbCommentaires = len(commentaire)

    #Récuperer le titre
    titreArticle = soupe.find("h3", id="p1")
    titreArticle = titreArticle.text
    print(f"{i}, {titreArticle}")

    #Ecriture des informations
    ligne = f'{titreArticle};{nbCommentaires}\n'
    contenuFichierSortie = contenuFichierSortie + ligne

    #Lien précédant
    nouveauLien = soupe.find("link", rel="prev")
    if nouveauLien == None:
        print("Dernière page atteinte")
        break
    lien = nouveauLien["href"]

    i=i+1

fichierSortie = open(f"/users/antoinecrovella/Documents/Programmation/infoBlog.csv", "w")
fichierSortie.write(contenuFichierSortie)
fichierSortie.close()
