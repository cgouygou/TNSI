# DL 0010 : Travail sur les tableaux/listes (rappels)

{{ initexo(0) }}


!!! example "{{ exercice() }}"
    === "Énoncé" 
        À rendre sur [Capytale](https://capytale2.ac-paris.fr/web/c/654c-726825/mlc){:target="_blank"}.

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
        ```python
        def maximum(tab:list) -> int:
            if tab == []:
                return None
            maxi = tab[0]
            for elt in tab:
                if elt > maxi:
                    maxi = elt
            return maxi
        ```
        "
        ) }}

!!! example "{{ exercice() }}"
    === "Énoncé" 
        À rendre sur [Capytale](https://capytale2.ac-paris.fr/web/c/01c4-726834/mlc){:target="_blank"} 

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
        ```python
        def indice(tab:list, n:int) -> int:
            for i in range(len(tab)):
                if tab[i] == n:
                    return i
            return None
        ```
        "
        ) }}