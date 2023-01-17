# DL 0110

À rendre le mardi 17 janvier au plus tard.

## Exercice 1 : Bases de données et dictionnaires

*On pourra utiliser les mots clés SQL suivants :*

`AND`, `SELECT`, `FROM`, `WHERE`, `JOIN`, `INSERT INTO`, `VALUES`, `COUNT`, `ORDER BY`, `OR`, `ON`, `SET`, `UPDATE`.


On étudie une base de données permettant la gestion de l'organisation d'un festival de musique de jazz, dont voici le schéma relationnel comportant trois relations :


- la relation {{ relation("groupes", "id_groupe", "nom", "style", "nb_pers") }}
- la relation {{ relation("musiciens", "id_musicien", "nom", "prenom", "instru","#id_groupe") }}
- la relation {{ relation("concerts", "id_concert", "scene", "heure_debut", "heure_fin","#id_groupe") }}

Dans ce schéma relationnel :

- les clés primaires sont soulignées ;
- les clés étrangères sont précédées d'un #.
Ainsi `concerts.id_groupe` est une clé étrangère faisant référence à `groupes.id_groupe`.

Voici un extrait des tables **`groupes`**, **`musiciens`** et **`concerts`** :

!!! note "Extrait de **`groupes`**"
            
    | `id_groupe` |        `nom`         |    `style`    | `nb_pers` |
    | :---------: | :------------------: | :-----------: | :-------: |
    |     `12`      |   `'Weather Report'`   | `'Jazz Fusion'` |     `5`     |
    |     `25`      |    `'The 3 Sounds'`    |  `'Soul Jazz'`  |     `4`     |
    |     `87`      | `'Return to Forever'`  | `'Jazz Fusion'` |     `8`     |
    |     `96`      | `'The Jazz Messenger'` |  `'Hard Bop'`   |     `3`     |

!!! note "Extrait de **`musiciens`**"

    | `id_musicien` |   `nom`   | `prenom`  |     `instru`     | `id_groupe` |
    | :-----------: | :-------: | :-------: | :--------------: | :---------: |
    |      `12`       | `'Garrett'` |  `'Kenny'`  | `'saxophone alto'` |     `96`      |
    |      `13`       | `'Garrett'` |  `'Kenny'`  |     `'flute'`      |     `25`      |
    |      `58`       |  `'Corea'`  | `'Chick'`  |     `'piano'`      |     `87`      |
    |      `97`       | `'Clarke'`  | `'Stanley'` |     `'basse'`      |     `87`      |


!!! note "Extrait de **`concerts`**"

    | `id_concert` | `scene` | `heure_debut` | `heure_fin` | `id_groupe` |
    | :----------: | :-----: | :-----------: | :---------: | :---------: |
    |      `10`      |    `1`    |   `'20 h 00'`   |  `'20 h 45'`  |     `12`      |
    |      `24`      |    `2`    |   `'20 h 00'`   |  `'20 h 45'`  |     `15`      |
    |      `36`      |    `1`    |   `'21 h 00'`   |  `'22 h 00'`  |     `96`      |
    |      `45`      |    `3`    |   `'18 h 00'`   |  `'18 h 30'`  |     `87`      |


**1.**  Citer les attributs de la table **`groupes`**.

??? success "Réponse"
    Les attributs de la table groupes sont : id_groupe, nom, style et nb_pers.

**2.**  Justifier que l'attribut `nom` de la table **`musiciens`** ne peut pas être une clé primaire.

??? success "Réponse"
    Une clé primaire doit être unique. Le nom 'Garrett' apparait plusieurs fois, donc le nom ne peut être une clé primaire.

**3.** En s'appuyant uniquement sur l'extrait des tables fourni ci-dessus écrire ce que renvoie la requête :

```sql
SELECT nom
FROM groupes
WHERE style = 'Jazz Fusion';
```

??? success "Réponse"
    La requête renvoie : `'Weather Report'` et `'Return to Forever'`.

**4.** Le concert dont l'`id_concert` est `36` finira à 22 h 30 au lieu de 22 h 00. 

Écrire une requête SQL permettant de mettre à jour la relation **`concerts`** pour modifier l'horaire de fin de ce concert.

??? success "Réponse"

    ```sql
    UPDATE concerts
    SET heure_fin = '22 h 30'
    WHERE id_concert = 36;
    ```

**5.** Fournir une seule requête SQL permettant d'ajouter dans la relation **`groupes`** le groupe `'Smooth Jazz Fourplay'`, de style `'Free Jazz'`, composé de 4 membres. Ce groupe aura un `id_groupe` de 15.

??? success "Réponse"
    ```sql
    INSERT INTO groupes (id_groupe, nom, style, nb_pers)
    VALUES (15, 'Smooth Jazz Fourplay', 'Free Jazz', 4);
    ```

**6.**  Donner une seule requête SQL permettant de récupérer le nom de tous les groupes qui jouent sur la scène 1.

??? success "Réponse"

    ```sql
    SELECT groupes.nom FROM groupes
    JOIN concerts
    ON concerts.id_groupe = groupes.id_groupe
    WHERE concerts.scene = 1;
    ```

Les données sont ensuite récupérées pour être analysées par la société qui produit les festivals de musique. Pour ce faire, elle utilise la programmation en Python afin d'effectuer certaines opérations plus complexes.

