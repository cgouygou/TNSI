# DL 0010 : Travail sur les tableaux/listes (rappels)

{{ initexo(0) }}

À faire pour le mardi 10 octobre sur Capytale : [https://capytale2.ac-paris.fr/web/c/1dc7-1939026](https://capytale2.ac-paris.fr/web/c/1dc7-1939026){:target="_blank"} 

!!! check "Proposition de correction"
    !!! example "{{ exercice() }}"
        === "Énoncé" 
            Écrire une fonction `maximum` qui prend en paramètre un tableau (type `list`) d'entiers et qui renvoie le plus grand élément du tableau). Si le tableau est vide, la fonction doit renvoyer `None`.

            ```python title='Exemples'
            >>> maximum([2, 1, 8, 0, 42, 8, 12])
            42
            >>> maximum([4, 4, 4])
            4
            >>> maximum([])
            None        
            ```

        === "Correction" 
            {{ correction(True, 
            "
            On peut parcourir le tableau sur ses éléments: 

            ```python linenums='1'
            def maximum(tab:list) -> int:
                '''
                Renvoie le plus grand élément de la liste tab.
                '''
                if tab == []:
                    return None
                maxi = tab[0]
                for elt in tab:   # parcours de liste sur les éléments
                    if elt > maxi:
                        maxi = elt
                return maxi
            ```
            Ou bien sur les indices:
            ```python linenums='1'
            def maximum(tab:list) -> int:
                '''
                Renvoie le plus grand élément de la liste tab.
                '''
                if tab == []:
                    return None
                maxi = tab[0]
                for i in range(len(tab)):   # parcours de liste sur les indices
                    if tab[i] > maxi:
                        maxi = tab[i]
                return maxi
            ```
            Et on n'oublie pas de tester:
            ```python linenums='1'
            assert maximum([2, 1, 8, 0, 42, 8, 12]) == 42
            assert maximum([4, 4, 4]) = 4
            assert maximum([]) == None
            ```
            
            "
            ) }}

    !!! example "{{ exercice() }}"
        === "Énoncé" 
            Écrire une fonction `indice` qui prend en paramètre un tableau (type `list`) d'entiers et un entier, et qui renvoie l'indice de la première occurence de l'entier dans le tableau. Si l'entier n'appartient pas à la liste, la fonction doit renvoyer `None`.

            ```python title='Exemples'
            >>> indice([2, 1, 8, 0, 42, 8, 12], 42)
            4
            >>> indice([2, 1, 8, 0, 42, 8, 12], 8)
            2
            >>> indice([2, 1, 8, 0, 42, 8, 12], 5)
            None        
            ```
        === "Correction" 
            {{ correction(True, 
            "
            ```python linenums='1'
            def indice(tab:list, n:int) -> int:
                for i in range(len(tab)):
                    if tab[i] == n:
                        return i
                return None

            assert indice([2, 1, 8, 0, 42, 8, 12], 42) == 4
            assert indice([2, 1, 8, 0, 42, 8, 12], 8) == 2
            assert indice([2, 1, 8, 0, 42, 8, 12], 5) == None
            ```
            "
            ) }}

    !!! example "{{ exercice() }}"
        === "Énoncé" 
            Écrire une fonction ``tranche`` qui prend en paramètres une liste `tab` et deux entiers ``start`` et ``stop`` et qui renvoie la liste équivalente à `tab[start:stop]`.

            **Aide:** à partir d'une liste vide, on ajoutera les éléments de `tab` correspondants aux indices compris entre ``start`` et ``stop``.
        === "Correction" 
            {{ correction(True, 
            "
            ```python linenums='1'
            def tranche(tab:list, start:int, stop:int) -> list:
                '''	
                Renvoie les éléments de tab dont les indices sont compris entre start (inclus)
                et stop (exclus).
                '''
                t = []
                for i in range(start, stop):
                    t.append(tab[i])
                return t

            assert tranche([2, 1, 8, 0, 42, 8, 12], 1, 4) == [1, 8, 0]
            assert tranche([2, 1, 8, 0, 42, 8, 12], 0, 1) == [2]
            assert tranche([2, 1, 8, 0, 42, 8, 12], 3, 7) == [0, 42, 8, 12]
            assert tranche([2, 1, 8, 0, 42, 8, 12], 2, 2) == []
            ```
            Ou mieux, en compréhension:

            ```python linenums='1'
            def tranche(tab:list, start:int, stop:int) -> list:
                '''	
                Renvoie les éléments de tab dont les indices sont compris entre start (inclus)
                et stop (exclus).
                '''
                return [tab[i] for i in range(start, stop)]
            ```
            "
            ) }}

