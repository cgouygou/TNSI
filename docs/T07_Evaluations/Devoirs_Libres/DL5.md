# DL 0101: AOC22 day 7

!!! capytale "Lien vers l'activité Capytale"
    Devoir à faire et à rendre ici : [https://capytale2.ac-paris.fr/web/c/f1db-1133073](https://capytale2.ac-paris.fr/web/c/f1db-1133073){:target="_blank"} 


L'objectif de ce DL est de résoudre l'épreuve du [day 7 d'AOC 2022](https://adventofcode.com/2022/day/7){:target="_blank"} .

Les données d'entrée sont dans [ce fichier](../data/input_day7.txt){:target="_blank"}.

!!! gear "Stratégie"
    1. Réprésenter les données avec un modèle adapté.
    2. Parcourir le fichier pour construire les données.
    3. Analyser les données pour trouver la solution.

!!! info "Indications"
    === "Lecture du fichier"
        On lit le fichier et on récupère les lignes dans une liste `data` (par ex.) avec:

        ```python
        data = open("input_day7.txt").read().splitlines()
        ```

    === "Représentation des données"        
        On crée une classe `Repertoire`, qui possède 4 attributs (à vous de les trouver) et plusieurs méthodes:

        - une méthode pour ajouter un fichier au répertoire;
        - une méthode pour ajouter un (sous-)répertoire au répertoire;
        - une méthode pour calculer la taille du répertoire (méthode récursive), qui correspond à la somme de la taille de ses fichiers et des tailles de ses sous-répertoires;
        - une méthode pour récupèrer un sous-répertoire à partir de son nom.

    === "Parcours des données"
        On parcourt les données pour construire l'arborescence du répertoire «home» `\`, en identifiant les actions à effectuer en fonction de la chaîne de caractère sur chaque ligne. Penser à gérer le **répertoire courant**.

        **Aide pour le parcours**: compléter les actions à effectuer en fonction de ce qui est lu dans le fichier (sachant qu'il n'y a rien à faire si la commande est `$ ls`) et que le `#!py else` correspond au dernier cas non envisagé...
        ```python linenums='1'
        for line in data[1:]:
            if line == '$ cd ..':
                ...
            elif line[:5] == '$ cd ':
                dir_name = line.split()[-1]
                ...
            elif line == '$ ls':
                pass
            elif line[:3] == 'dir':
                ...
            else:
                ...
        ```
        

    === "Analyse des données"
        Créer une fonction récursive qui prend en paramètre un répertoire, ajoute sa taille (si elle convient) à une variable (de type `list`) **globale** puis examine ses sous-dossiers de la même façon.

        **Aide pour la fonction récursive**
        ```python linenums='1'
        tailles = []

        def exploration(rep:Repertoire) -> None:
            t = rep.size()
            if t ... :
                tailles.append(..)
            for sous_rep in ... :
                ...(sous_rep)

        exploration(home)
        print(sum(...))
        ```
        


!!! check "Test du programme"
    Comme indiqué dans l'énoncé sur le site d'AOC 2022, avec le [fichier d'entrée d'exemple](../data/input_day7.txt){:target="_blank"}, vous devez obtenir deux valeurs (94853 et 584) pour une réponse finale de 95437.