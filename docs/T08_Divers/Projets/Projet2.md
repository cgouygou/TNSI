# (Mini-) Projet 2

![](../images/meme_login.jpg){: .center width=320} 


!!! example "Authentification"
    === "Énoncé" 
        Dans ce mini-projet, vous devez écrire un système d'authentification par login/mot de passe à un service qui permet de stocker une phrase secrète. Comme précédemment le menu doit contenir trois choix:

        - **login** : s'authentifier puis afficher la phrase secrète. Proposer de changer cette phrase.
        - **register**: s'enregistrer puis saisir la phrase secrète à stocker.
        - **quit**: pour ... quitter le programme.

        **Remarques:**

        - les données doivent bien entendu être stockées dans une base de données.
        - on ne doit pas pouvoir choisir un login déjà utilisé.
        - les mots de passe doivent être hachés. Voir [ici](https://fr.wikipedia.org/wiki/Fonction_de_hachage){:target="_blank"}  pour le principe et [ici](https://docs.python.org/fr/3/library/hashlib.html){:target="_blank"} pour la fonction de hachage à utiliser.

        **Ouvertures:**

        - Proposer de changer le mot de passe.
        - Vérifier la force du mot de passe proposé (calcul d'entropie).

    === "Proposition de correction (a minima)" 

        
