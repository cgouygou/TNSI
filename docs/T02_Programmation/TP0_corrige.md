# Corrigé du TP Zéro


!!! example "Exercice 1"
	Écrire une fonction `maximum` qui prend deux entiers en paramètres et qui renvoie le plus grand des deux.

	**Fonction `#!py max` interdite**.


	```python
	def maximum(a:int, b:int) -> int:
		if a > b:
		    return a
		return b
	```

!!! example "Exercice 2"
	Écrire une fonction `somme_et_produit` qui prend deux entiers en paramètres et qui renvoie un tuple contenant leur somme et leur produit.

	```python
	def somme_et_produit(a:int, b:int) -> tuple:
    	return a + b, a * b
	```

!!! example "Exercice 2 bis"
	Écrire une fonction `somme_et_produit_str` qui prend deux entiers en paramètres et qui renvoie une chaîne de caractères donnant leur somme et leur produit.
	
	```python
	def somme_et_produit(a:int, b:int) -> str:
    	return f"La somme de {a} et {b} est {a + b} et leur produit est {a * b}."

	```

!!! example "Exercice 3"
	Écrire une fonction `somme` qui prend en paramètre un entier et qui renvoie la somme de tous les entiers inférieurs. 
	Par exemple, `somme(5)` doit renvoyer `10` car $1+2+3+4=10$.

	```python
	def somme(n:int) -> int:
		s = 0
		for k in range(n):
			s = s + k
    	return s
	
	assert somme(5) == 10
	assert somme(0) == 0
	```

!!! example "Exercice 4"
	Écrire une fonction `fais6stp` qui simule des lancers de dés et qui donne le nombre de tentatives avant d'avoir obtenu un 6.

	On utilise la fonction `#!py randint` du module `#!py random`.

	Pas de tests possibles, puisque le pseudo-hasard intervient.

	```python
	import random

	def fais6stp():
		nb_tentatives = 0
		de = 0
		while de != 6:
		    de = random.randint(1, 6)
		    nb_tentatives += 1
		return nb_tentatives
	```

!!! example "Exercice 5"
	Écrire une fonction `somme_liste` qui prend en paramètre une liste (d'entiers) et qui renvoie la somme de ses éléments.

	!!! info "Rappel"
		Il est primordial de savoir faire un parcours de liste par indice ou par élément.
		Ici un parcours de liste par élément est possible (pas besoin des indices).

	=== "Parcours par élément"	
		```python
		def somme_liste(tab:list) -> int:
			somme = 0
			for nb in tab:
				somme += nb
			return somme

		assert somme_liste([5, 1, 2]) == 8
		assert somme_liste([]) == 0
		```
	=== "Parcours par indice"	
		```python
		def somme_liste(tab:list) -> int:
			somme = 0
			for i in range(len(tab)):
				somme += tab[i]
			return somme

		assert somme_liste([5, 1, 2]) == 8
		assert somme_liste([]) == 0
		```

!!! example "Exercice 6"
	Écrire une fonction `echange` qui prend en paramètre une liste `tab`, deux entiers `i` et `j` et qui renvoie la liste dont les éléments d'indices `i` et `j` ont été échangés.

	```python
	def echange(tab:list, i:int, j:int) -> list:
		temp = tab[i]
		tab[i] = tab[j]
		tab[j] = temp
		return tab
	```

