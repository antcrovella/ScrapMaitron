#utiliser les fonctions d'une librairie spécifique (utiliser import) et donner un allias

import urllib.request as urlReq
page = urlReq.urlopen("http://www.octavejulien.fr")
encodage = page.info().get_content_charset()
source = page.read().decode(encodage)

