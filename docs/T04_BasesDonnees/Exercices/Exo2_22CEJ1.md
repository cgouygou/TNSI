# Exercice BAC 2: Mesures du réchauffement climatique

Dans le cadre d'une étude sur le réchauffement climatique, un centre météorologique rassemble des données. On considère que la base de données contient deux relations (tables). La relation **`Centres`** qui contient l'identifiant des centres météorologiques, la ville, la latitude, la longitude et l'altitude du centre. La relation **`Mesures`** qui contient l'identifiant de la mesure, l'identifiant du centre, la date de la mesure, la température, la pression et la pluviométrie mesurées.

Le schéma relationnel de la relation **`Centres`** est le suivant :

`#!sql Centres(id_centre: INT, nom_ville: VARCHAR, latitude: FLOAT, longitude: FLOAT, altitude: FLOAT)`

Le schéma relationnel de la relation **`Mesures`** est le suivant :

`#!sql Mesures(id_mesure: INT, id_centre: INT, date_mesure: DATE, temperature: FLOAT, pression: INT, pluviometrie: INT)`

On fournit ci-dessous le contenu des deux relations.

**Relation `Centres`**

| `id_centre` | `nom_ville`     | `latitude` | `longitude` | `altitude` |
| ----------: | :-------------- | ---------: | ----------: | ---------: |
|         213 | Amiens          |     49.894 |       2.293 |         60 |
|         138 | Grenoble        |     45.185 |       5.723 |        550 |
|         263 | Brest           |     48.388 |       -4.49 |         52 |
|         185 | Tignes          |     45.469 |       6.909 |       2594 |
|         459 | Nice            |     43.706 |       7.262 |        260 |
|         126 | Le Puy-en-Velay |     45.042 |       3.888 |        744 |
|         317 | Gérardmer       |     48.073 |       6.879 |        855 |


**Relation `Mesures`**

| `id_mesure` | `id_centre` | `date_mesure` | `temperature` | `pression` | `pluviometrie` |
| ----------: | ----------: | :------------ | ------------: | ---------: | -------------: |
|        1566 |         138 | 2021-10-29    |           8.0 |       1015 |              3 |
|        1568 |         213 | 2021-10-29    |          15.1 |       1011 |              0 |
|        2174 |         126 | 2021-10-30    |          18.2 |       1023 |              0 |
|        2200 |         185 | 2021-10-30    |           5.6 |        989 |             20 |
|        2232 |         459 | 2021-10-31    |          25.0 |       1035 |              0 |
|        2514 |         213 | 2021-10-31    |          17.4 |       1020 |              0 |
|        2563 |         126 | 2021-11-01    |          10.1 |       1005 |             15 |
|        2592 |         459 | 2021-11-01    |          23.3 |       1028 |              2 |
|        3425 |         317 | 2021-11-02    |           9.0 |       1012 |             13 |
|        3430 |         138 | 2021-11-02    |           7.5 |        996 |             16 |
|        3611 |         263 | 2021-11-03    |          13.9 |       1005 |              8 |
|        3625 |         126 | 2021-11-03    |          10.8 |       1008 |              8 |

**1.a.** Proposer une clé primaire pour la relation **`Mesures`**. Justifier votre choix.

**1.b.** Avec quel attribut peut-on faire une jointure entre la relation **`Centres`** et la relation **`Mesures`** ?

**2.a.** Qu'affiche la requête suivante ?

```sql
SELECT * FROM Centres WHERE altitude > 500;
```

**2.b.** On souhaite récupérer le nom de la ville des centres météorologiques situés à une altitude comprise entre 700 m et 1200 m. Écrire la requête SQL correspondante.

**2.c.** On souhaite récupérer la liste des longitudes et des noms des villes des centres météorologiques dont la longitude est supérieure à 5. La liste devra être triée par ordre alphabétique des noms de ville. Écrire la requête SQL correspondante.

**3.a.** Qu'affiche la requête suivante ?

```sql
SELECT * FROM Mesures WHERE date_mesure = "2021-10-30";
```

**3.b.** Écrire une requête SQL permettant d'ajouter une mesure prise le 8 novembre 2021 dans le centre numéro 138, où la température était de 11 °C, la pression de 1013 hPa et la pluviométrie de 0 mm. La donnée dont l'attribut est `id_mesure` aura pour valeur 3650.

**4.a.** Expliquer ce que renvoie la requête SQL suivante.

```sql
SELECT * FROM Centres WHERE latitude = (SELECT MIN(latitude) FROM Centres);
```

**4.b.** Écrire une requête SQL donnant la liste des villes dans lesquelles on a enregistré une température inférieure à 10 °C en octobre 2021. On utilisera le mot clé `#!sql DISTINCT` afin d'éviter d'avoir des doublons. On rappelle que l'on peut utiliser les opérateurs de comparaison avec les dates.
