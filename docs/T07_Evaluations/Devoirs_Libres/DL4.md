# DL 0101: files d'attente

Pour rappel, l'énoncé est [ici (ex 7)](https://cgouygou.github.io/TNSI/T01_StructuresDonnees/T1.2_FifoLifo/T1.2_FifoLifo/#124-exercices){:target='_blank'}

!!! check "Proposition de correction"
    Il est nécessaire d'avoir une classe `#!py File` dans un fichier nommé `TAD.py`.

    ```python
    import random
    from TAD import File


    ################## Simulation avec une seule file d'attente ####################

    def simul_file_unique(nb_guichets, temps_attente_max, N):
        dispo = nb_guichets * [0]
        cumul_temps_attente = 0
        file = File()
        nb_clients_servis = 0
        for arrivant in range(1, N + 1):
            file.enfiler(arrivant)
            for k in range(nb_guichets):
                if dispo[k] == 0:
                    if not file.est_vide():
                        sortant = file.defiler()
                        cumul_temps_attente += arrivant - sortant
                        dispo[k] = random.randint(1, temps_attente_max)
                        nb_clients_servis += 1
                else:
                    dispo[k] -= 1
        return cumul_temps_attente / nb_clients_servis


    ###### Simulation avec une file d'attente par guichet, et choix aléatoire ######

    def simul_alea(nb_guichets, temps_attente_max, N):
        dispo = nb_guichets * [0]
        cumul_temps_attente = 0
        files = [File() for _ in range(nb_guichets)]
        nb_clients_servis = 0

        for arrivant in range(1, N + 1):
            guichet = random.randint(1, nb_guichets)
            files[guichet-1].enfiler(arrivant)
            for k in range(nb_guichets):
                if dispo[k] == 0:
                    if not files[k].est_vide():
                        sortant = files[k].defiler()
                        cumul_temps_attente += arrivant - sortant
                        dispo[k] = random.randint(1, temps_attente_max)
                        nb_clients_servis += 1
                else:
                    dispo[k] -= 1
        return cumul_temps_attente / nb_clients_servis

    ####### Simulation avec une file d'attente par guichet et choix glouton ########

    def simul_glouton(nb_guichets, temps_attente_max, N):
        cumul_temps_attente = 0
        files = [File() for _ in range(nb_guichets)]
        taille_files = [0 for _ in range(nb_guichets)]
        nb_clients_servis =0

        for arrivant in range(1, N + 1):
            i = taille_files.index(min(taille_files))
            files[i].enfiler(arrivant)
            taille_files[i] += 1
            for k in range(nb_guichets):
                if dispo[k] == 0:
                    if not files[k].est_vide():
                        sortant = files[k].defiler()
                        taille_files[k] -= 1
                        cumul_temps_attente += arrivant - sortant
                        dispo[k] = random.randint(1, temps_attente_max)
                        nb_clients_servis += 1
                else:
                    dispo[k] -= 1
        return cumul_temps_attente / nb_clients_servis

    ## Lancement et affichage des simulations

    nb_simul = 10000
    tps_max = 5
    nb_g = 5

    print(f"Temps d'attente moyen avec une seule file : {simul_file_unique(nb_g, tps_max, nb_simul)}")
    print(f"Temps d'attente moyen avec une file par guichet (aléatoire): {simul_alea(nb_g, tps_max, nb_simul)}")
    print(f"Temps d'attente moyen avec une file par guichet (glouton): {simul_glouton(nb_g, tps_max, nb_simul)}")
    ```