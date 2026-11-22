# EXERCICE 1 (6 points)

Cet exercice porte sur les bases de données relationnelles et le langage SQL.

Les mots clés du langage SQL suivants pourront être utilisés dans les requêtes :

`SELECT FROM`, `WHERE`, `JOIN ON`, `INSERT INTO VALUES`, `UPDATE SET`, `COUNT`, `AND`, `OR`, `DISTINCT`.

Pour rappel : le mot clé `DISTINCT` est utilisé pour supprimer les doublons des résultats d'une requête, en ne retournant que des lignes uniques.

On s’intéresse dans cet exercice à la mise à disposition de données « temps réel » de qualité de l’air.

Le Bureau de la Qualité de l’Air (BQA) au sein du Ministère de la Transition Ecologique et Solidaire (MTES) a mandaté le Laboratoire Central de Surveillance de la Qualité de l’Air (LCSQA) pour organiser la mise à disposition du public au niveau national des données « temps réel » des mesures des concentrations de polluants atmosphériques.

Les données d’observation sont issues de la surveillance réglementaire de la qualité de l’air. Elles décrivent les concentrations moyennes horaires des polluants réglementés surveillés par des appareils de mesure automatiques installés sur des stations fixes.

Les stations de mesure de la qualité de l’air sont gérées par les Associations Agréées de Surveillance de la Qualité de l’Air (AASQA). Les AASQA sont donc producteurs et responsables de ces données. On compte 18 AASQA, correspondant aux régions métropolitaines et aux départements et régions d'outre-mer.

