# Premier lien utilisé = "https://maitron.fr/spip.php?page=recherche_avanc&swishe_type1=phrase1&swishe_from1=full1&swishe_exp1=section+speciale&multi1=et1&swishe_type2=phrase2&swishe_from2=full2&swishe_exp2=Paris&multi2=et2&swishe_type3=phrase3&swishe_from3=full3&swishe_exp3=&swishe_option=tout&typetri=triA&swishe_mot_op_periode=or&swishe_mot%5B%5D=periode.26&swishe_mot%5B%5D=periode.3&swishe_mot_op_dico=or&swishe_mot_op_pro=or&swishe_mot_op_dep=or&swishe_mot_op_int=or&OK=Envoyer"


# Creation de la fonction
def noticesMaitron(lienPage, nbPage, mode=1):
    # Importation des bibliothèques utilisées
    import urllib.request as urlReq
    from bs4 import BeautifulSoup as bs
    import re
    import datetime

    # Définition des variables générales de la fonction
    chemin = f"/users/antoinecrovella/Documents/Master/Outils de la recherche/M2/Programmation/Projet/NoticesSiteMaitron{datetime.datetime.now()}.txt"
    contenuFichierSortie = (f"Ensemble des notices du Maitron où il est fait mention des termes 'section speciale'\nLien de recherche utilisé pour le scrapping : {lienPage}\n\n\n")
    i = 0
    y = 0

    # Definition d'une fonction utilisée dans le code
    def findBalisesNotice():
        return soupe.find("div", class_="notice-texte entry").findAll("p")

    # Renvoi de l'avancement
    print(f"Début du scrapping")

    while y < int(nbPage):

        # Renvoi de l'avancement
        y = y + 1
        print(f"\n Page n°{y} en traitement\n")

        # Lecture de la page de recherche
        page = urlReq.urlopen(lienPage)
        source = page.read()
        soupe = bs(source, features="html.parser")

        # Récupération les liens des articles présents sur la page de recherche
        resultatRecherche = soupe.find("div", class_="resultats-recherche")
        elementsListe = resultatRecherche.findAll("li")

        # Récupération des informations de chaque notice
        for chaqueElementListe in elementsListe:
            lien = chaqueElementListe.a["href"]

            try:
                page = urlReq.urlopen(lien)
                source = page.read()
                soupe = bs(source, features="html.parser")

                # Titre de la notice
                titre = soupe.find("h1", class_="notice-titre")
                titre = titre.text

                # Eléments de l'introduction
                intro = soupe.find("div", class_="intro")
                intro = intro.text

                # Renvoi de l'avancement
                i = i + 1
                print(f'{i}. {titre}')

                texteNotice = ""

                # Importation des éléments de la notice dans le cas du choix du mode "simplifié"
                if mode == 1:
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nLien notice : {lien}\n\n\n"


                # Ecriture des paragraphes où apparaissent l'ensemble de mots "section spéciale" dans le cas du choix du mode "paragraphe"
                if mode == 2:
                    for chaqueBalise in findBalisesNotice():
                        texteBalise = chaqueBalise.text
                        if re.findall("s.ction sp.ciale|S.ction sp.ciale|S.ction Sp.ciale|s.ction Sp.ciale", texteBalise):
                            texteNotice = texteNotice + texteBalise
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nParagraphe(s) où la mention 'section spéciale' apparaît : \n{texteNotice}\n\nLien notice : {lien}\n\n\n"

                # Écriture de la notice dans le cas du choix du mode "complet"
                if mode == 3:
                    for chaqueBalise in findBalisesNotice():
                        texteBalise = chaqueBalise.text
                        texteNotice = texteNotice + texteBalise
                    contenuFichierSortie = contenuFichierSortie + f"{i}. {titre}\n\nTexte intro : {intro}\n\nTexte notice : {texteNotice}\n\nLien notice : {lien}\n\n\n"

    # Cas où les liens ne sont pas utilisables
            except:
                i = i + 1
                print(f"La fiche n°{i} n'a pas pu être téléchargée")
                contenuFichierSortie = contenuFichierSortie + f"La fiche n°{i} de la page {y} n'a pas pu être téléchargée, le lien suivant n'a pas fonctionné : {lien}\n\n"
                continue

    # Passage à la page de recherche suivant
        page = urlReq.urlopen(lienPage)
        source = page.read()
        soupe = bs(source, features="html.parser")
        pagination = soupe.find("p", class_="pagination-resultats")
        balisesPagination = pagination.findAll("a")
        for chaqueBalise in balisesPagination:
            texteBalise = chaqueBalise.text
            if re.findall("suivant", texteBalise):
                nouveauLien = chaqueBalise["href"]
                lienPage = "https://maitron.fr" + nouveauLien

    # Écriture du fichier
    fichier = open(chemin, "w+")
    fichier.write(contenuFichierSortie)
    fichier.close()

    # Fin du programme
    print(f"\n Scrapping terminé, {y} pages ont été importées \n")


# Appel de la fonction pour une utilisation par l'utilisateur
lienPage = input("Quel lien souhaitez-vous utiliser ? : \n")
nbPage = int(input("Quel nombre de pages souhaitez-vous scrapper ? : \n"))
print("1. Mode simplifié")
print("2. Mode paragraphe")
print("3. Mode complet \n ")
mode = int(input("Quel mode souhaitez-vous utiliser ? : \n"))
noticesMaitron(lienPage, nbPage, mode)