Elle stocke les données relatives aux musiciens sous forme d'un tableau de dictionnaires dans laquelle a été ajouté le nombre de concerts effectués par chaque musicien :

```python
>>> print(musiciens)
  [{'id_musicien': 12, 'nom': 'Garrett', 'prenom': 'Kenny',
    'instru': 'saxophone alto', 'id_groupe' : 96, 'nb_concerts': 5},
   {'id_musicien': 13, 'nom': 'Garrett', 'prenom': 'Kenny',
    'instru': 'flute', 'id_groupe' : 25, 'nb_concerts': 9},
   {'id_musicien': 58, 'nom': 'Corea', 'prenom': 'Chick',
    'instru': 'piano', 'id_groupe' : 87, 'nb_concerts': 4},
   {'id_musicien': 97, 'nom': 'Clarke', 'prenom': 'Stanley',
    'instru': 'basse', 'id_groupe' : 87, 'nb_concerts': 4},
   ...
  ]
```

**7.**  Écrire la fonction `recherche_nom` ayant pour unique paramètre un tableau de dictionnaires (comme `musiciens` présenté précédemment) renvoyant une liste contenant le nom de tous les musiciens ayant participé à au moins 4 concerts.

??? success "Réponse"

    ```python
    def recherche_nom(musiciens):
        resultat = []
        for musicien in musiciens:
            if musicien['nb_concerts'] >= 4:
                resultat.append(musicien['nom'])
        return resultat
    ```


## Exercice 2: Réseaux (rappels de Première)

!!! info "Rappels"
    - Une adresse IPv4 est composée de 4 octets, soit 32 bits. Elle est notée `a.b.c.d`, où `a`, `b`, `c` et `d` sont les valeurs des 4 octets.

    - La notation `a.b.c.d/n` signifie que les `n` premiers bits de l'adresse IP représentent la partie « réseau », les bits qui suivent représentent la partie « machine ».

    - L'adresse IPv4 dont tous les bits de la partie « machine » sont à 0 est appelée « adresse du réseau ».

    - L'adresse IPv4 dont tous les bits de la partie « machine » sont à 1 est appelée « adresse de diffusion » (broadcast).


**1.** Comment s'appelle la valeur `n` dans la notation `a.b.c.d/n`? Dans le cas où cette valeur vaut 24, comment la note-t-on également?

??? success "Réponse"
	`n` est la valeur du masque de sous-réseau. Si elle vaut 24, on l'écrit avec les 24 bits de poids fort égaux à 1, le reste à 0, c'est-à-dire `11111111.11111111.11111111.00000000`, ou bien encore `255.255.255.0`.

**2.a.** Donner en écriture décimale l'adresse IPv4 correspondant à l'écriture binaire : 11000000.10101000.10000000.10000011.

??? success "Réponse"
	On obtient l'adresse `192.168.128.131`.


**2.b** L'adresse IPv4 `192.168.128.145` et celle de la question précédente font-elle partie du même sous-réseau `192.168.128.128/28`?

??? success "Réponse"
	Puisque le masque est de 28 pour ce sous-réseau, les adresses doivent avoir en commun leurs 28 bits de poids forts. C'est le cas pour les 24 premiers puisque les 3 adresses commencent par `192.168.128`. Il ne reste donc qu'à comparer les 4 bits de poids fort du dernier octet des  adresses.

	Or 128 s'écrit `10000000`, 131 s'écrit `10000011` et 145 s'écrit `10010001`. La première adresse en fait donc partie, mais pas la deuxième.

À partir de la question suivante, on considère le réseau représenté ci-dessous:

![Réseau](../images/reseau_clair.svg#only-light){: .center width=75%}

![Réseau](../images/reseau_sombre.svg#only-dark){: .center width=75%}

**3.** On considère la machine d'adresse IPv4 `192.168.1.1`.

**3.a.** Donner l'adresse du réseau sur lequel se trouve cette machine.

??? success "Réponse"
	L'adresse du réseau est `192.168.1.0`

**3.b.** Donner l'adresse de diffusion (broadcast) de ce réseau.

??? success "Réponse"
	L'adresse de diffusion de ce réseau est `192.168.1.255`

**3.c.** Donner le nombre maximal de machines que l'on peut connecter sur ce réseau.

??? success "Réponse"
	On peut donc connecter à ce réseau 254 machines (256 moins les 2 précédentes).

**3.d.** On souhaite ajouter une machine sur ce réseau, proposer une adresse IPv4 possible pour cette machine.

??? success "Réponse"
	On peut proposer n'importe quelle adresse de la forme `192.168.1.d` où `d` est un entier compris entre 1 et 254.

**4.** La machine d'adresse IPv4 `192.168.1.1` transmet un paquet IPv4 à la machine d'adresse IPv4 `192.168.4.2`. Donner toutes les routes pouvant être empruntées par ce paquet IPv4, chaque routeur ne pouvant être traversé qu'une seule fois.

  Par exemple, une route possible est A → B → C → E → D.

??? success "Réponse"
	Outre A → B → C → E → D, les autres routes possibles sont:
	
	- A → B → C → F → D
	- A → C → E → D
	- A → C → F → D
	- A → E → C → F → D
	- A → E → D