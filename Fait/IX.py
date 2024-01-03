import urllib.request as urlReq
from bs4 import BeautifulSoup as bs

page = urlReq.urlopen("http://www.octavejulien.fr")
source = page.read()
soupe = bs(source, features="html.parser")

print("Affichage de l'élément <head>")
print(soupe.head)

print("\n")

print("Recherche des éléments <a>")
elements_a = soupe.findAll("a")

print("\n")

print("Affichage du texte du titre")
print(soupe.head.title.text)

print("\n")

print("Affichage du lien hypertexte de la 1e balise <a>")
print(soupe.find("a")["href"])

print("\n")

soupe.find("meta", attrs={"http-equiv":"Content-type"})["content"]


elements_a = soupe.findAll("a")
for element in elements_a:
    print(element["href"])
