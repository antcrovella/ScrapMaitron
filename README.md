# ScrapMaitron

Le but du programme est de récupérer automatiquement un ensemble de fiches issues du Maitron, dictionnaire biographique du mouvement ouvrier. Ce programme vise à récupérer un grand nombre de fiches, et non une seule. Ainsi, il doit être utilisé à partir d'une page de résultat obtenu grâce à une recherche ou une recherche avancée.

## Présentation du code

Le code est composé d'une fonction principale, "noticesMaitron", appelée dans le programme. Celle-ci prend trois variables : 
lienPage, soit le lien de la page de résultat où se trouvent les notices à scrapper.
nbPage, soit le nombre de pages à télécharger depuis cette page de résultat.
mode, soit le mode utilisé pour le téléchargement, celui-ci est, sans autres indications, automatiquement sur "1".

Après avoir importé les différentes bibliothèques utilisées dans ce programme, les variables générales de la fonction sont définies :
chemin, soit l'endroit sur l'ordinateur où le document .txt doit être sauvegardé, avec la date qui s'ajoute automatique.
contenuFichierSortie, soit le contenu de ce document .txt avant que les notices y soient inscrites.
i et y, deux compteurs permettant de renvoyer l'information de l'avancement du programme à l'utilisateur et d'arrêter le programme en conformité avec le nombre de pages à scrappé défini par l'utilisateur. i pour les notices, y pour les pages.

