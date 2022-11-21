# Exercices interactifs

{{ initexo(0) }}

!!! example "{{ exercice() }}"
    === "Énoncé" 
        *Questions interactives à réaliser sur le site sqlzoo.net.*

        1. Travail sur SELECT, (base de données Nobel) : [ici](https://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial){. target="_blank"}.

        2. Travail sur SUM et COUNT, (base de données World) : [ici](https://sqlzoo.net/wiki/SUM_and_COUNT){. target="_blank"}. (jusqu'à la question 5.)

        3. Travail sur JOIN, (base de données Euro2012) : [ici](https://sqlzoo.net/wiki/The_JOIN_operation){. target="_blank"}.

    === "Correction" 
        {{ correction(False, 
        "
        "
        ) }}


!!! example "{{ exercice() }}"
    Gestion d'un réseau d'agences de location de voitures.   
    *D'après le travail de J. Le Coupanec (Académie de Rennes)*

    La base de données [locations.db](../data/locations.db) contient les tables ```Agences```,```Locations```, ```Vehicules```.
    ![](../images/diag_locations.png)

    1. Répondez aux [9 questions](https://colbert.bzh/sql/tp.html?html=locations_1&db=locations){. target="_blank"} sur la relation Agence. (Travail sur SELECT)
    2. Répondez aux [11 questions](https://colbert.bzh/sql/tp.html?html=locations_2&db=locations){. target="_blank"} sur la relation Véhicules. (Travail sur SELECT plus des fonctions d'agrégation)
    3. Répondez aux [12 questions](https://colbert.bzh/sql/tp.html?html=locations_3&db=locations){. target="_blank"} sur la relation Locations. (Travail sur des jointures)
    4. Répondez aux [17 questions](https://colbert.bzh/sql/tp.html?html=locations_4&db=locations){. target="_blank"} sur la relation Véhicules. (Travail sur UPDATE, INSERT, DELETE)

    

!!! example "{{ exercice() }} : The SQL Murder Mystery "
    === "Énoncé" 
        Cet exercice en ligne est proposé par le Knight Lab de l'université américaine Northwerstern University.


        ![](../images/sql_murder_mystery.png){: .center width=50%}

        **Le point de départ de l'histoire** : un meurtre a été commis dans la ville de SQL City le 15 janvier 2018.

        À partir de ce point de départ et d'une base de données dont le diagramme est donné ci-dessous, il s'agit de trouver le meurtrier.

        ![](../images/schemaMM.png){: .center width=100%}

        Rendez-vous sur [cette page](https://mystery.knightlab.com/walkthrough.html){:target="_blank"}, et bonne enquête à coups de requêtes !

        Vous pouvez travailler en ligne ou bien dans votre SGBD préféré, avec la base [sql-murder-mystery.db](../data/sql-murder-mystery.db). Attention pour valider votre réponse, il faudra vous rendre en bas de la page officielle.



    === "Correction" 
        {{ correction(False, 
        "
        "
        ) }}