# DL 0010 : Travail sur les tableaux/listes (rappels)

{{ initexo(0) }}


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
        {{ correction(False, 
        "
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
        {{ correction(False, 
        "
        "
        ) }}