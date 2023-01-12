# ABR, POO et méthode infixe

Tout d'abord merci de prendre le temps de lire ceci.


## Prequel

Je suis en train de terminer - pour la première année d'enseignement de NSI en Terminale - le chapitre sur les arbres, notamment les ABR ce matin[^1].

[^1]: jeudi 12 janvier 2023.

À propos de la représentation des arbres binaires à l'aide de classes, j'ai déjà longuement hésité entre plusieurs façons de faire, vues dans la littérature, au DIU, etc:

- deux classes `Noeud` et `Arbre`;
- une seule classe `Noeud`;
- une seule classe `Arbre`.

J'ai finalement opté pour cette dernière option, après avoir lu [ce billet](https://sebhoa.gitlab.io/iremi/03_Didactique/arbres/){:target="_blank"}.

J'obtiens donc l'implémentation suivante[^2] pour les ABR, dans laquelle je décide d'intégrer les différents algos au programme en tant que méthodes et non fonctions hors de la classe[^3]:

[^2]: Vous pouvez déjà critiquer ce choix...
[^3]: ça aussi...

```python linenums='1'
class ABR:
    def __init__(self, cle=None):
        self.cle = cle
        if self.cle is not None:
            self.gauche = ABR()
            self.droit = ABR()

    def est_vide(self):
        return self.cle is None
    
    def infixe(self):
        if not self.est_vide():
            self.gauche.infixe()
            print(self.cle)
            self.droit.infixe()
            
    def inserer_cle(self, cle):
        if self.est_vide():
            self.cle = cle
            self.gauche = ABR()
            self.droit = ABR()
        elif cle < self.cle:
            self.gauche.inserer_cle(cle)
        else:
            self.droit.inserer_cle(cle)

    def inserer_cles(self, liste_cles):
        for cle in liste_cles:
            self.inserer_cle(cle)

    def affiche(self, indent = 0):
        s = ' '*2*indent + '|_' + str(self.cle) + '\n'
        if not self.gauche.est_vide():
            s += self.gauche.affiche(indent + 1)
        if self.gauche.est_vide() and not self.droit.est_vide():
            s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'     

        if not self.droit.est_vide():
            s += self.droit.affiche(indent + 1)
        if self.droit.est_vide() and not self.gauche.est_vide():
            s += ' '*(2*indent+2) + '|' + '_' + 'None' + '\n'  
        return s

    def __repr__(self):
        return self.affiche(0)

# ABR exemple    
a = ABR()
a.inserer_cles([5, 4, 2, 7])
```

## S01E01

J'en arrive alors à un exercice où je demande aux élèves d'écrire une méthode (ou fonction, comme ils veulent) qui permet de déterminer si un arbre binaire donné est un ABR ou non. Je les laisse libre de la méthode et plusieurs décident de vérifier que le résultat du parcours infixe est trié dans l'ordre croissant, suite à la remarque précédente du cours (que vous trouverez habilement sur ce site).

Bien entendu (?), pour illustrer le parcours préfixe, j'avais opté pour un traitement de la racine réduit à un affichage[^4].

[^4]: heureusement que Laurent Chéno a pris sa retraite et ne lira jamais ce billet.

Se pose donc la question d'adapter la méthode `infixe` pour qu'elle retourne une liste des nœuds visités dans l'ordre infixe.

!!! danger "Stupeur"
    Je m'aperçois avec effroi que je n'ai pas vraiment anticipé la méthode car il me semble que ce n'est pas très bon en terme de complexité, n'est-ce pas?

    J'essaie alors de réfléchir avec les neurones dont je dispose. D'habitude, lorsque je dois faire un DFS - plutôt sur un graphe -  je stocke dans *une variable globale* (je sais, je sais) les sommets/nœuds visités. Et je me dis qu'en POO à l'intérieur de la classe ça va être compliqué...

Des élèves proposent donc d'utiliser une liste en paramètre de la méthode et d'y ajouter successivement les clés des nœuds visités. On obtient alors cette modification de la méthode `infixe`:

```python linenums='1'
    def infixe(self, ordre=[]):
        if not self.est_vide():
            self.gauche.infixe(ordre)
            ordre.append(self.cle)
            self.droit.infixe(ordre)
        return ordre
```

Avant de tester, je me dis intérieurement que ça va pas... Il va y avoir une valeur renvoyée sur chaque sous-arbre vide... Mais bon pédagogiquement il faut leur montrer et leur expliquer pourquoi ensuite...

Verdict:

```python 
>>> a.infixe()
[2, 4, 5, 7]
```

!!! question "Question 1"
    Pourquoi ça marche ??? Où passent les multiples `return`???

    Parce qu'on est d'accord, si on `print` on a:

    ```python 
    >>> a.infixe()
    []
    [2]
    [2]
    [2, 4]
    [2, 4]
    [2, 4, 5]
    [2, 4, 5, 7]
    [2, 4, 5, 7]
    [2, 4, 5, 7]
    ```
    Pourquoi que le dernier `return`?

Je m'interroge devant mes élèves - qui se posent beaucoup moins de questions puisque «ça marche» - et leur dis que je vais réfléchir. Dont acte, mais en vain, d'où ce billet...

On passe à la suite.

## S01E02

Puisqu'on récupère l'ordre infixe, c'est parti on attaque la suite de la fonction/méthode. En cours d'implémentation, un de mes élèves m'interpelle car il ne comprend pas ce qu'il obtient. Moi non plus.

Sa fonction (non finalisée) mais il a testé ça avant de comparer les deux listes:
```python linenums='1'
def is_abr(arbre):
    return arbre.infixe(), sorted(arbre.infixe())
```

Son test:
```python
>>> is_abr(a)
([2, 4, 5, 7, 2, 4, 5, 7], [2, 2, 4, 4, 5, 5, 7, 7])
```

!!! question "Question 2"
    Mais pourquoi diantre les valeurs se retrouvent en double ??? Dans la méthode `infixe`, `ordre` est locale, non ??? 

    Je lui ai conseillé de stocker d'abord le résultat du parcours infixe dans une variable, il a tenté:

    ```python linenums='1'
    def is_abr(arbre):
        p = arbre.infixe()
        return p, sorted(arbre.infixe())
    ```

    Idem. 

    Bon moi je pensais plutôt à ça, qui fait le job:

    ```python linenums='1'
    def is_abr(arbre):
        p = arbre.infixe()
        return p, sorted(p)
    ```

Bon voilà c'est fini, c'est surtout la question 2 qui me chiffonne, je ne comprends pas du tout la gestion de la liste lors de deux appels de la méthode `infixe` successifs.

J'espère que je suis clair, et pas trop à côté de la plaque. Merci de ne pas déchirer mon DIU sinon.

En tout cas, merci d'avoir lu jusqu'ici...