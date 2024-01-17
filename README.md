# ScrapMaitron

Le but du programme est de récupérer automatiquement un ensemble de fiches issues du Maitron, dictionnaire biographique du mouvement ouvrier. Ce programme vise à récupérer un grand nombre de fiches, et non une seule. Ainsi, il doit être utilisé à partir d'une page de résultat obtenu grâce à une recherche ou une recherche avancée.

Attention : ne pas confondre les notices (fiches propres à chaque individu) et les pages (une page contient au maximum 15 notices, elle est obtenue après une recherche)

![ImageSiteMaitron](https://github.com/antcrovella/ScrapMaitron/assets/155578364/73f477c4-65fd-45a6-b51b-8bd2dea6edbe)

## Présentation du code

### Variables générales et arguments définis par l'utilisateur

Le code est composé d'une fonction principale, "noticesMaitron", appelée dans le programme. Celle-ci prend trois arguments : \
lienPage, soit le lien de la page de résultat où se trouvent les notices à scrapper. \
nbPage, soit le nombre de pages à télécharger depuis cette page de résultat. \
mode, soit le mode utilisé pour le téléchargement, celui-ci est, sans autres indications, automatiquement sur "1".

Après avoir importé les différentes bibliothèques utilisées dans ce programme, les variables générales de la fonction sont définies : \
chemin, soit l'endroit sur l'ordinateur où le document .txt doit être sauvegardé, avec la date qui s'ajoute automatique. \
contenuFichierSortie, soit le contenu de ce document .txt avant que les notices y soient inscrites. \
i et y, deux compteurs permettant de renvoyer l'information de l'avancement du programme à l'utilisateur et d'arrêter le programme en conformité avec le nombre de pages à scrapper défini par l'utilisateur. i pour les notices, y pour les pages.
 
Nous définissons ensuite une nouvelle fonction, findBalisesNotice. Utilisée à plusieurs reprises dans le programme, elle permet de retrouver dans les différentes notices les balises "p" contenant le texte du celles-ci.

### Boucle while

Pour faire fonctionner notre programme, nous utilisons une boucle while. Celle-ci s'exécute tant que la valeur du compteur y (dont la valeur augmente à chaque itération) est inférieure à la valeur de l'argument nbPage, définie par l'utilisateur. Cette condition permet de scrapper le nombre de pages demandées par l'utilisateur, le programme s'arrêtant une fois que cette valeur a été atteinte.

Le programme lit la page de recherche (variable page) et récupère, pour chacune des notices présentes sur celle-ci, la balise "li" contenant le lien de chaque notice.

### Boucle for/in

À l'aide d'une boucle, le programme va donc prendre chacune des balises contenues dans la variable elementsListe et y récupérer l'élément href, soit le lien de chaque notice (variable lien).

#### Élements toujours repris

La page contenant la notice va être lue, et vont y être extrait, à chaque itération, les éléments suivants : \
Le titre de la notice (variable titre). \
Le chapeau introducteur (variable intro). \

#### fonction if et modes d'utilisation

À l'aide de la fonction if, le programme, selon le choix de l'utilisateur, ne télécharge pas la même chose de la notice. \
1. Dans le cas du mode numéro 1, le programme ne va inscrire sur le fichier .txt que le titre, l'introduction et le lien de la notice.
2. Dans le cas du mode numéro 2, le programme inscrit les mêmes données que le mode numéro 1 en y rajoutant les paragraphes du corps du texte de la notice où l'ensemble "section spéciale" apparaît. À l'aide d'une boucle et grâce aux expréssions régulières, le programme lit chacun des textes présents dans les balises "p" (fonction findBalisesNotice définie au début du programme) et ne garde dans le fichier .txt que ceux où l'ensemble section spéciale apparaît. Que cet ensemble soit écrit avec ou sans majuscules et accents. 
3. Dans le cas du mode numéro 3, le programme inscrit l'ensemble de la notice dans le fichier .txt soit le titre, l'introduction, le lien et l'ensemble des paragraphes de la notice, même s'ils ne contiennent pas tous l'ensemble "section spéciale".

### Try/Except

L'ensemble des tâches décrites précédemment et exécutées par le programme ne se réalisent que dans le cas où ce dernier à réussit à ouvrir la page de la notice. Dans le cas où un des liens (balise "li") présent sur la page de recherche n'est pas utilisable (ce qui arrive parfois), le programme le notifie à l'utilisateur et continue la boucle.

### Passage à une nouvelle page

Pour passer à une nouvelle page de recherche automatiquement, le programme va chercher les différentes balises "pagination-resultats" et ne retient dans celles-ci, à l'aide d'une boucle et de l'utilisation d'une expréssion régulière, que celle dont le nom de la balise contient le mot "suivant" pour effectivement passer à la page suivante, et non une autre page de recherche. 

### Écriture du fichier et fin du programme

Une fois la boucle while achevée, le programme écrit l'ensemble des données récoltées (variable contenuFichierSortie) dans un fichier .txt. Le programme renvoie enfin à l'utilisateur que ce dernier est terminé.

### Appel de la fonction

L'appel de la fonction permet à l'utilisateur de définir les arguments présentées dans la sous-partie "variables générales". 

## Utilisation

Pour utiliser ce programme il faut vous rendre sur le site du maitron (https://maitron.fr) et effectuer une recherche ou une recherche avancée (dans notre cas la recherche effectuée cherche toutes les notices où "section spéciale" et "Paris" apparaissent dans la notice, le résultat de cette recherche nous donne le lien suivant : https://maitron.fr/spip.php?page=recherche_avanc&swishe_type1=phrase1&swishe_from1=full1&swishe_exp1=section+speciale&multi1=et1&swishe_type2=phrase2&swishe_from2=full2&swishe_exp2=Paris&multi2=et2&swishe_type3=phrase3&swishe_from3=full3&swishe_exp3=&swishe_option=tout&typetri=triA&swishe_mot_op_periode=or&swishe_mot%5B%5D=periode.26&swishe_mot%5B%5D=periode.3&swishe_mot_op_dico=or&swishe_mot_op_pro=or&swishe_mot_op_dep=or&swishe_mot_op_int=or&OK=Envoyer. Une fois obtenu le premier lien de la page de recherche, il vous suffit de choisir le nombre de pages que vous souhaitez télécharger et le mode d'utilisation. Un exemple des résultats obtenus pour chaque mode est consultable dans le dossier résultats requête. 
