# Correction du DS0002

{{ initexo(0) }}

!!! example "{{ exercice() }}"
    === "Énoncé" 
        Expliquer ce qu'est une fonction récursive. Donner les deux étapes indispensables.
    === "Correction" 
        {{ correction(True, 
        "
        Une fonction récursive est une fonction qui s'appelle elle-même. Les deux étapes indispensables sont:

        - un cas d'arrêt, pour arrêter la récursivité;
        - un appel récursif dans le cas général, avec modification du paramètre (pour arriver au cas d'arrêt).
        "
        ) }}


!!! example "{{ exercice() }}"
    === "Énoncé" 
        Dans le cours, on a écrit une fonction récursive `#!py puissance(x, n)`   permettant de calculer $x^n$:

        ```python linenums='1'
        def puissance(x:float, n:int) -> float:
            '''
            calcule et renvoie la puissance n-ième de x
            '''
            if n == 0:
                return 1
            else:
                return x * puissance(x, n-1)
        ```

        On veut écrire une nouvelle fonction récursive `#!py puissance(x, n)`  qui calcule le nombre $x^n$ de façon plus efficace que la précédente. 

        Pour cela, on utilise le fait que :

        - quel que soit $x$, $x^0=1$
        - si $n$ est pair, $x^n=(x \times x)^{n/2}$
        - sinon $x^n=x \times (x \times x)^{(n - 1)/2}$

        Compléter le code ci-dessous (uniquement les pointillés):

        ```python linenums='1'
        def puissance(x:float, n:int) -> float:
            if n == 0 :
                return  ...
            else :
                if  ..........    :
                    return puissance(x*x, n//2)
                else :
                    return  ...........................
        ```

        Combien d'appels récursifs sont nécessaires pour calculer $x^{13}$ ? Est-ce mieux que la fonction du cours?


    === "Correction" 
        {{ correction(True, 
        "
        ```python linenums='1'
        def puissance(x:float, n:int) -> float:
            if n == 0 :
                return  1
            else :
                if  n % 2 == 0:
                    return puissance(x*x, n//2)
                else :
                    return  x * puissance(x*x, (n-1) // 2)
        ```
        
        La fonction du cours va faire 13 appels récursifs, puisque le paramètre diminue de 1 à chaque appel.

        En revanche, la nouvelle fonction va en faire seulement 4, pous une valeur de l'exposant de 6, puis 3, puis 1, puis 0. Elle est donc bien plus efficace (en $O(\log n)$ contre $O(n)$ pour celle du cours).
        "
        ) }}

!!! example "{{ exercice() }}"
    === "Énoncé" 
        Écrire une fonction récursive `#!py somme` qui prend en paramètre un entier `#!py n`  et renvoie la somme des entiers de 0 à $n$.
    === "Correction" 
        {{ correction(True, 
        "
        Voir le cours.
        "
        ) }}

!!! example "{{ exercice() }} : Partie Machine 1"
    === "Énoncé" 
        On cherche à écrire une fonction récursive ```recherche(tab, m)``` qui recherche la présence de la valeur ```m``` dans un tableau ```tab``` (de type `list`). Cette fonction doit renvoyer un **booléen**.

        Pour cela, on examine le premier élément de la liste. Soit c'est la valeur cherchée, soit on recommence la recherche dans le tableau privé de son premier élément.

        **Aide:** le *slicing* est **exceptionnellement autorisé**, on utilisera donc `tab[1:]`pour obtenir le tableau privé de son premier élément.

        **Exemples d'utilisation:**

        ```python
        >>> recherche([0, 7, 12, 1, 42, 23, 78], 42)
        True
        >>> recherche([0, 7, 12, 1, 42, 23, 78], 3)
        False
        >>> recherche([], 1)
        False
        ```

        N'oubliez pas de spécifier votre fonction et d'écrire les 3 tests (à l'aide du mot-clé `assert`) correspondant aux exemples donnés.
    === "Correction" 
        {{ correction(True, 
        "
        ```python linenums='1'
        def recherche(tab: list, m: int) -> bool:
            '''
            Renvoie un booléen indiquant la présence de la valeur m dans le tableau tab.
            '''
            if tab == []:
                return False
            elif tab[0] == m:
                return True
            else:
                return recherche(tab[1:], m)
        
        assert recherche([0, 7, 12, 1, 42, 23, 78], 42) == True
        assert recherche([0, 7, 12, 1, 42, 23, 78], 3) == False
        assert not recherche([], 1)
        ```
        
        "
        ) }}

!!! example "{{ exercice() }} : Partie Machine 2"
    === "Énoncé" 
        Un palindrome est un mot qui peut être lu dans les deux sens de la même façon. Par exemple, «kayak», «radar», «gag», «ABBA»  ou encore «ressasser» sont des palindromes, mais pas «toto».

        En particulier, si un mot est un palindrome, alors en enlevant un caractère au début et à la fin du mot (le même), alors on obtient un nouveau palindrome...

        Écrire une fonction *récursive* `est_palindrome` qui prend en paramètre une **chaîne de caractère** et renvoie un **booléen** qui détermine si la chaîne est un palindrome ou non.

        Penser à spécifier et à tester la fonction.

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
        - *slicing* autorisé: pour obtenir une chaîne de caractères privée de son premier **et** de son dernier caractère, on peut utiliser `mot[1:-1]`.



    === "Correction" 
        {{ correction(True, 
        "
        ```python linenums='1'
        def est_palindrome(mot: str) -> bool:
            if mot == '':
                return True
            elif mot[0] != mot[-1]:
                return False
            else:
                return est_palindrome(mot[1:-1])

        assert est_palindrome('toto') == False
        assert est_palindrome('kayak') == True
        assert est_palindrome('') == True 
        assert est_palindrome('abcdeedcba') 
        ```

        "
        ) }}