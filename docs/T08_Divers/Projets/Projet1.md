# Projet 1

## Le jeu de la vie de John Conway

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
    - Le programme principal devra contenir deux classes: `Cellule` et `Jeu`.
    - La classe `Jeu` devra contenur (entre autres):
        + un attribut `grille`: un tableau d'objets `Cellule`
        + une méthode `actualisation` (ou `update`) qui consistera à actualiser l'état de la grille (c'est à dire de chacune de ses cellules) ainsi qu'à afficher la grille.
    - L'état initial de la grille sera choisi aléatoirement.
    - Utiliser le module `pygame` pour animer la grille génération après génération.

    La boucle des événements sera donc réduite à (avec par exemple `j` instance de la classe `Jeu`):
    ```python linenums='1'
    continuer = True
    while continuer:
        for evenement in pygame.event.get(): 
            if evenement.type == QUIT:
                continuer = False

        j.actualisation()
        pygame.display.flip()
        pygame.time.delay(100)
    ```

!!! info "Grille d'évaluation"
    Sur ce projet, vous serez évalués sur la grille suivante:

    |Item |Contenu|Points|
    |-----|-------|:----:|
    |POO|Les classes sont correctement conçues et l'interface est cohérente et claire. L'utilisation de la POO est maîtrisée (utilisation de setters par ex.).|5|
    |Travail de groupe|Les tâches sont définies et réparties au sein du groupe|3|
    |Projet abouti|Le projet tourne sans erreur et répond aux consignes.|4|
    |Qualité du code|Code aéré, spécifié, lisible, noms de variables pertinents...|4|
    |Oral| Restitution orale|4|
    |Total||20|
    |Bonus|Code en :gb: |2|
    |Malus|Code récupéré sur le web (ChatGPT, forums, github, etc) |-50, Game Over|


!!! check "Proposition de correction"
    ```python linenums='1'
    # ============================
    # Jeu de la vie de John Conway
    # Cédric Gouygou
    # ============================
    
    
    # ============================
    #           Modules
    # ============================
    
    import pygame
    import random as rd
    
    # ============================
    #           Classes
    # ============================
    
    class Cellule():
        def __init__(self, t:int, l:int, c:int, e:int):
            self.s = t               # taille en pixels d'une cellule
            self.ligne = l           # adresse de la cellule dans la grille du jeu (ligne)
            self.colonne = c         # adresse de la cellule dans la grille du jeu (colonne)
            self.x = self.s * c      # abscisse du coin haut-gauche de la cellule pour affichage
            self.y = self.s * l      # ordonnée du coin haut-gauche de la cellule pour affichage
            self.etat = e            # état actuel de la cellule (0: morte, 1: vivante)
            self.etat_suivant = 0    # état de la cellule à la prochaine génération
            self.nb_voisins = 0      # nombre de voisins vivants
    
        def actualise_suivant(self):
            '''
            Détermine l'état de la cellule à la génération suivante en fonction
            de son nombre actuel de voisins.
            '''
            if (self.etat == 0 and self.nb_voisins == 3) or (self.etat == 1 and self.nb_voisins in {2, 3}):
                self.etat_suivant = 1
            else:
                self.etat_suivant = 0
    
        def actualise_cellule(self):
            '''
            Actualise l'état de la cellule au passage  àla génération suivante.
            '''
            self.etat = self.etat_suivant
    
        def affiche_cellule(self, ecran):
            '''
            Représente graphiqement la cellule par un carré, aux coordonnées (self.x, self.y) et
            de taille self.s
            '''
            if self.etat:
                pygame.draw.rect(ecran, (0, 0, 0), (self.x, self.y, self.s, self.s))
            else:
                pygame.draw.rect(ecran, (255, 255, 255), (self.x, self.y, self.s, self.s))
    
    
    class Jeu():
        def __init__(self, l:int, h:int, t:int, e:int):
            self.longueur = l          # longueur de la grille(en nombre de cellules)
            self.hauteur = h           # hauteur de la grille
            self.taille_cellule = t    # taille d'une cellule (en pixels)
            self.ecran = e             # ecran Pygame d'affichage
            # ci-dessous, grille de cellules (list de list d'objets de classe Cell)
            self.cellules = [[Cellule(self.taille_cellule, r, c, rd.randint(0, 1)) for c in range(self.longueur)] for r in range(self.hauteur)]
    
        def actualisation(self):
            '''
            Effectue deux parcours de la grille.
            Premier parcours:
            - Détermine le nombre de voisins vivants autour de chaque cellule
            - Détermine l'état des cellules à la génération suivante en fonction du nombre de
            voisins
            Deuxième parcours:
            - actualise l'état des cellules
            - affiche les cellules
            '''
            for r in range(self.hauteur):
                for c in range(self.longueur):
                    self.cellules[r][c].nb_voisins = self.compte_voisins(r, c)
                    self.cellules[r][c].actualise_suivant()
            for r in range(self.hauteur):
                for c in range(self.longueur):
                    self.cellules[r][c].actualise_cellule()
                    self.cellules[r][c].affiche_cellule(self.ecran)
    
        def compte_voisins(self, ligne:int, colonne:int) -> int:
            '''
            Détermine le nombre de voisins vivants autour d'une cellule.
            Les deplacements (variable d) sont relatifs par rapport à l'adresse (ligne, colonne)
            de la cellule.
            '''
            n = 0
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                try:
                    n += self.cellules[ligne + d[0]][colonne + d[1]].etat
                except:
                    pass
            return n
    
    # ============================
    #       Initialisation
    # ============================
    
    ## Lancement de Pygame
    pygame.init()
    
    
    ## Constantes
    longueur_grille, hauteur_grille = 640, 480
    taille_cellule = 20
    taille = (longueur_grille, hauteur_grille)
    
    
    ## Écran
    fenetre = pygame.display.set_mode(taille)
    pygame.display.set_caption("Jeu de la vie de John Conway")
    
    
    ## Instanciation du jeu
    j = Jeu(longueur_grille // taille_cellule , hauteur_grille // taille_cellule, taille_cellule, fenetre)
    
    # ============================
    #         Main
    # ============================
    
    continuer = False
    while not continuer:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                continuer = True
    
        j.actualisation()
        pygame.display.flip()
        pygame.time.delay(100)
        
    ## Fermeture de la fenêtre Pygame
    pygame.quit()



    ```
<!-- 
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

        ``` -->
