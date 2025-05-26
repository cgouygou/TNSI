# Corrigé du bac blanc n°2

▶ **Sujet Centres étrangers 2024 (J2)** (à télécharger avec le corrigé [ici](https://pixees.fr/informatiquelycee/term/#suj_bac){:target="_blank"}).


!!! warning "Coquilles dans le corrigé"
    - **Exercice 1, Partie A, question 2:** $a=4$ et $b=7$.
    - **Exercice 3, Partie B, question 13:** ```JOIN personnel ON agres.idchefagres = personnel.matricule```


!!! info "Variante fin exercice 2"

    **Question 13**

    À mon humble avis, la version itérative de la méthode `#!py contient` est un peu compliquée.

    J'aurais plutôt vu une version récursive dont l'idée est :
    
    - soit le dossier courant est celui cherché et on renvoie `#!py True`;
    - soit on recherche récursivement dans les dossiers «fils» (mais attention, on ne sait pas combien de sous-dossiers il y a);
    - on renvoie `#!py False` si après parcours le dossier n'est pas trouvé.

    ```python linenums='1'
    def contient(self, nom_dossier):
        if self.nom == nom_dossier:
            return True
        trouve = False
        for f in self.fils:
            trouve = trouve or f.contient(nom_dossier)
        return trouve
    ```
    
    **Question 14**

    Mais ça se complique peut-être ici...

    1. Pour chaque fils (sous-dossier) du dossier:
    
        - si le nom du fils est celui cherché, on renvoie le nom du dossier
        - sinon on récupère la réponse récursivement dans le dossier fils:
            - s'il y en a une, on la renvoie

    2. On renvoie `#!py None`  si aucun parent n'a été trouvé

    ```python linenums='1'
    def parent(self, nom_dossier):
        for fils in self.fils:
            if fils.nom == nom_dossier:
                return self.nom
            else:
                p = fils.parent(nom_dossier)
                if p:
                    return p
        return None
    ```
    
