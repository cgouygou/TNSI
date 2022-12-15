# Terminale NSI - DS 0101 - 09/12/2022

**Nom Prénom:**

---
**Note/Appréciation:**

<br>
<br>
<br>
<br>

---

## Exercice 1 (8 points)

On veut créer une base de données ```baseHopital.db```  qui contiendra les trois tables correspondant au diagramme relationnel suivant :

![](diag_ex1_b.png)

On suppose que les dates sont données sous la forme ```aaaa--mm-jj```.



1. Écrire le schéma de la relation **ordonnances**. Souligner la clé primaire et  marquer d'un # les clés étrangères.

**ordonnances(<span class="cle-primaire"> code Int</span>, #id_patient Int, #matricule_medecin Int, date_ord Date, medicmaents String)

2. Donner l'instruction SQL permettant de créer la table/relation **ordonnances**.
```sql
CREATE TABLE ordonnances(
	code INTEGER PRIMARY KEY,
	id_patient INTEGER REFERENCES Patients(Id),
	matricule_medecin INTEGER REFERENCES Medecins(matricule),
	date_ord DATE,
	medicaments TEXT
);
```

3. Mme Anne Vegue, née en 2000 et demeurant 3 rue des Pignons Verts 12345 Trouperdu doit être enregistrée comme patiente numéro 1. Donner l'instruction SQL correspondante.
```sql
INSERT INTO patients VALUES (1, "Vegue", "Anne", "F", 2000);
```

4. Le patient numéro 100 a changé de prénom et s'appelle maintenant "Alice". Donner l'instruction SQL modifiant en conséquence ses données.
```sql
UPDATE patients SET prenom = 'Alice' WHERE id = 100 ;
```

5. Par souci d'économie, la direction décide de se passer des médecins spécialisés en épidémiologie. Donner l'instruction SQL permettant de supprimer leurs fiches.
```sql
DELETE FROM medecins WHERE specialite = "épidémiologie";
```

6. Donner la requête SQL permettant d'obtenir la liste des patient(e)s ayant été examiné(e)s par un(e) psychiatre en avril 2020.
```sql
SELECT p.nom, p.prenom FROM patients AS p
JOIN ordonnances AS o ON p.id = o.id_patient
JOIN medecins AS m ON o.matricule_medecin = m.matricule
WHERE m.specialite = "psychiatrie" AND o.date_ord LIKE "%04-2020%";
```

## Exercice 2 (12 points)

On considère ci-dessous le diagramme de la base de données du stock d'un supermarché :

![](diag_ex2_b.png)

1. Proposer un type de domaine pertinent pour l'attribut `cp`  de la table **fournisseur**.

	L'attribut `cp` doit être représenté par un type `#!sql VARCHAR(5)` (ou `#!sql CHAR(5)`).

2. Quelle requête SQL donne le prix d'achat du produit dont le ```nom_court``` est «Liq_Vaiss_1L» ?
```sql
SELECT prix_achat FROM produits WHERE nom_court = 'Liq_Vaiss_1L';
```

3. Quelle requête SQL donne l'adresse, le code postal et la ville du fournisseur dont le nom est «Avenir_confiseur» ?
```sql
SELECT adresse, cp, ville FROM fournisseur WHERE nom = 'Avenir_confiseur';
```

4. Quelle requête SQL donne les produits étant en rupture de stock ?
```sql
SELECT produits.nom FROM produits
JOIN stocks ON produits.id = stocks.produit
WHERE stocks.quantite = 0;
```

5. Quelle requête SQL donne la liste de toutes les ampoules vendues en magasin ? On pourra faire l'hypothèse que le nom du produit contient le mot «ampoule».
```sql
SELECT nom FROM produits WHERE nom LIKE "%ampoule%";
```

6. Quelle requête SQL permet d'avoir le prix moyen de ces ampoules ?
```sql
SELECT AVG(prix_vente) FROM produits WHERE nom LIKE "%ampoule%";
```

7. Quelle requête SQL permet d'identifier le produit le plus cher du magasin ?
```sql
SELECT nom FROM produits WHERE prix_vente = (SELECT MAX(prix_vente) FROM produits);
```
Un tri sur le prix de vente par ordre décroissant est accepté.

8. Quelle requête SQL renvoie les noms des produits dont la date de péremption est dépassée ? _(on pourra utiliser la fonction SQL `NOW()`  qui renvoie la date actuelle )_

```sql
SELECT p.nom FROM produits AS p
JOIN stocks AS s ON s.produits = p.id
WHERE s.date_peremption < NOW();
```