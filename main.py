import random
import time
import os

hp = 20 # points de vie du joueur
nbr_combat = 0 # nombre de combats joue
nbr_victoires = 0 # nombre de combats gagnes
nbr_defaites = 0 # nombre de combats perdus
nbr_adversaire = 0 # nombre dadversaires rencontres 
nombre_victoires_consecutives = 0 

################

def combat(enemy_hp): # fonction pour le combat

    nbr_combat += 1 # ajoute 1 a chaque combat

    lance_de = random.randint(1,6) # lance un de de 1 a 6

    print("Vous lancez un dé...")
    print(f"Le dé est tombé sur {lance_de}.")

    if lance_de <= enemy_hp: # si le de tombe sur un nombre plus petit ou egal que la force de l'adversaire
        print("Vous perdez le combat..")
        hp -= enemy_hp
        return 0

    else: # si le nombre est plus grand que la force de l'adversaire
        print("Vous gagnez le combat!")
        hp += force_adversaire
        nbr_victoires += 1
        return 1


################


while hp > 0: # 
    nbr_adversaire += 1 # ajoute un adversaire au compteur

    force_adversaire = random.randint(1,5) # genere une force au hasard pour l'adversaire

    print(f"Adversaire: {nbr_adversaire}\n"
          f"Vie de l'adversaire : {force_adversaire}\n"
          f"Vie du joueur : {hp}\n"
          f"Combat {nbr_combat} : {nbr_victoires} vs {nbr_defaites}")  # affiche le status de la partie

    print(f"Vous ouvrez une porte et tombez face à face avec un adversaire de difficulté : {force_adversaire}.")

    choix = int(input("Que voulez-vous faire ?\n"  #choisir quoi faire
        "1- Combattre cet adversaire\n"
        "2- Contourner cet adversaire et aller ouvrir une autre porte\n"
        "3- Afficher les règles du jeu\n"
        "4- Quitter la partie\n"))          
    

    ################

    if choix == 1:
        cmbt = combat(force_adversaire) # utilise la fonction combat

        if cmbt == 0: # perdu
            print(f"Votre niveau de vie est maintenant à {hp}")

        elif cmbt == 1: # gagner
            print(f"Vous avez maintenant {nombre_victoires_consecutives} victoires consécutives!")
            print(f"Votre niveau de vie est maintenant à {hp}")

    ################

    elif choix == 2:
        hp -= 1
        print("Vous contournez l'adversaire mais il arrive a vous toucher et vous perdez 1 point de vie.")

    ################
        
    elif choix == 3:
        nbr_adversaire -= 1 # nous ne rencontrons pas d'adversaire de plus
        
        print("Voici les règles du jeu:\n")
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire."
        "Une défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire."
        "La partie se termine lorsque les points de vie de l'usager tombent sous 0."
        "L'usager peut combattre ou éviter chaque adversaire, dans le cas de l'évitement, il y a une pénalité de 1 point de vie.")
        time.sleep(10) # attendre 10 secondes pour donner assez de temps pour lire

    ################
        
    elif choix == 4:
        print("Merci et au revoir...")
        hp = 0 # la boucle s'arrete lorsque le joueur n'a plus de point de vie
        time.sleep(3)

    ################
        
    os.system("cls") #effacer le texte a chaque action pour rendre la console plus propre
