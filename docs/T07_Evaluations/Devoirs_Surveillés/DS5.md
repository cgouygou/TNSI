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
4. **a.** Il faut au minimum 3 éléments pour pouvoir simplifier et qu'il n'en reste que deux.

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
