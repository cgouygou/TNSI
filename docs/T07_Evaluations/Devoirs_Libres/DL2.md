# DL 0010 (sujet 25AN1J1 - exercice 2 modifié)

Une entreprise souhaite gérer les colis qu’elle expédie à l’aide d’une application
informatique. On sait que chaque colis a un identifiant unique, un poids, une adresse
de livraison et un état. Pour chacun d’entre eux, trois états sont possibles : «préparé»,
«transit» ou «livré».

Pour cela, on a créé une classe `#!py Colis`  avec les attributs suivants:

- `id` : un identifiant unique (de type `#!py str` ) ;
- `poids` : le poids du colis en kilogrammes (de type `#!py float`) ;
- `adresse` : l’adresse de destination (de type `#!py str`) ;
- `etat` : l’état du colis (de type `#!py str` parmi `'préparé'`, `'transit'`, `'livré'`).


Lorsque l’on crée une instance de la classe `Colis`, l’attribut `etat` est initialisé à
`'préparé'` tandis que les valeurs des autres attributs sont passées en paramètres.

Voici le début du code Python de la classe `Colis`:

```python linenums='1'
class Colis:
    def __init__(self, id, poids, adresse):
        self.id = id
        self.poids = poids
        self.adresse = adresse
        self.etat = 'préparé'
```

On crée, par exemple, les deux colis suivants :

```python
colisA = Colis('AC12', 5.0, '20 rue de la paix 57000 Metz')
colisB = Colis('AF34', 10.25, '32 rue du centre 57000 Metz')
```

!!! question "Question 1"
    Écrire la méthode `passer_transit` de la classe `Colis` qui permet de mettre l’état du colis à la valeur `'transit'`. 

??? check "Réponse"
    ```python 
    def passer_transit(self):
        self.etat = 'transit'
    ```


On dispose de la fonction `ajouter_colis` suivante :
```python
def ajouter_colis(liste, colis):
    '''
    ajoute le colis à la fin de la liste
    '''
    liste.append(colis)
```

Par exemple, après l’exécution des trois instructions suivantes, on a ajouté les deux
colis créés précédemment à la liste `liste_colis` :
```python linenums='1'
liste_colis = []
ajouter_colis(liste_colis, colisA)
ajouter_colis(liste_colis, colisB)
```

!!! question "Question 2"
    Dans cette question uniquement, on considère que l’acheminement des colis de plus de 25 kg est refusé par le transporteur.
    Recopier et modifier le code de la fonction `ajouter_colis` afin qu’elle ajoute
    le colis à la liste si son poids est inférieur ou égal à 25 kg et qu’elle affiche le
    message `«Dépassement du poids maximal autorisé»` sinon.

??? check "Réponse"
    ```python
    def ajouter_colis(liste, colis):
        '''
        ajoute le colis à la fin de la liste si son poids est inférieur à 25kg
        '''
        if colis.poids <= 25:
            liste.append(colis)
        else:
            print("Dépassement du poids maximal autorisé")
    ```

!!! question "Question 3"
    Écrire une fonction `nb_colis` qui prend en paramètre une liste d’objets de la classe `Colis` et qui renvoie le nombre de colis présents dans cette liste.

??? check "Réponse"
    ```python
    def nb_colis(liste_colis):
        return len(liste_colis)
    ```
    

!!! question "Question 4"
    Recopier et compléter les lignes 2 et 4 du code ci-après de la fonction `poids_total` qui prend en paramètre une liste d’objets de la classe `Colis` et qui renvoie le poids total de l’ensemble des colis de cette liste.

    ```python linenums='1'
    def poids_total(liste):
        total = ...
        for c in liste :
            total = ...
        return total
    
    ```

??? check "Réponse"
    ```python linenums='1'
    def poids_total(liste):
        total = 0
        for c in liste :
            total = total + c.poids
        return total

    ```

!!! question "Question 5"
    Écrire une fonction `liste_colis_etat` qui prend en paramètres une liste d’objets de la classe `Colis` et une chaîne de caractères `statut` (parmi
    `'préparé'`, `'transit'` ou `'livré'`) et qui renvoie une nouvelle liste contenant l’ensemble des colis de cette liste dont l’état est le même que `statut`.

