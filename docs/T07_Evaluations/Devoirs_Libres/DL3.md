# DL 0011

À faire pour le mardi 17 octobre sur Capytale : [https://capytale2.ac-paris.fr/web/c/7539-2023341](https://capytale2.ac-paris.fr/web/c/7539-2023341){:target="_blank"} 


## Exercice 1 (rappel sur les listes en compréhension)

1. (Re)Lire le cours de Première [sur les listes en compréhension](https://cgouygou.github.io/1NSI/T02_TypesConstruits/T2.1_Listes/T2.1_Listes3/#2110-listes-en-comprehension).

2. Définir chacune des listes suivantes **en compréhension**.

**a) Liste des entiers pairs entre 0 et 100**
```python
liste_pairs = [p for p in range(0, 101, 2)]
```

**b) Liste des élements de la liste tab dont les indices sont compris entre 2 (inclus) et 10 (exclus)**
```python
tab = [3, -1, 7, 0, 8, -5, 23, 12, -42, 1001, 78, -98, 72, 50]
liste_2_10 = [tab[i] for i in range(2, 10)]
```

**c) Liste des élements de la liste tab dont les indices sont impairs**
```python
tab = [3, -1, 7, 0, 8, -5, 23, 12, -42, 1001, 78, -98, 72, 50]
liste_impairs = [tab[i] for i in range(len(tab)) if i%2 == 1]
```

**d) Liste des élements de la liste tab qui sont divisibles par 7**
```python
tab = [3, -1, 7, 0, 8, -5, 23, 12, -42, 1001, 78, -98, 72, 50]
liste_div_7 = [t for t in tab if t%7 == 0]
```

## Exercice 2 (Sujet BNS 2022 - n°28, ex 1)

Écrire une fonction `moyenne` qui prend en paramètre un tableau non vide de nombres
flottants et qui renvoie la moyenne des valeurs du tableau. Les tableaux seront
représentés sous forme de liste Python.

**Exemples :**
```python
>>> moyenne([1.0])
1.0
>>> moyenne([1.0, 2.0, 4.0])
2.3333333333333335
```

```python linenums='1'
def moyenne(tab:list) -> float:
    somme = 0
    for t in tab:
        somme += t
    return t / len(tab)
```

## Exercice 3 (Sujet BNS 2022 - n°28, ex 2)

On considère la fonction `dec_to_bin` ci-dessous qui prend en paramètre un entier positif `a` en écriture décimale et qui renvoie son écriture binaire sous la forme d'une chaine de caractères.

**Exemples:**

```python
>>> dec_to_bin(83)
'1010011'
>>> dec_to_bin(127)
'1111111'
```


Compléter le code ci-dessous. N'oubliez pas de convertir vos entiers en chaînes de caractères avec la fonction `str()`.

=== "Énoncé" 
    ```python linenums='1'
    def dec_to_bin(a):
        bin_a = ...
        a = a // 2
        while ... :
            bin_a = ... + bin_a
            a = ...
        return bin_a
    ```
=== "Correction" 
    ```python linenums='1'
    def dec_to_bin(a):
        bin_a = str(a%2)
        a = a // 2
        while a != 0 :
            bin_a = str(a%2) + bin_a
            a = a // 2
        return bin_a
    ```


## Exercice 4

Proposer une version récursive de la fonction `dec_to_bin` précédente.

```python linenums='1'
def dec_to_bin_rec(n):
    if n // 2 == 0:
        return str(n%2)
    else:
        return bin_rec(n//2) + str(n%2)

```
