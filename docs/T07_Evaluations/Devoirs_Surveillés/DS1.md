# Correction du DS0001

## Exercice 1 (flottants)

1. En virgule fixe, l'erreur d'approximation est la même pour tous les nombres, de l'ordre de $2^{-n}$ où $n$ est le nombre de chiffres conservés après la virgule. Cette erreur, infime pour les très grands nombres, devient très importante pour les petits nombres.

2. En virgule flottante, l'erreur **relative** est la même pour tous les nombres.

3. Par exemple `0.1`.

## Exercice 2 (algorithmique)

1. La méthode par force brute consiste à envisager **tous les cas possibles**. L'avantage est qu'elle permet à coup sûr de trouver la **solution optimale** globale au problème. L'inconvénient est qu'**elle peut prendre trop de temps** si les données sont trop grandes.

2. La méthode gloutonne consiste à faire **le meilleur choix local à chaque étape** en espérant obtenir le meilleur choix global. L'avantage est que la solution s'obtient **assez rapidement**. L'inconvénient est qu'**on n'est pas assuré d'obtenir la solution optimale** au problème.


## Exercice 3 (programmation générale)

1.

```python linenums='1'
def somme(tab:list) -> int:
    assert tab != [], "Erreur d'argument: liste vide"
    s = 0
    for i in range(len(tab)):
        s += tab[i]
    return s

assert somme([2, 5, 10]) == 17
assert somme([1]) == 1
```

2. 

```python linenums='1'
def maximum(tab:list) -> int:
    assert tab != [], "Erreur d'argument: liste vide"
    elt_max = tab[0]
    for element in tab:
        if element > elt_max:
            elt_max = element
    return elt_max

assert maximum([2, -1 , 8, 1]) == 8
assert maximum([0, 0, 0]) == 0
```

## Exercice 4 (POO)

1. Décrire la classe `Coffre` en précisant ses attributs et ses méthodes. Préciser les types des attributs, des éventuels paramètres des méthodes et des valeurs éventuellement renvooyées par ces méthodes.

    !!! check "Proposition de correction"
        **Classe**: Coffre

        **Attributs:**
        
        - code: `int`
        - ouvert: `bool`
        - montant: `int`

        **Méthodes:**

        - ouvrir(`int`) -> `None`
        - fermer()  -> `None`
        - consulter()  -> `str`
        - deposer(`int`) -> `str`
        - retirer(`int`) -> `str`

2. Écrire un scénario utilisant cette classe pour tester les différentes méthodes.

    !!! check "Proposition de correction"
        ```python
        >>> c = Coffre(1234)
        >>> c.consulter()
        'Le coffre est fermé.'
        >>> c.ouvrir(1238)
        Mauvais code
        >>> c.ouvrir(1234)
        Coffre ouvert
        >>> c.consulter()
        'Le coffre contient un montant de 0.'
        >>> c.deposer(100)
        'montant déposé: 100 '
        >>> c.consulter()
        'Le coffre contient un montant de 100.'
        >>> c.retirer(20)
        'montant retiré: 20 '
        >>> c.retirer(200)
        "il n'y a pas assez d'argent dans le coffre"
        >>> c.fermer()
        >>> c.deposer(50)
        'montant déposé: 0'
        >>> c.retirer(30)
        'montant retiré: 0'
        ```

## Partie machine

Un coffre fort contient un montant d'argent. Ce montant est nul si le coffre est vide. Le coffre peut être ouvert ou fermé. Pour ouvrir le coffre, on doit saisir un code (entier à 4 chiffres), mais ce code n'est pas nécessaire pour le fermer. Si le coffre est ouvert, on peut le consulter, y déposer de l’argent ou en retirer. Si le coffre est fermé, ces opérations sont impossibles. On ne peut pas retirer plus que ce que contient le coffre.

!!! check "Proposition de correction"
    ```python linenums='1'
    class Coffre :
    """ Une classe pour les coffres-forts 
        attributs : 
            ouvert  : bool 
            code : int
            contenu : float
    """ 

    def __init__(self, c) :
        """
        Coffre(code) , crée un coffre fermé et vide, et c comme code d'ouverture
        """
        self.code = c
        self.ouvert = False
        self.contenu = 0


    def ouvrir(self, c) -> None:
        """
        met le coffre en etat ouvert, en vérifiant le code c donné.
        """
        if c == self.code:
            self.ouvert = True
            print("Coffre ouvert")
        else:
            print("Mauvais code")


    def fermer(self) -> None:
        """ met le coffre en etat fermé """
        self.ouvert = False


    def consulter(self) -> str:
        """ donne le contenu du coffre s'il est ouvert, 'coffre fermé' sinon"""
        if self.ouvert:
            return f"Le coffre contient un montant de {self.contenu}."
        else:
            return "Le coffre est fermé."

    def deposer(self, montant)  -> str:
        """
        Ajoute le montant au contenu si le coffre est ouvert.
        Renvoie une chaîne de caractères précisant le montant déposé (0 si fermé).
        """
        if self.ouvert:
            self.contenu += montant
            return f"montant déposé: {montant} "
        else:
            return "montant déposé: 0"

    def retirer(self, montant)  -> str:
        """
        Retire le montant du coffre s'il est ouvert.
        Renvoie une chaîne de caractères précisant le montant retiré (0 si fermé).
        """
        if self.ouvert:
            if montant <= self.contenu:
                self.contenu -= montant
                return f"montant retiré: {montant} "
            else:
                return "il n'y a pas assez d'argent dans le coffre"
        else:
            return "montant retiré: 0"
    ```