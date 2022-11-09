# DS 0010 - 20/10/2022 - Corrigé

<!-- **Partie 2 sur machine :** [https://capytale2.ac-paris.fr/web/c/f6cd-848206](https://capytale2.ac-paris.fr/web/c/f6cd-848206){:target="_blank"} -->

## Partie I

### Exercice 1 (tableaux/listes)

1. Écrire une fonction `tranche` qui prend en paramètre une liste `lst` et renvoie la liste privée de son premier élément (c'est-à-dire d'indice 0) et de son dernier (c'est-à-dire d'indice `len(lst)-1`).

    !!! check "Proposition de correction"
        ```python
        # Construction en extension
        def tranche(lst:list) -> list:
            nouvelle_liste = []
            for k in range(1, len(lst)-1):
                nouvelle_liste.append(lst[k])
            return nouvelle_liste

        # Construction en compréhension
        def tranche(lst:list) -> list:
            return [lst[k] for k in range(1, len(lst)-1)]
        ```

2. Proposer un jeu de tests (c'est-à-dire des exemples d'appels pour tester la fonction, avec le résultat attendu pour chaque appel).

    !!! check "Proposition de correction"
        ```python
        >>> tranche([3, 5, 7, 12, 23])
        [5, 7, 12]
        >>> tranche([3, 5])
        []
        >>> tranche([3])
        []
        >>> tranche([])
        []
        ```
### Exercice 2 (Programmation Orientée Objet)

Un coffre fort contient un montant d'argent. Ce montant est nul si le coffre est vide. Le coffre peut être ouvert ou fermé. Pour ouvrir le coffre, on doit saisir un code (entier à 4 chiffres), mais ce code n'est pas nécessaire pour le fermer. Si le coffre est ouvert, on peut le consulter, y déposer de l’argent ou en retirer. Si le coffre est fermé, ces opérations sont impossibles. On ne peut pas retirer plus que ce que contient le coffre.

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

## Partie II (machine)

### Exercice 1 (récursivité)

Un palindrome est un mot qui peut être lu dans les deux sens de la même façon. Par exemple, «kayak», «radar», «gag» ou «ABBA» sont des palindromes, mais pas «toto».

Écrire une fonction *récursive* `est_palindrome` qui prend en paramètre une **chaîne de caractère** et renvoie un **booléen** qui détermine si la chaîne est un palindrome ou non.

**Exemples:**

```python 
>>> est_palindrome("toto")
False
>>> est_palindrome("kayak")
True
>>> est_palindrome("")
True
>>> est_palindrome("abcdeedcba")
True
```

**Rappel:**
- on peut récupérer les élements d'une chaîne de caractères (type `str`) comme un tableau, par leur indice. Par exemple, si `mot` est de type `str`, `mot[0]` renvoie le premier caractère et `mot[-1]` le dernier.
- pour obtenir une chaîne de caractères privée de son premier **et** de son dernier caractère, on peut utiliser `mot[1:-1]`.

**Indication:** réfléchir à quelle condition sur la première et la dernière lettres un mot est un palindrome...

!!! check "Proposition de correction"
    ```python linenums='1'
    def est_palindrome(mot:str) -> bool:
    if len(mot) == 0:
        return True
    elif mot[0] != mot[-1]:
        return False
    else:
        return est_palindrome(mot[1:-1])

    ```


### Exercice 2 (POO)

Un coffre fort contient un montant d'argent. Ce montant est nul si le coffre est vide. Le coffre peut être ouvert ou fermé. Pour ouvrir le coffre, on doit saisir un code (entier à 4 chiffres), mais ce code n'est pas nécessaire pour le fermer. Si le coffre est ouvert, on peut le consulter, y déposer de l’argent ou en retirer. Si le coffre est fermé, ces opérations sont impossibles. On ne peut pas retirer plus que ce que contient le coffre.

1. Compléter le code suivant pour implémenter la classe `Coffre`.

    **Remarque:** enlever les `pass` au fur et à mesure pour tester le code.

    
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
            self.montant = 0


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
                return f"Le coffre contient un montant de {self.montant}."
            else:
                return "Le coffre est fermé."

        def deposer(self, montant)  -> str:
            """
            Ajoute le montant au contenu si le coffre est ouvert.
            Renvoie une chaîne de caractères précisant le montant déposé (0 si fermé).
            """
            if self.ouvert:
                self.montant += montant
                return f"montant déposé: {montant} "
            else:
                return "montant déposé: 0"

        def retirer(self, montant)  -> str:
            """
            Retire le montant du coffre s'il est ouvert.
            Renvoie une chaîne de caractères précisant le montant retiré (0 si fermé).
            """
            if self.ouvert:
                if montant <= self.montant:
                    self.montant -= montant
                    return f"montant retiré: {montant} "
                else:
                    return "il n'y a pas assez d'argent dans le coffre"
            else:
                return "montant retiré: 0"
        ```
        

2. Voir **2.** de l'exercice 2 - Partie I.