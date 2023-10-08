# DS 0001

## Exercice 1 (flottants)

1. $0,101_2 = 2^{-1} + 2^{-3} = 0,5 + 0, 125 = 0,625$
2. Pour la partie entière : $5 = 101_2$
    Pour la partie décimale:

    $$\begin{array}{rl}
    0,28125 \times 2 &= 0,5625\\
    0,5625 \times 2 &= 1,125\\
    0,125 \times 2&= 0,25\\
    0,25 \times 2&= 0,5\\
    0,5 \times 2 &= 1,0
    \end{array}
    $$

    Donc $0,28125=0,01001_2$ et finalement $5,28125=101,01001_2$.


## Exercice 2 (cours)

1. La méthode par force brute consiste à envisager tous les cas possibles. L'avantage est qu'elle permet à coup sûr de trouver la solution optimale globale au problème. L'inconvénient est qu'elle peut prendre trop de temps si les données sont trop grandes.

2. La méthode gloutonne consiste à faire le meilleur choix local à chaque étape en espérant obtenir le meilleur choix global. L'avantage est que la solution s'obtient assez rapidement. L'inconvénient est qu'on n'est pas assuré d'obtenir la solution optimale au problème.

3. Une fonction récursive est une fonction qui s'appelle elle-même dans sa définition. Elle doit comporter un cas d'arrêt et un appel (récursif) à elle-même avec des paramètres différents qui assurent à terme l'obtention du cas d'arrêt.

## Exercice 3 (récursivité)

1. On obtient le code suivant:

    ```python linenums='1'
    def puissance(x:float, n:int) -> float:
        if n == 0:
            return 1
        else:
            if n%2 == 0:
                return puissance(x*x, n//2)
            else:
                return x * puissance(x*x, (n-1)//2)
    ```
    
2. Le calcul de $x^{13}$ va nécessiter le calcul de $x^6$, puis $x^3$, puis $x^1$ et enfin $x^0$, soit 4 appels récursifs et 5 appels de fonction. C'est beaucoup mieux que la fonction vue en classe qui demande 12 appels récursifs (et 13 appels en tout).


## Exercice 4 (récursivité, partie machine)

On doit envisager le cas d'arrêt où le premier élement de `#!py tab` est la valeur recherchée avec un renvoi de la valeur `#!py True`). Mais pour pouvoir accéder au premier élément, il faut que `#!py tab` soit non vide! Et c'est d'ailleurs lorsque `#!py tab` est vide qu'on sait qu'on a pas trouvé la valeur recherchée, c'est aussi un cas d'arrêt (avec un renvoi de la valeur `#!py False`).

On obtient par exemlpe:

```python linenums='1'
def recherche(tab:list, m:int) -> bool:
    '''
    Renvoie un booléen déterminant si la valeur m est trouvée dans la liste tab ou non.
    '''
    if tab == []:
        return False
    elif tab[0] == m:
        return True
    else:
        return recherche(tab[1:], m)
```
