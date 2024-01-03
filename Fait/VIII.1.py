import urllib.request as urlReq
page = urlReq.urlopen("http://les.barricades.free.fr/Histoire/semaineSang_hist.txt")
source = page.read()

#1ere option, écrire le fichier en mode bianaire("bw")
#fichier = open("/users/antoinecrovella/Documents/Programmation/semaineSanglante.txt", "bw")
#fichier.write(source)
#fichier.close()

#2eme option, décoder le fichier binaire
texte = source.decode("iso-8859-1")
fichier = open("/users/antoinecrovella/Documents/Programmation/semaineSanglante.txt", "w")
fichier.write(texte)
fichier.close()
