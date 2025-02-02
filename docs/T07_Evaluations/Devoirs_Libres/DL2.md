# DL 0010: No space left on device

**Énoncé inspiré de l'épreuve «Day 7» de l'[Advent of Code 2022](https://adventofcode.com/2022){:target="_blank"}.**

*Thèmes abordés: commandes UNIX, structure d'arbre, POO, récursivité*

![](../images/meme_space.jpg){: .center width=320} 

Un ami vous confie - en tant qu'expert·e UNIX - un appareil qui dysfonctionne pour le réparer. Vous tentez d'exécuter une mise à jour du système mais vous obtenez le message d'erreur suivant:

```bash
Error: No space left on device
```

Peut-être pouvez-vous supprimer des fichiers pour faire de la place pour la mise à jour ?

Vous naviguez sur le système de fichiers pour évaluer la situation et vous sauvegardez la sortie du terminal. Par exemple (les lignes qui commencent par `$` sont les commandes que vous avez exécutées):

```bash
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
```

!!! question "Question 1"
    Rappeler le sens et l'utilisation des commandes `cd` et `ls` dans un système UNIX.

Compte tenu des commandes et de la sortie dans l'exemple ci-dessus, vous pouvez déterminer que le système de fichiers ressemble visuellement à l'arborescence suivante (dir (directory) → répertoire, file → fichier, les tailles sont en octets):

```
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
```

Ici, il y a quatre répertoires : `/` (le répertoire racine), `a` et `d` (qui sont dans le répertoire `/`), et `e` (qui est dans `a`). Ces répertoires contiennent également des fichiers de différentes tailles.

Puisque le disque est plein, votre première étape devrait probablement être de trouver des répertoires qui sont de bons candidats à la suppression. Pour ce faire, vous devez déterminer la taille totale de chaque répertoire. La taille totale d'un répertoire est la somme des tailles des fichiers qu'il contient directement, ou indirectement (c'est-à-dire dans ses sous-répertoires). Les répertoires eux-mêmes ne comptent pas comme ayant une taille intrinsèque.

Par exemple, la taille totale du répertoire `e` est 584 puisqu'il ne contient qu'un seul fichier de taille 584.

!!! question "Question 2"
    1. Vérifier que la taille totale du répertoire `a` est 94853.
    2. Donner la taille des répertoires `d` et `/`.

Au travail maintenant. Vous optez pour la stratégie suivante:

1. Choisir un modèle adapté pour représenter les données (vous choisissez de construire une classe `Repertoire` qui reprend une structure d'arbre).
2. Parcourir le [fichier de sortie du terminal](../data/sortie_terminal.txt) pour construire les données.
3. Analyser les données pour sélectionner seulement les répertoires dont la taille totale est inférieure à 100000.

!!! question "Questions 3 à 6"
    === "Question 3: les attributs"
        La classe `Repertoire` comporte 4 attributs:

        - un attribut `nom`, de type `#!py str`, correspondant au nom du répertoire (par exemple `'/'`, `'a'`, etc.) et donné en paramètre du constructeur;
        - un attribut `parent`, de type `#!py Repertoire`, correspondant au répertoire parent (par exemple `'/'` pour `'a'`, `'a'` pour `'e'` et `#!py None` pour `'/'`) et donné en paramètre du constructeur;
        - un attribut `enfants`, de type `#!py list` et vide par défaut, qui contiendra la liste des répertoires enfants;
        - un attribut `fichiers`, de type `#!py list` et vide par défaut, qui contiendra **la taille** des fichiers directement contenus dans le répertoire.

        Dans le code à compléter ci-dessous:

        1. Compléter le constructeur `#!py __init__` de la classe `Repertoire`.
        2. Dans la partie *Création des données*, instancier l'objet `racine` correspondant au répertoire... racine.

    === "Question 4: les méthodes"
        La classe `Repertoire` comporte 4 méthodes:

        - une méthode `ajoute_fichier` qui prend en paramètre une taille de fichier et l'ajoute à l'attribut `fichiers`;
        - une méthode `ajoute_enfant` qui prend en paramètre un répertoire et l'ajoute à l'attribut `enfants`;
        - une méthode `selection_enfant` qui prend en paramètre un nom de répertoire et renvoie le répertoire parmi les enfants qui correspond à ce nom;
        - une méthode `taille` qui calcule et renvoie la somme des tailles des fichiers contenus dans le répertoire et des tailles des répertoires enfants. Cette fonction est donc récursive.
        

        Compléter le code de ces 4 méthodes.

        **Remarque:**  pour la méthode `taille`, on peut utiliser la fonction `#!py sum` qui renvoie la somme des éléments d'une liste donnée en paramètre. Vous pouvez réécrire complètement cette méthode sans l'utiliser, ou l'utiliser pour l'écrire en une seule ligne avec une liste en compréhension.

    === "Question 5: la création des données"
        Il s'agit maintenant de lire le fichier texte contenant les instructions et leurs résultats en console.

        Pour cela le fichier est chargé dans une variable `donnees` qui contient **une liste** dont les éléments sont les chaînes de caractères correspondant à chaque ligne du fichier. L'instruction suivante supprime la première ligne, inutile ici.

        Avec l'exemple de l'introduction, la variable `donnees` serait donc la suivante:

        ```python linenums='1'
        ["$ ls", "dir a", "14848514 b.txt", "8504156 c.dat", "dir d", "$ cd a", ..., "7214296 k"]
        ```

        Le principe est bien entendu de parcourir cette liste, et d'agir en fonction de la chaîne de caractères lue: ajouter un répertoire enfant, ajouter des fichiers ou se déplacer dans l'arborescence des répertoires. **Il est donc impératif de gérer le répertoire courant !**

        - la chaîne **est** `#!py "$ cd .."`: on gère le répertoire courant;
        - la chaîne **commence par** `#!py "$ cd"` : on gère le répertoire courant en sélectionnant le répertoire grâce son nom;
        - la chaîne est `#!py $ ls`: il n'y a rien à faire:
        - la chaîne **commence par** `#!py "$ dir"` : on ajoute un répertoire enfant;
        - sinon la chaîne correspond à un fichier...
        
        !!! code "Rappel"
            La méthode `#!py split` permet de scinder une chaîne de caractères sur les caractères espaces et de récupérer une liste des «morceaux». Voir [ici](https://cgouygou.github.io/1NSI/T08_Extras/4Divers/4Chaines/Strings/){:target="_blank"} par exemple.

            En particulier, `#!py ligne.split()[0]` permet de récupérer la chaîne des caractères de la variable `ligne` jusqu'au premier caractère espace, et `#!py ligne.split()[-1]` permet de récupérer la chaîne des caractères de la variable `ligne` du dernier caractère espace jusqu'à la fin:

            ```python
            >>> ligne = "la nsi c'est la vie"
            >>> ligne.split()
            ["la", "nsi", "c'est", "la", "vie"]
            >>> ligne.split()[0]
            "la"
            >>> ligne.split()[-1]
            "vie"
            ```
        
        Compléter la partie *Création des données*.

    === "Question 6: l'analyse des données"
        Maintenant que l'arborescence est construite, on peut donc enfin déterminer les répertoires dont la taille est inférieure à une taille donnée (ici 100000).

        On va donc écrire une fonction `cherche_petit_repertoire` qui prend en paramètre un objet de classe `Repertoire` et un entier `n` et qui va chercher dans le répertoire donné en paramètre les répertoires dont la taille est inférieure (ou égale) à `n`. Cette fonction **ne renvoie rien**, elle ajoute à la variable (globale) `petits_repertoires` de type `#!py list` les tailles inférieures à `n`trouvées:

        - si la taille du répertoire est inférieure à `n`, on l'ajoute;
        - on recommence avec les enfants du répertoire.

        Compléter la partie *Parcours/analyse des données*.

        **Indice:** après avoir lancé votre programme, la variable `petits_repertoires` doit avoir une longueur de 26. Le plus petit élément est 23754 et le plus grand est 95112.

!!! question "Question 7"
    La classe `Repertoire` représente une structure d'arbre, adaptée pour l'exercice. À quel type de parcours correspond la fonction `cherche_petit_repertoire`?

??? question "Bonus"
    L'espace total du disque est de 70000000. Pour installer la mise à jour, vous avez besoin d'un espace libre de 30000000.

    Trouvez le nom du plus petit répertoire (en terme de taille) à supprimer pour pouvoir installer la mise à jour du système.

        

!!! code "Code à compléter"
    ```python linenums='1'
    
    # Dans ce code à compléter, les ... sont donnés à titre indicatif.
    # Si vous avez besoin de plus de lignes de code, ajoutez-en, ce ne sera pas pénalisé.
       
    
    #=======================#
    # Création de la classe #
    #=======================#

    class Repertoire:
        def __init__(self, , ):
            self.name = ...
            self.parent = ...
            self.enfants = ...
            self.fichiers = ...

        def ajoute_fichier(self, f:int):
            ...

        def ajoute_enfant(self, rep:Repertoire):
            ...

        def selection_enfant(self, nom:str) -> Repertoire:
            ...

        def taille(self) -> int:
            s = sum(...)
            for enfant in ... :
                s += ...
            return s


    #=======================#
    # Création des données  #
    #=======================#

    donnees = open("sortie_terminal.txt").read().splitlines()
    donnees.pop(0)
    racine = ...
    rep_courant = ...

    for ligne in donnees:
        if ligne == '$ cd ..':
            rep_courant = ...
        elif ligne[:5] == '$ cd ':
            nom_repertoire = ...
            rep_courant = ...
        elif ligne == '$ ls':
            pass
        elif ligne[:3] == 'dir':
            ...
        else:
            ...


    #==============================#
    # Parcours/analyse des données #
    #==============================#
    
    petits_repertoires = []
    def cherche_petit_repertoire(rep: Repertoire, n:int):
        ...
        ...
        ...
        ...
        ...

    cherche_petit_repertoire(..., ...)
    print(petits_repertoires)
    ```


