# Exercice BAC 1 : Base de données musicale

> D'après 2022, Métropole, J2, Ex. 4
 
On pourra utiliser les mots clés SQL suivants : `#!sql SELECT,  FROM,  WHERE,  JOIN,  ON,  INSERT,  INTO,  VALUES,  UPDATE,  SET,  AND`. 

La clause `#!sql ORDER BY` suivie d'un attribut permet de trier les résultats par ordre croissant de l'attribut.
L'instruction `#!sql COUNT(*)` renvoie le nombre de lignes d'une requête.

Un musicien souhaite créer une base de données relationnelle contenant ses morceaux et interprètes préférés. Pour cela il utilise le langage SQL.

Il crée une table **`morceaux`** qui contient entre autres attributs les titres des morceaux et leur année de sortie :

| `id_morceau` |         `titre`          | `annee` | `id_interprete` |
| :----------: | :----------------------: | :-----: | :-------------: |
|      1       |   Like a Rolling Stone   |  1965   |        1        |
|      2       |         Respect          |  1967   |        2        |
|      3       |         Imagine          |  1970   |        3        |
|      4       |         Hey Jude         |  1968   |        4        |
|      5       | Smells Like Teen Spirit  |  1991   |        5        |
|      6       | I Want To hold Your Hand |  1963   |        4        |

Il crée la table **`interpretes`** qui contient les interprètes et leur pays d'origine :

| `id_interprete` |      `nom`      |   `pays`   |
| :-------------: | :-------------: | :--------: |
|        1        |    Bob Dylan    | États-Unis |
|        2        | Aretha Franklin | États-Unis |
|        3        |   John Lennon   | Angleterre |
|        4        |   The Beatles   | Angleterre |
|        5        |     Nirvana     | États-Unis |

`id_morceau` de la table **`morceaux`** et `id_interprete` de la table **`interpretes`** sont des clés primaires.

L'attribut `id_interprete` de la table **`morceaux`** fait directement référence à la clé primaire de la table **`interpretes`**.

**1.a.** Écrire le résultat de la requête suivante :

```SQL
SELECT titre
    FROM morceaux
    WHERE id_interprete = 4;
```


**1.b.** Écrire une requête permettant d'afficher les noms des interprètes originaires d'Angleterre.


**1.c.** Écrire le résultat de la requête suivante :

```SQL
SELECT titre, annee
    FROM morceaux
    ORDER BY annee;
```

**1.d.** Écrire une requête permettant de calculer le nombre de morceaux dans la table **`morceaux`**.

**1.e.** Écrire une requête affichant les titres des morceaux par ordre alphabétique.

**2.a.** Citer, en justifiant, la clé étrangère de la table **`morceaux`**.

**2.b.** Écrire un schéma relationnel des tables **`interpretes`** et **`morceaux`**.

**2.c.** Expliquer pourquoi la requête suivante produit une erreur :

```SQL
INSERT INTO interpretes
    VALUES (1, 'Trust', 'France');
```

**3.a.** Une erreur de saisie a été faite. Écrire une requête SQL permettant de changer l'année du titre « Imagine » en 1971.

**3.b.** Écrire une requête SQL permettant d'ajouter l'interprète « The Who » venant d'Angleterre à la table **`interpretes`**. On lui donnera un `id_interprete` égal à 6.

**3.c.** Écrire une requête SQL permettant d'ajouter le titre « My Generation » de « The Who » à la table **`morceaux`**. Ce titre est sorti en 1965 et on lui donnera un `id_morceau` de 7 ainsi que l'`id_interprete` qui conviendra.

**4.** Écrire une requête permettant de lister les titres des interprètes venant des États-Unis.


