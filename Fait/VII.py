#Créer et utiliser des fonctions, définir soit même des fonctions

def credits():
    print("A. Crovella, 2023")


def siecle(année):
    if année >= 1901 and année <= 2000:
        return("XX")
    if année >= 1801 and année <= 1900:
        return("XIX")

def age(annéeNaissance, annéeRef=2023):
    age = annéeRef - annéeNaissance
    return(ageCalculé)


def estNombre(mot):
    listeNb = ['O', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for caractère in mot:
        if caractère in listeNb:
            continue
        else:
            return(False)
    return(True)

#for mot in texte:
    #if estNombre(mot):
        #continue
    #lexique[mot] = lexique [mot] + 1


#Séparation ariables globales et locales
resultat = True

def falsifieResultat():
    resultat = False
    variableDansFonction = "Bonjour"
    print("Résultat falsifié !")

nbIndividus = 0
def enregistreIndividu(nom):
    global nbIndividus
    print(nom + "a été ajouté.")
    nbIndividus = nbIndividus +1
