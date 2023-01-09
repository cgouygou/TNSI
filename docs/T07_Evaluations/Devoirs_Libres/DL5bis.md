# DL 0101 (bis) : carrés magiques

!!! capytale "Lien vers l'activité Capytale"
    Devoir à faire et à rendre ici : [https://capytale2.ac-paris.fr/web/c/ec89-1139771](https://capytale2.ac-paris.fr/web/c/ec89-1139771){:target="_blank"} 


Dans cet exercice, on appelle carré d’ordre $n$ un tableau de $n$ lignes et $n$ colonnes dont chaque case contient un entier naturel.

**Exemples :**
![image](../images/img20_2.png){: .center width=70%}

Un carré est dit *magique* lorsque les sommes des éléments situés sur chaque ligne, chaque
colonne et chaque diagonale sont égales. Ainsi c2 et c3 sont magiques car la somme de chaque
ligne, chaque colonne et chaque diagonale est égale à 2 pour c2 et 15 pour c3. 

Le carré c4 n’est en revanche pas magique car la somme de la première ligne est égale à 34 alors que celle de la dernière colonne
est égale à 27.

1. La classe `Carre` ci-après contient des méthodes qui permettent de manipuler des carrés.
    Compléter les fonctions `somme_ligne` et `somme_colonne`.


    ```python linenums='1'
    class Carre:
        def __init__(self, tableau = [[]]):
            self.ordre = len(tableau)
            self.valeurs = tableau

        def affiche(self):
            '''Affiche un carré'''
            for i in range(self.ordre):
                print(self.valeurs[i])

        def somme_ligne(self, i):
            '''Calcule la somme des valeurs de la ligne i'''
            return sum(...)

        def somme_colonne(self, j):
            '''Calcule la somme des valeurs de la colonne j'''
            return sum([self.valeurs[...][...] for ... in range(self.ordre)])
    ```

2. Compléter la fonction `est_magique` qui prend en paramètre un carré (une instance de `Carre`) et qui renvoie la valeur de
la somme si ce carré est magique, `False` sinon.

    ```python linenums='1'
    def est_magique(carre):
        n = carre.ordre
        s = carre.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(..., ...):
            if carre.somme_ligne(i) != s:
                return ...

        #test de la somme de chaque colonne
        for j in range(n):
            if ... != s:
                return False

        #test de la somme de chaque diagonale
        if sum([carre.valeurs[...][...] for k in range(n)]) != s:
            return False
        if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
        return ...
    ```
3. Tester la fonction `est_magique` sur les carrés c2, c3 et c4. 


!!! check "Correction"
    ```python linenums='1'
    class Carre:
        def __init__(self, tableau = [[]]):
            self.ordre = len(tableau)
            self.valeurs = tableau

        def affiche(self):
            '''Affiche un carré'''
            for i in range(self.ordre):
                print(self.valeurs[i])

        def somme_ligne(self, i):
            '''Calcule la somme des valeurs de la ligne i'''
            return sum(self.valeurs[i])

        def somme_col(self, j):
            '''Calcule la somme des valeurs de la colonne j'''
            return sum([self.valeurs[i][j] for i in range(self.ordre)])

    def est_magique(carre):
        n = carre.ordre
        s = carre.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(1, n):
            if carre.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(n):
            if carre.somme_col(j) != s:
                return False

        #test de la somme de chaque diagonale
        if sum([carre.valeurs[k][k] for k in range(n)]) != s:
            return False
        if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False
        return s

    c1 = Carre([[1, 1],
                [1, 1]])

    c2 = Carre([[2, 9, 4],
                [7, 5, 3],
                [6, 1, 8]])

    c3 = Carre([[4, 5, 16, 9],
                [14, 7, 2, 11],
                [3, 10, 15, 6],
                [13, 12, 8, 1]])

    assert est_magique(c1) == 2
    assert est_magique(c2) == 15
    assert est_magique(c3) == False

    ```
    