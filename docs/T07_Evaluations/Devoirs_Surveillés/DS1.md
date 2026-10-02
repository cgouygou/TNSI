# DS 0001 (Corrigé)

## Exercice 1

1. Un algorithme est appelé glouton lorsqu'il fait le meilleur choix local à chaque étape en espérant obtenir le meilleur choix global.

2. Comme on ne peut pas représenter l'infinité des nombres réels avec un mémoire finie, les nombres flottants sont des valeurs approchées. La comparaison de deux nombres flottants peut donc être fausse.

3. 

    ```python linenums='1'
    def maximum(tab):
        m = tab[0] # tab est non vide, donc on peut prendre l'élément d'indice 0
        for elt in tab:
            if elt > m:
                m = elt
        return m

    ```

## Exercice 2

Il y a 6 erreurs dans ce code:

1. `#!py s == 0 ` est incorrect, il faut écrire `#!py s = 0` pour affecter la valeur `#!py 0` à `#!py s`.
2. il manque `#!py :` en fin de ligne `#!py for element in tab` (`#!py SyntaxError`).
3. il faut tester `#!py element >=0` 
4. `#!py NameError`: il manque un t à `#!py elemen` : `#!py s = s + element` 
5. cette ligne est mal indentée (`#!py IndentationError` 
6. la fonction doit **renvoyer** la somme avec `#!py return s` et non l'afficher avec `#!py print(s)` 

Le code corrigé:

```python linenums='1'
def somme(tab):
    s = 0
    for element in tab:
        if element >= 0:
            s = s + element
    return s
```


## Exercice 3

```python linenums='1'
def est_triee(tab:list) -> bool:
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True

assert est_triee([1, 2, 3, 4]) == True
assert est_triee([2, 1]) == False
```


## Exercice 4

1. Attributs :

    - ouvert (`#!py bool`) : pour déterminer si l'état du coffre, ouvert ou fermé. Vaut `#!py False` par défaut, à l'instanciation.
    - code (`#!py int`) : le code nécessaire à l'ouverture. Déterminé à l'instanciation (paramètre du constructeur `#!py __init__`).
    - montant (`#!py float`): le montant d'argent contenu dans le coffre. Vaut `#!py 0` par défaut, à l'instanciation.

2. Méthodes:

    - `#!py ouvrir(c:int)` : ouvre le coffre si la valeur `#!py c` passée en argument  correspond au code du coffre.
    - `#!py fermer()` : ferme le coffre.
    - `#!py consulter() -> str` : donne le montant du coffre si celui est ouvert.
    - `#!py déposer(m:float)` : ajoute au montant du coffre la valeur `#!py m` passée en argument. 
    - `#!py retirer(m:float)` : enlève au montant du coffre la valeur `#!py m` passée en argument. 