Les données disponibles permettent de documenter les concentrations de polluants atmosphériques (ozone O3, monoxyde d'azote NO et dioxyde d’azote NO2, dioxyde de soufre SO2, particules de diamètre inférieur à 10 µm PM10, particules de diamètre inférieur à 2,5 µm PM2.5, monoxyde de carbone CO, etc.).

Les stations dont sont issues les observations ne disposent pas toutes de mesures pour l’ensemble de ces polluants, certaines ne mesurent qu’un seul polluant de la liste, d’autres en mesurent plusieurs.

Pour cet exercice, le modèle relationnel suivant a été retenu :

## Modèle relationnel

### Relation `AASQA`

| Attribut | Type |
|---|---|
| <u>Id</u> | CHAR(7) |
| Nom | VARCHAR(50) |
| FuseauHoraire | VARCHAR(50) |
| Siteweb | VARCHAR(50) |

### Relation `Station`

| Attribut | Type |
|---|---|
| <u>Id</u> | CHAR(7) |
| Nom | VARCHAR(50) |
| Latitude | DECIMAL(10,6) |
| Longitude | DECIMAL(10,6) |
| Altitude | INT |
| TypeImplantation | VARCHAR(50) |
| AASQAId | CHAR(7) |

### Relation `Mesure`

| Attribut | Type |
|---|---|
| <u>StationId</u> | CHAR(7) |
| <u>DateDebut</u> | DATETIME |
| <u>DateFin</u> | DATETIME |
| <u>Polluant</u> | VARCHAR(50) |
| TypeInfluence | VARCHAR(50) |
| Valeur | DECIMAL(10,1) |

Les clés primaires sont soulignées.

Les éventuelles clés étrangères ne sont volontairement pas identifiées.

Une AASQA gère zéro, une ou plusieurs stations et une station est gérée par une et une seule AASQA. De la même façon, une station réalise zéro, une ou plusieurs mesures et une mesure est réalisée par une et une seule station.

Quelques occurrences de chaque table ou relation sont données ci-dessous.

### Relation `AASQA`

| Id | Nom | FuseauHoraire | Siteweb |
|---|---|---|---|
| FR072A | AIR BREIZH | UTC | http://www.airbreizh.asso.fr |
| FR004A | AIRPARIF | UTC | http://www.airparif.asso.fr |
| FR061A | LIG'AIR | UTC | https://www.ligair.fr |
| FR065A | QUALITAIR CORSE | UTC | http://www.qualitaircorse.org |
| FR064A | GWAD'AIR | UTC-4 | http://www.gwadair.fr |
| FR077A | HAWA MAYOTTE | UTC+3 | http://www.hawa-mayotte.fr |
| FR069A | ATMO NORMANDIE | UTC | http://www.atmonormandie.fr/ |
| FR068A | ATMO OCCITANIE | UTC | http://atmo-occitanie.org/ |
| FR071A | ATMO AUVERGNE-RHONE-ALPES | UTC | http://www.atmo-auvergnerhonealpes.fr/ |
| FR076A | ATMO BOURGOGNE-FRANCHE-COMTE | UTC | https://atmo-bfc.org/ |
| FR074A | ATMO HAUTS DE FRANCE | UTC | http://www.atmo-hdf.fr |

### Relation `Station`

| Id | Nom | Latitude | Longitude | Altitude | TypeImplantation | AASQAId |
|---|---|---|---|---|---|---|
| FR37040 | ABYMES RN1 | 16.254086 | -61.53713 | 13 | Périurbaine | FR064A |
| FR05083 | Gonfreville l Orcher | 49.50273 | 0.232486 | 80 | Urbaine | FR069A |
| FR33203 | Annecy Rocade | 45.9097 | 6.11825 | 452 | Urbaine | FR071A |
| FR07056 | Pays du Mezenc | 44.98377 | 4.226006 | 1191 | Rurale régionale | FR071A |
| FR04143 | Paris Centre | 48.859 | 2.351 | 37 | Urbaine | FR004A |

### Relation `Mesure`

La colonne `Valeur` est donnée en µg/m³.

| StationId | DateDebut | DateFin | Polluant | TypeInfluence | Valeur |
|---|---|---|---|---|---|
| FR05083 | 15/04/2022 00:00 | 15/04/2022 01:00 | SO2 | Industrielle | 3.3 |
| FR05083 | 15/04/2022 01:00 | 15/04/2022 02:00 | SO2 | Industrielle | 3.3 |
| FR33203 | 15/04/2022 07:00 | 15/04/2022 08:00 | PM10 | Trafic | 66.5 |
| FR33203 | 15/04/2022 08:00 | 15/04/2022 09:00 | PM10 | Trafic | 45 |
| FR07056 | 15/04/2022 13:00 | 15/04/2022 14:00 | O3 | Fond | 101.2 |
| FR07056 | 15/04/2022 14:00 | 15/04/2022 15:00 | O3 | Fond | 102.7 |

## Partie A : Modèle relationnel

1. Expliquer le rôle de la clé primaire dans une relation.

2. Donner les quatre attributs formant la clé primaire pour la relation `Mesure`.

3. Expliquer le rôle d'une clé étrangère.

4. Donner un exemple de clé étrangère dans le modèle relationnel ci-dessus.

## Partie B : Alimentation de la base de données

Chaque jour des mesures sont réalisées. Il faut ajouter ces mesures à la base de données.

5. Écrire une requête SQL permettant de rajouter à la table `Mesure` la mesure de valeur 34, du polluant PM10 (type d'influence "Trafic"), le 20/06/2022 de 10h à 11h pour la station "Annecy Rocade".

6. L’attribut `StationId` dans la table `Mesure` est une clé étrangère faisant référence à l’identifiant d’une station. Lors de l'ajout à la table `Mesure` de la mesure de valeur 13.5, du polluant O3 (type d'influence "Fond"), le 20/06/2022 de 00h à 01h pour la station d'identifiant "FR41017", l'exécution échoue et l'exception suivante est levée :

   ```text
   IntegrityError: FOREIGN KEY constraint failed
   ```

   Expliquer cette erreur.

## Partie C : Exploitation de la base de données

7. Écrire une requête SQL permettant d'afficher le nom et le site web des AASQA.

8. Écrire une requête SQL permettant d'afficher le nombre total de stations.

9. Expliquer à quoi sert la requête suivante :

   ```sql
   SELECT Station.Nom, Station.TypeImplantation
   FROM AASQA JOIN Station ON AASQA.Id = Station.AASQAId
   WHERE AASQA.Nom = "ATMO AUVERGNE-RHONE-ALPES";
   ```

Pour les questions suivantes, on considère l’AASQA "Air Pays de la Loire" et la station "Mazagran" (qui sont connues dans la base de données).

10. Écrire une requête SQL permettant d'afficher la date de début, la date de fin et la valeur du polluant PM10 pour la station "Mazagran".

11. Écrire une requête SQL permettant d’afficher la liste sans doublon des polluants de la station "Mazagran".

12. Écrire une requête SQL permettant d'afficher le nom des stations gérées par "Air Pays de la Loire" et pour ces stations la valeur, la date de début et la date de fin des mesures du polluant NO2.
