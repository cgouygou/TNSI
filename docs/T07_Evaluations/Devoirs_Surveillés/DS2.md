# DS0010 - Corrigé

## Exercice 1

1. Une fonction récursive est une fonction qui s'appelle elle-même dans sa définition. Elle comporte :

    - un (ou plusieurs) cas d'arrêt;
    - un appel récursif avec un paramètre croissant ou déroissant qui amènera au cas d'arrêt.

2. Un algorithme glouton effectue à chaque étape le meilleur choix local, en espérant que la soluton (rapide à obtenir) soit assez proche de la meileure solution globale.

## Exercice 2

```python linenums='1'
def somme(n:int) -> int:
    if n == 0:
        return 0
    return n + somme(n-1)
```

## Exercice 3

1. Premier passage: 4-9-8-7-4-2 (du haut vers le bas) puis 4-8-7-4-2 puis 4-8-4-2

    Deuxième passage: 4-4-2

    Troisième passage: 4-2 (la pile est gagnante)

2. La pile gagnante est la pile B.


3. 
    
    ```python linenums='1'
    def sommet(p:Pile) -> int:
        '''
        Fonction qui renvoie l'élément au sommet de la pile p
        sans le retirer.
        '''
        if not p.est_vide():
            s = p.depiler()
            p.empiler(s)
            return s
    ```

4. 
    
    ```python linenums='1'
    def taille(p):
        c = 0
        q = Pile()
        while not p.est_vide():
            c += 1
            elt = p.depiler()
            q.empiler(elt)
        while not q.est_vide():
            elt = q.depiler()
            p.empiler(elt)
        return c
    ```

5. 
    
    ```python linenums='1'
    def reduire_triplet_au_sommet(p):
        a = p.depiler()
        b = p.depiler()
        c = sommet(p)
        if a % 2 != c % 2 : #le premier (a) et le troisième (c) ne sont pas de même parité
            p.empiler(b) # on ne supprime pas b donc on l'empile
        p.empiler(a) # dans tous les cas on empile a
    ```

6.  

    **a.** Il faut au minimum 3 éléments pour pouvoir simplifier et qu'il n'en reste que deux.

    **b.** 
    ```python linenums='1'
    def parcourir_pile_en_reduisant(p):
        q = Pile()
        while taille(p) >= 3:
            reduire_triplet_au_sommet(p)
            elt = p.depiler()
            q.empiler(elt)
        while not est_vide(q):
            elt = q.depiler()
            p.empiler(elt)
    ```

    **c.**

    ```python linenums='1'
    def jouer(p):
        t1 = taille(p)
        parcourir_pile_en_reduisant(p)
        t2 = taille(p)
        if t1 == t2 : # si après réduction la taille est la même, c'est terminé
            return p  # on renvoie la pile
        else:
            return jouer(p) # sinon on recommence avec p qui a été réduite
    ```

## Exercice 4

1. 
    ```python linenums='1'
    class Carte:
        def __init__(self, v):
            self.valeur = v
            self.TdB = self.calcul_Tdb()
    ```

2. 

    ```python linenums='1'
    def calcul_TdB(self):
        tetes = 0
        if self.valeur % 11 == 0:
            tetes += 5
        if self.valeur % 10 == 0: # la valeur se termine par un 0
            tetes += 3
        if self.valeur % 10 == 5: # la valeur se termine par un 5
            tetes += 2
        if tetes == 0:
            tetes = 1
        return tetes
    ```

3. 

    ```python linenums='1'
    class Main:
        def __init__(self, liste_cartes):
            self.contenu = liste_cartes

        def afficher(self):
            for carte in self.contenu:
                print(carte.valeur)

        def ajouter_carte(self, carte):
            self.contenu.append(carte)
    ```

4. 

    ```python linenums='1'
        def nombre_TdB(self):
            total = 0
            for carte in self.contenu:
                total += carte.TdB
            return total
    ```

5. 

    ```python linenums='1'
    class Jeu:
        def __init__(self, n):
            self.nbr = n
            self.paquet = [Carte(k) for k in range(1, 105)]
            self.mains = []
    ```

6. Il faut écrire `#!py from random import shuffle` 

7. 

    ```python linenums='1'
    def distribuer(self):
        self.melanger()
        self.mains = [Main([]) for _ in range(self.nbr)]
        for i in range(10):
            for joueur in range(self.nbr):
                carte = self.paquet.pop()
                self.mains[joueur].ajouter_carte(carte)
    ```

8. 

    ```python linenums='1'
    manche_1 = Jeu(4) # pour 4 joueurs par exemple
    manche_1.distribuer()
    indice_main_max = 0
    main_max = 0
    for i in range(len(manche_1.mains)):
        if manche_1.mains[i].nombre_TdB() >= main_max:
            main_max = manche_1.mains[i].nombre_TdB()
            indice_main_max = i
    
    print(f"La main d'indice {i} est celle contenant le plus de têtes de bœuf")
    ```
    