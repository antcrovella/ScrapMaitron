import urllib.request as urlReq
image = urlReq.urlopen("http://bataille.bouvines.free.fr/images/imagvitraux/blasonv01a.jpg")
source = image.read()

fichier = open("/users/antoinecrovella/Documents/Programmation/image.jpg", "bw")
fichier.write(source)
fichier.close()

