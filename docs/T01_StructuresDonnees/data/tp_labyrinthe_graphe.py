import pygame
import random
from pygame.locals import *

################################################################################
###                                 Classes                                  ###
################################################################################

class Graphe:
    def __init__(self, liste_sommets):
        self.adj = {sommet: [] for sommet in liste_sommets}
    
    def sommets(self):
        return [key for key in self.adj]
    
    def ordre(self):
        return len(self.sommets())
    
    def voisins(self, sommet):
        '''
        renvoie la liste des voisins de sommet
        '''
        return self.adj[sommet]
    
    def est_voisin(self, s1, s2):
        '''
        verifie si s2 est un voisin de s1
        '''
        return s2 in self.voisins(s1)
    
    def ajoute_sommet(self, sommet):
        '''
        ajoute le sommet au graphe
        '''
        if sommet not in self.adj:
            self.adj[sommet] = []
        
    def ajoute_arete(self, s1, s2):
        '''
        ajoute une arête entre les sommets s1 et s2 dans le graphe, en les créant
        au préalable.
        '''
        self.ajoute_sommet(s1)
        self.ajoute_sommet(s2)
        if not self.est_voisin(s1, s2):
            self.adj[s1].append(s2)
        if not self.est_voisin(s2, s1):
            self.adj[s2].append(s1)


class Cellule:
    def __init__(self, mur_nord, mur_est, mur_sud, mur_ouest):
        self.murs = {'N':mur_nord, 'E':mur_est, 'S':mur_sud, 'O':mur_ouest}

class Labyrinthe:
    def __init__(self, hauteur, largeur):
        self.grille = self.construire_grille(hauteur, largeur)

    def construire_grille(self, h, l):
        grille = [[Cellule(True, True, True, True) for j in range(l)] for i in range(h)]
        return grille
    
    def afficher(self, c):
        '''
        affiche le labyrinthe, avec c qui désigne la longueur du côté d'une cellule
        '''
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                if self.grille[i][j].murs['S']:
                    pygame.draw.line(screen, [0, 0, 0], [j*c, (i+1)*c], [(j+1)*c, (i+1)*c], 2)
                if self.grille[i][j].murs['N']:
                    pygame.draw.line(screen, [0, 0, 0], [j*c, i*c], [(j+1)*c, i*c], 2)
                if self.grille[i][j].murs['E']:
                    pygame.draw.line(screen, [0, 0, 0], [(j+1)*c, i*c], [(j+1)*c, (i+1)*c], 2)
                if self.grille[i][j].murs['O']:
                    pygame.draw.line(screen, [0, 0, 0], [j*c, i*c], [j*c, (i+1)*c], 2)


    def creer_passage(self, i1, j1, i2, j2):
        '''
        crée une ouverture entre les cellules d'adresses (i1, j1) et (i2, j2)
        '''
        if i1 == i2 : #ouverture horizontale
            if j1 < j2:
                self.grille[i1][j1].murs['E'] = False
                self.grille[i2][j2].murs['O'] = False
            else:
                self.grille[i1][j1].murs['O'] = False
                self.grille[i2][j2].murs['E'] = False
        else:
            if i1 < i2:
                self.grille[i1][j1].murs['S'] = False
                self.grille[i2][j2].murs['N'] = False
            else:
                self.grille[i1][j1].murs['N'] = False
                self.grille[i2][j2].murs['S'] = False
                
    def creer_labyrinthe(self, i, j, di, dj):
        '''
        générère un labyrinthe de dimension (di, dj) à partir de la case (i, j) en haut à gauche.
        '''
        if di == 1:
            for k in range(j, j+dj-1):
                self.creer_passage(i, k, i, k+1)
        elif dj == 1:
            for k in range(i, i+di-1):
                self.creer_passage(k, j, k+1, j)
        else:
            if di >= dj:
                c = random.randint(1, di-1)
                self.creer_labyrinthe(i, j, c, dj)
                self.creer_labyrinthe(i+c, j, di-c, dj)
                r = random.randint(0, dj-1)
                self.creer_passage(i+c-1, j+r, i+c, j+r)
            else:
                c = random.randint(1, dj-1)
                self.creer_labyrinthe(i, j, di, c)
                self.creer_labyrinthe(i, j+c, di, dj-c)
                r = random.randint(0, di-1)
                self.creer_passage(i+r, j+c-1, i+r, j+c)

################################################################################
###                                Fonctions                                 ###
################################################################################



def affiche_chemin(chemin:list, cote:int):
    '''
    Dessine dans la fenetre Pygame screen des carrés de coté taille avec comme
    couleur:
    - du vert si le sommet est la source
    - du rouge si le sommet est la cible
    - du bleu sinon.
    
    Le paramètre chemin est une liste de tuples correspondant aux adresses
    (ligne, colonne) des cellules dans la grille du labyrinthe.
    '''
    source = chemin[...]
    cible = chemin[...]
    for cellule in chemin:
        x =
        y = 
        if cellule == source:
            pygame.draw.rect(screen, ..., ...)
        ...


################################################################################
###                                Constantes                                ###
################################################################################

hauteur_laby, largeur_laby, cote_cellule = 50, 100, 10
taille_ecran = (largeur_laby*cote_cellule, hauteur_laby*cote_cellule)

laby = Labyrinthe(hauteur_laby, largeur_laby)
laby.creer_labyrinthe(0, 0, hauteur_laby, largeur_laby)

depart, arrivee = 

################################################################################
###                                 Graphe                                   ###
################################################################################

g = Graphe([])

for i in range(hauteur_laby):
    for j in range(largeur_laby):
        if not laby.grille[i][j].murs['N']:
            g.ajoute_arete((i, j), (i-1, j))
        ...
                
chemin = 

################################################################################
###                                 Pygame                                   ###
################################################################################

pygame.init()

screen = pygame.display.set_mode(taille_ecran)
screen.fill([255, 255, 255])
pygame.display.set_caption("Chemin dans un labyrinthe")


affiche_chemin()
laby.afficher(cote_cellule)

continuer = True
while continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    pygame.display.flip()

pygame.quit()