??? check "Réponse"
    ```python linenums='1'
    def liste_colis_etat(liste_colis, statut):
        liste = []
        for colis in liste_colis:
            if colis.etat == statut:
                liste.append(colis)
        return liste    
    ```
    
    Ou, bien mieux, en créant directement la liste par compréhension:

    ```python linenums='1'
    def liste_colis_etat(liste_colis, statut):
        return [colis for colis in liste_colis if colis.etat == statut]
    ```
    


L’entreprise tente d’optimiser, à l’aide d’un algorithme glouton, le chargement des colis
dans un camion ayant une capacité exprimée en kilogrammes, sans tenir compte de
la contrainte de volume. La procédure gloutonne adoptée est la suivante : on charge
les colis dans le camion en les choisissant par ordre décroissant de leur poids, sans
dépasser la capacité du camion.

Pour cela, il est nécessaire de travailler sur une liste de colis triés par ordre de poids
décroissants. La fonction `tri_decroissant` permet de réaliser ce tri.

```python linenums='1'
def tri_decroissant(liste):
    n = len(liste)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if liste[j].poids > liste[min_pos].poids:
                min_pos = j
        # Échanger les éléments
        temp = liste[i]
        liste[i] = liste[min_pos]
        liste[min_pos] = temp
    return liste
```

!!! question "Question 6"
    Donner le nom du tri utilisé dans la fonction `tri_decroissant` ainsi que son coût dans le pire des cas.  

??? check "Réponse"
    Il s'agit d'un [tri par sélection](https://cgouygou.github.io/1NSI/T07_Algorithmes/T7.2_Tri_selection/T7.2_Tri_selection/){:target="_blank"} dont le coût est en $O(n^2)$, c'est-à-dire proportionnel au carré de la longueur de la liste à trier.


Le code Python ci-après présente la fonction récursive `chargement_glouton` dont
les paramètres sont :

- `liste` : une liste de colis triées par poids décroissants ;
- `rang` : un indice compris entre `0` inclus et `len(liste)` inclus ;
- `capacite` : une charge exprimée en kilogrammes ;

et qui renvoie la liste des colis à charger en appliquant l’algorithme glouton, en
supposant que la charge restante dans le camion est `capacite`, et en ne considérant
que les colis de `liste` d’indice supérieur ou égal à `rang`.

```python linenums='1'
def chargement_glouton(liste, rang, capacite):
    if rang == len(liste):
        return ...
    elif liste[rang].poids <= ...:
        return ... + chargement_glouton(liste, ..., ...)
    else:
        return chargement_glouton(liste, ..., ...)
```

!!! question "Question 7"
    Recopier et compléter le code ci-dessus de la fonction `chargement_glouton`.

??? check "Réponse"
    ```python linenums='1'
    def chargement_glouton(liste, rang, capacite):
        if rang == len(liste):
            return []
        elif liste[rang].poids <= capacite:
            return [liste[rang]]] + chargement_glouton(liste, rang+1, capacite - liste[rang].poids)
        else:
            return chargement_glouton(liste, rang+1, capacite)
    ```


!!! question "Question 8"
    Expliquer brièvement pourquoi, lors d’un appel à la fonction `chargement_glouton`, on peut obtenir l’erreur suivante.

    ```python
    RecursionError: maximum recursion depth exceeded while
    calling a Python object.
    ```

??? check "Réponse"
    On peut éventuellement dépasser le nombre d’appels récursifs autorisés.


!!! question "Question 9"
    Écrire une fonction `chargement_glouton2` **itérative** (sans récursivité) qui prend en paramètres `liste` une liste de colis triés par poids décroissants et
    `capacite` la capacité du camion exprimée en kilogrammes, et qui renvoie la liste des colis à charger pour maximiser le poids total sans dépasser la capacité.
    
    On pourra créer une liste `colis_a_charger`, puis parcourir les colis triés en les ajoutant à cette liste tant que le poids total n’excède pas la capacité du camion.

??? check "Réponse"
    ```python linenums='1'
    def chargement_glouton2(liste, capacite):
        colis_a_charger = []
        for colis in liste :
            if colis.poids <= capacite :
                colis_a_charger.append(colis)
                capacite -= colis.poids
        return colis_a_charger
    ```
    
