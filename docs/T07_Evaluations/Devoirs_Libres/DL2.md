# DL 0010: No space left on device

*Thèmes abordés: commandes UNIX, structure d'arbre, POO, récursivité*

Un ami vous confie - en tant qu'expert.e UNIX - un appareil qui dysfonctionne pour le réparer. Vous tentez d'exécuter une mise à jour du système mais vous obtenez le message d'erreur suivant:

```bash
Error: No space left on device
```

Peut-être pouvez-vous supprimer des fichiers pour faire place à la mise à jour ?

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

Puisque le disque est plein, votre première étape devrait probablement être de trouver des répertoires qui sont de bons candidats à la suppression. Pour ce faire, vous devez déterminer la taille totale de chaque répertoire. La taille totale d'un répertoire est la somme des tailles des fichiers qu'il contient, directement ou indirectement. Les répertoires eux-mêmes ne comptent pas comme ayant une taille intrinsèque.

Par exemple, la taille totale du répertoire `e` est 584 puisqu'il ne contient qu'un seul fichier de taille 584.

!!! question "Question 2"
    1. Vérifier que la taille totale du répertoire `a` est 94853.
    2. Donner la taille des répertoires `d` et `\`.

Au travail maintenant. Vous optez pour la stratégie suivante:

1. Choisir un modèle adapté pour représenter les données (vous choisissez de construire une classe `Repertoire`).
2. Parcourir le [fichier de sortie du terminal](../data/sortie_terminal.txt) pour construire les données.
3. Analyser les données pour sélectionner seulement les répertoires dont la taille totale est inférieure à 100000.

!!! question "Questions"
    === "Question 3"
        La classe `Repertoire`


        
!!! code "Code à compléter"
    ```python
    #=======================#
    # Création de la classe #
    #=======================#

    class Repertoire:
        def __init__(self, nom, p):
            self.name = name
            self.parent = p
            self.enfants = []
            self.fichiers = []

        def add_file(self, f):
            self.files.append(f)

        def add_child(self, d):
            self.children.append(d)

        def size(self):
            return sum(self.files) + sum([c.size() for c in self.children])

        def select_child(self, name:str) -> Directory:
            for child in self.children:
                if child.name == name:
                    return child

    #=======================#
    # Création des données  #
    #=======================#

    donnees = open("sortie_terminal.txt").read().splitlines()
    home = Directory('/', None)
    current_dir = home

    for line in data[1:]:
        if line == '$ cd ..':
            current_dir = current_dir.parent
        elif line[:5] == '$ cd ':
            dir_name = line.split()[-1]
            current_dir = current_dir.select_child(dir_name)
        elif line == '$ ls':
            pass
        elif line[:3] == 'dir':
            current_dir.add_child(Directory(line.split()[-1], current_dir))
        else:
            current_dir.add_file(int(line.split()[0]))

    #==============================#
    # Parcours/analyse des données #
    #==============================#
    
    small_sizes = []
    def find_small_sizes(d):
        s = d.size()
        if s <= 100000:
            small_sizes.append(s)
        for child in d.children:
            find_small_sizes(child)

    find_small_sizes(home)
    ```
