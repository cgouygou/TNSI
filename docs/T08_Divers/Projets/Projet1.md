# Projet 1

## Sujet 1 : Life & Death

!!! example "Énoncé"
    On considère une grille - théoriquement infinie - dont les cases appellées *cellules* peuvent prendre deux états distincts : «vivante» ou «morte».

    Une cellule possède huit voisins : les cellules adjacentes horizontalement, verticalement et diagonalement.

    À chaque génération, les cellules peuvent changer d'état ou conserver leur état selon les règles suivantes:

    - si une cellule **morte** possède *exactement* 3 cellules voisines vivantes, alors elle devient **vivante** (elle naît);
    - si une cellule **vivante** possède 2 ou 3 cellules vivantes, alors elle reste vivante, **sinon elle meurt**.

    L'objectif est de simuler, génération après génération, l'état de la grille.

    **Exemple:**

    === "1"
        ![](../images/jv1.png){: .center} 
    === "2"
        ![](../images/jv2.png){: .center}
    === "3"
        ![](../images/jv3.png){: .center}
    === "4"
        ![](../images/jv4.png){: .center} 
    === "5"
        ![](../images/jv5.png){: .center}
    === "6"
        ![](../images/jv6.png){: .center}
    === "7"
        ![](../images/jv7.png){: .center} 
    === "8"
        ![](../images/jv8.png){: .center}
    === "9"
        ![](../images/jv9.png){: .center}
    === "10"
        ![](../images/jv10.png){: .center} 
    === "11"
        ![](../images/jv11.png){: .center}
    === "12"
        ![](../images/jv12.png){: .center}



!!! abstract "Consignes"
    - Utiliser le module `pygame` pour animer la grille génération après génération.
    - L'état initial de la grille sera choisi aléatoirement.
    - Le programme principal devra contenir deux classes: `Grille` et `Cellule`.
    - La classe `Grille` contiendra une méthode `actualisation` (ou `update`) qui consistera à actualiser l'état de la grille (c'est à dire de chacune de ses cellules) ainsi qu'à afficher la grille.

        La boucle des événements sera donc réduite à (avec par exemple `G` instance de la classe `Grille`):
        ```python linenums='1'
        continuer = True
        while continuer:
            for evenement in pygame.event.get(): 
                if evenement.type == QUIT:
                    continuer = False

            G.actualisation()
            pygame.display.flip()
            pygame.time.delay(100)
        ```
        

## Sujet 2: Promenade d'une puce

!!! example "Énoncé"
    Une puce se promène sur une grille dont les cases appellées *cellules* peuvent être blanches ou noires. Au départ, toutes les cellules sont blanches et la puce se trouve au centre de la grille.

    La puce peut se déplacer horizontalement ou verticalement sur la grille de la façon suivante:

    - si la puce se situe sur une cellule blanche, elle tourne de 90° vers la droite, change la couleur de la case en noir et avance d'une case.
    - si la puce se situe sur une cellule noire, elle tourne de 90° vers la gauche, change la couleur de la case en blanc et avance d'une case.

    ![](../images/jv28.png){: .center} 

!!! abstract "Consignes"
    - Utiliser le module `pygame` pour animer la grille génération après génération.
    - Le programme principal devra contenir deux classes: `Grille` et `Puce`.
    - La classe `Grille` contiendra une méthode `actualisation` (ou `update`) qui consistera à actualiser l'état de la grille (c'est à dire de la cellule où la puce est passée) ainsi qu'à afficher la grille.

        La boucle des événements sera donc réduite à (avec par exemple `G` instance de la classe `Grille`):
        ```python linenums='1'
        continuer = True
        while continuer:
            for evenement in pygame.event.get(): 
                if evenement.type == QUIT:
                    continuer = False

            G.actualisation()
            pygame.display.flip()

        ```