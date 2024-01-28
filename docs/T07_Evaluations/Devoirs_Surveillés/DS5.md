# DS0101 - 19/01/2024 - Corrigé

## Exercice 1: TAD/Programmation

1. Premier passage: 4-9-8-7-4-2 puis 4-8-7-4-2 puis 4-8-4-2

    Deuxième passage: 4-4-2

    Troisième passage: 4-2 (la pile est gagnante)

2. La pile gagnante est la pile B.

3. 

    ```python linenums='1'
    def reduire_triplet_au_sommet(p):
        a = depiler(p)
        b = depiler(p)
        c = sommet(p)
        if a % 2 != c % 2 : #le premier (a) et le troisième (c) ne sont pas de même parité
            empiler(p, b) # on ne supprime pas b donc on l'empile
        empiler(p, a) # dans tous les cas on empile a
    ```
4.  

    **a.** Il faut au minimum 3 éléments pour pouvoir simplifier et qu'il n'en reste que deux.

    **b.** 
    ```python linenums='1'
    def parcourir_pile_en_reduisant(p):
        q = creer_pile_vide()
        while taille(p) >= 3:
            reduire_triplet_au_sommet(p)
            e = depiler(p)
            empiler(q, e)
        while not est_vide(q):
            e = depiler(q)
            empiler(p, e)
    ```

    **c.**

    ```python linenums='1'
    def jouer(p):
        t = taille(p)
        parcourir_pile_en_reduisant(p)
        if t == taille(p) : # si après réduction la taille est la même, c'est terminé
            return p  # on renvoie la pile
        else:
            return jouer(p) # sinon on recommence
    ```

5. 

    ```python linenums='1'
    class Pile:
        def __init__(self):
            self.contenu = []
            self.taille = 0 # on ajoute l'attribut taille, initialisé à 0

        def est_vide(self):
            return self.contenu == []

        def empiler(self, valeur):
            self.contenu.append(valeur)
            self.taille += 1  # la taille a augmenté de 1

        def depiler(self):
            if not self.est_vide():
                self.taille -= 1  # la taille a diminué de 1
                return self.contenu.pop()

        def longueur(self):
            return self.taille
    ```

6. Cette méthode s'appelle un **accesseur** (ou *getter* en anglais).

7. 

    ```python linenums='1'
    def sommet(p:Pile) -> int:
        '''
        Fonction qui renvoie l'élément au sommet de la pile p
        sans le retirer.
        '''
        if not p.est_vide():
            s = p.depiler()
            p.empiler(s)
            return s
    ```

## Exercice 2: Bases de données/SQL

1. **a.** Une clé primaire d’une relation est un attribut (ou plusieurs attributs) dont la valeur permet d'identifier de manière unique un enregistrment (p-uplet) de la relation.

    **b.** Une clé étrangère est un attribut qui permet d’établir un lien entre deux relations.

    **c.** Un abonné ne peut pas réserver plusieurs fois la même séance, car le couple `idAbonné, idSéance` est une clé primaire pour la relation **Réservation**. Il est donc impossible d’avoir deux fois la même séance pour le même abonné.

2. **a.** On complète le tableau avec dans l'ordre les valeurs 13, 737, 3 et 2.

    **b.** En SQL on obtient:

    ```sql
    INSERT INTO Reservation
    VALUES (13, 737, 3, 2);
    ```

3. Cette requête permet de déterminer le nombre de séances proposées les 10 et 11 janvier 2023.

4. En SQL on obtient les requêtes:

    **a.**

    ```sql
    SELECT nom, prenom FROM Abonne;
    ```

    **b.**

    ```sql
    SELECT titre, realisateur
    FROM Film
    WHERE duree < 120;
    ```

    **c.**

    ```sql
    SELECT Film.titre, Film.duree FROM Film
    JOIN Seance ON Film.idFilm = Seance.idFilm
    WHERE Seance.date = '2023-01-14' AND Seance.heure = '21:00';
    ```

5. **a.** On obtient:

    ```sql
    UPDATE Film
    SET duree = 131 
    WHERE titre = 'Wakanda forever';
    ```

    **b.** `idSéance` est une clé étrangère pour la relation **Réservation**. La suppression d’une séance risque donc de provoquer des problèmes dans la relation **Réservation** (avec un `Réservation.idSéance` ne correspondant à aucun `Séance.idRéservation`). Cela pourrait enfreindre la contrainte de référence.

    **c.** On l'écrirait:

    ```sql
    DELETE FROM Seance
    WHERE idSeance = 135;
    ```


## Exercice 3: Réseaux/routage

### Partie 1: adresses IP

1. Il s'agit de celle d'Alice.

2. - Pour le réseau L1, le masque s'écrit en binaire 11111111.11111111.11111111.00000000 et en décimal 255.255.255.0. On peut y connecter $2^8-2=254$ machines.
    - Pour le réseau L2, le masque s'écrit en binaire 11111111.11111111.11111111.11000000 et en décimal 255.255.192.0. On peut y connecter $2^6-2=62$ machines.

3. L'adresse IP 192.168.2.88 partage les 3 premiers octets (24 bits) de l'adresse réseau de L2. Mais 88 s'écrit 01011000 en binaire et ne commence pas par 00 donc elle n'a pas les même 26 premiers bits identiques à celle du réseau L2. Donc la réponse est négative.

### Partie 2: le protocole RIP

4. Dans le protocole RIP les routeurs s'échangent leurs tables de routage toutes les 30 secondes et les mettent à jour en prenant pour chaque destination la distance la plus courte au sens du nombre de sauts (entre deux routeurs), jusqu'à stabilisation des tables.

5. On obtient le tableau:

| Routeur | Destination | Passerelle | Distance |
|:-------:|:-----------:|:----------:|:--------:|
|    A    |      G      |      B     |     3    |
|    B    |      G      |      F     |     2    |
|    C    |      G      |      B     |     3    |
|    D    |      G      |      E     |     3    |
|    E    |      G      |      F     |     2    |
|    F    |      G      |      -     |     1    |

6. Le message transite via les routeurs A -> B -> F -> G.

7. Le routeur B envoie la distance 16 (l'infini) car il n'a plus de route vers G.

8. **a.** Trivial.

    **b.** Par exemple, la table de routage de A sera modifiée pour la destination E avec une passerelle H et une distance de 2 (contre C / 3 auparavant).

    **c.** On obtient la table:

    | Destination | Passerelle | Distance |
    |:-----------:|:----------:|:--------:|
    |      A      |      -     |     1    |
    |      B      |      A     |     2    |
    |      C      |      A     |     2    |
    |      D      |      E     |     2    |
    |      E      |      -     |     1    |
    |      F      |      E     |     2    |

### Partie 3: le protocole OSPF

9. Le débit maximal de référence est de 1 Gbits/s, soit $10^9$ bits/s et le débit du réseau est de 100 Mbits/s soit $100\times 10^6 = 10^8$ bits/s. Le coût est donc bien de $\dfrac{10^9}{10^8}=10$.

10. Le coût étant 2 fois moindre que le précédent, on en déduit que le débit est deux fois plus rapide, soit 200 Mbits/s.

11. **a.** On obtient le chemin G -> F -> B -> -> C -> A pour un coût total de 16.

    **b.** C'est le routeur B.