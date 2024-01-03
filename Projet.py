#Premier lien utilisé = "https://maitron.fr/spip.php?page=recherche_avanc&swishe_type1=phrase1&swishe_from1=full1&swishe_exp1=section+speciale&multi1=et1&swishe_type2=phrase2&swishe_from2=full2&swishe_exp2=&multi2=et2&swishe_type3=phrase3&swishe_from3=full3&swishe_exp3=&swishe_option=tout&typetri=triA&swishe_mot_op_periode=or&swishe_mot%5B0%5D=periode.26&swishe_mot%5B1%5D=periode.3&swishe_mot_op_dico=or&swishe_mot_op_pro=or&swishe_mot_op_dep=or&swishe_mot_op_int=or&OK=Envoyer&swishe_depart=0&swishe_nbParPage=15"
#Définition du premier lien utilisé issu d'une recherche avancée précisant les variables recherchées (ici toutes les notices où "section speciale" apparaît)

lienPage = input("Quel lien souhaitez-vous utiliser ? : \n")

def noticesMaitron(lienPage, nbPage, mode="simplifié"):
    import urllib.request as urlReq
    from bs4 import BeautifulSoup as bs
    import re
    chemin = "/users/antoinecrovella/Documents/Programmation/Projet/NoticesSiteMaitron.txt"
    contenuFichierSortie = "Ensemble des notices du Maitron où il est fait mention des termes 'section speciale'\n\n\n"
    i = 0
    y = 0
    print(f"Début du scrapping")

    while y < nbPage:

    #Renvoi de l'avancement
        print(f"\n Page n°{y+1} en traitement\n")

    #Lecture de la page de recherche
        page = urlReq.urlopen(lienPage)
        source = page.read()
        soupe = bs(source, features="html.parser")

    #Récupération les liens des articles présents sur la page de recherche
        resultatRecherche = soupe.find("div", class_="resultats-recherche")
        elementsListe = resultatRecherche.findAll("li")

    #Récupération des informations de chaque notices
        for chaqueElementListe in elementsListe:
            lien = chaqueElementListe.a["href"]

            try:
                page = urlReq.urlopen(lien)
                source = page.read()
                soupe = bs(source, features="html.parser")

                #Titre de la notice
                titre = soupe.find("h1", class_="notice-titre")
                titre = titre.text

                #Eléments de l'introduction
                intro = soupe.find("div", class_="intro")
                intro = intro.text

                #Renvoi de l'avancement
                i = i + 1
                print(f'{i}. {titre}')

                #Ecriture de la notice dans le cas du choix du mode "complet"
                if mode == "complet":
                    notice = soupe.find("div", class_="notice-texte entry")
                    balisesNotice = notice.findAll("p")
                    texteNotice = ""
                    for chaqueBalise in balisesNotice:
                        texteBalise = chaqueBalise.text
                        texteNotice = texteNotice + texteBalise
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nTexte notice : {texteNotice}\n\nLien notice : {lien}\n\n\n"

                #Ecriture des paragraphes où apparaissent l'ensemble de mots "section spéciale" dans le cas du choix du mode "paragraphe"
                if mode == "paragraphe":
                    notice = soupe.find("div", class_="notice-texte entry")
                    balisesNotice = notice.findAll("p")
                    texteParagraphe = ""
                    for chaqueBalise in balisesNotice:
                        texteBalise = chaqueBalise.text
                        if re.findall("s.ction sp.ciale", texteBalise) or re.findall("S.ction sp.ciale", texteBalise) or re.findall("S.ction Sp.ciale", texteBalise) or re.findall("s.ction Sp.ciale", texteBalise):
                            texteParagraphe = texteParagraphe + texteBalise
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nParagraphe(s) où la mention 'section spéciale' apparaît : {texteParagraphe}\n\nLien notice : {lien}\n\n\n"

                #Importation des éléments de la notice dans le cas du choix du mode "simplifié"
                if mode == "simplifié":
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nLien notice : {lien}\n\n\n"

    #Cas où les liens ne sont pas utilisables
            except:
                i = i + 1
                print(f"La fiche n°{i} n'a pas pu être téléchargée")
                contenuFichierSortie = contenuFichierSortie + f"La fiche n°{i} de la page {y} n'a pas pu être téléchargée, le lien suivant n'a pas fonctionné : {lien}\n\n"
                continue

    #Passage à la page de recherche suivant
        page = urlReq.urlopen(lienPage)
        source = page.read()
        soupe = bs(source, features="html.parser")
        pagination = soupe.find("p", class_="pagination-resultats")
        liensPagination = pagination.findAll("a")
        lienNouvellePage = liensPagination[-2]
        nouveauLien = lienNouvellePage["href"]
        lienPage = "https://maitron.fr" + nouveauLien
        y = y + 1

    #Ecriture du fichier
    fichier = open(chemin, "w+")
    fichier.write(contenuFichierSortie)
    fichier.close()

    #Fin du programme
    print(f"\n Scrapping terminé, {y-1} pages ont été importées \n")
