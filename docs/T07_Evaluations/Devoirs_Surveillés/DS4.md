# DS0100 - Corrigé

## Exercice 1

1. ![](../images/faro.png){: .center width=480} 
2. Il faut empiler `n` valeurs décroissantes de `n` à `1`.

    ```python
    def produire_jeu(n):
        resultat = Pile()
        for i in range(n):
            resultat.empile(n-i)
        return resultat
    ```

3. Il n'y a seulement que `n // 2` valeurs dans chaque moitié et non `n`, donc il faut rectifier en `for i in range(n // 2)`.

4. 

    ```python
    def recombiner(m1, m2):
        resultat = Pile()
        while not m1.est_vide():
            resultat.empile(m1.depile())
            resultat.empile(m2.depile())
        return resultat
    ```

5. 

    ```python
    def faro(p, n):
        m1, m2 = scinder_jeu(p, n)
        return recombiner(m1, m2)
    ```



## Exercice 2

1. `chien40 = Chien(40, 'Duke', 'wheel dog', 10)`
2. 

    ```python
    def changer_role(self, nouveau_role):
        self.role = nouveau_role
    ```

3. `chien40.changer_role('leader')`
4. On obtient `4.6`.
5. 

    ```python
    def temps_course(equipe):
        cumul = 0
        for temps in equipe.liste_temps:
            cumul += convert(temps)
        return cumul
    ```

6. On obtient l'arbre suivant:
    ![](../images/arbre1.png){: .center width=480} 


7. C'est le parcours infixe.
8. C'est une fonction récursive car elle fait un appel à elle-même ligne 10.
9. Ligne 8 : `arb.gauche = Noeud(eq)`
    Ligne 10 : `inserer(arb.gauche, eq)`
    Ligne 15 : `inserer(arb.droit, eq)`

10. 

    ```python
    def est_gagnante(arbre):
        if arbre.gauche == None:
            return arbre.racine.nom_equipe
        else:
            return est_gagnante(arbre.gauche)
        
    ```

11. On obtient l'arbre suivant:

    ![](../images/arbre2.png){: .center width=480} 


12. 

    ```python
    def rechercher(arbre, equipe):
        if arbre.racine == equipe:
            return True
        elif convert(equipe.temps_etape) < convert(arbre.racine.temps_etape):
            if arbre.gauche == None:
                return False
            else:
                return rechercher(arbre.gauche, equipe)
        else:
            if arbre.droit == None:
                return False
            else:
                return rechercher(arbre.droit, equipe)
    ```

## Exercice 3


9. 

    ```sql
    SELECT titre_parution FROM parution;
    ```

10. On obtient le numéro de parution et le numéro des pages qui ont police Arial, 12 et classés par ordre de numéro de parution.

11. 

    ```sql
    SELECT num_image, titre_image, poids
    FROM image
    WHERE poids >= 1000;
    ```

12. 

    ```sql
    SELECT num_parution
    FROM parution
    JOIN page ON parution.num_parution = page.num_parution
    JOIN comporte_image ON page.id_page = comporte_page.id_page
    JOIN image ON comporte_image.num_image = image.num_image
    WHERE image.titre_image LIKE "%Apollo%";
    ```

13. 

    ```sql
    INSERT INTO image
    VALUES (2923, "Volcans du massif central", '', 400, 400, 1430);
    ```

14. La requête supprime de la table **texte** le texte ayant pour numéro 2034. La contrainte de référence pourrait être enfreinte, on ne peut pas supprimer une valeur d'une clé primaire d'une autre table.



