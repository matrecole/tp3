import random
import time
import os

hp = 20
nbr_combat = 0
nbr_victoires = 0
nbr_defaites = 0
nbr_adversaire = 0
nombre_victoires_consecutives = 0

################

def combat(enemy_hp):

    nbr_combat += 1

    lance_de = random.randint(1,6)

    print("Vous lancez un dé...")
    print(f"Le dé est tombé sur {lance_de}.")

    if lance_de <= enemy_hp:
        print("Vous perdez le combat..")
        return 0

    else:
        print("Vous gagnez le combat!")
        hp += force_adversaire
        nbr_victoires += 1
        return 1


################


while hp > 0:
    nbr_adversaire += 1

    force_adversaire = random.randint(1,5)

    print(f"Adversaire: {nbr_adversaire}\n"
          f"Vie de l'adversaire : {force_adversaire}\n"
          f"Vie du joueur : {hp}\n"
          f"Combat {nbr_combat} : {nbr_victoires} vs {nbr_defaites}")

    print(f"Vous ouvrez une porte et tombez face à face avec un adversaire de difficulté : {force_adversaire}.")

    choix = int(input("Que voulez-vous faire ?\n" 
        "1- Combattre cet adversaire\n"
        "2- Contourner cet adversaire et aller ouvrir une autre porte\n"
        "3- Afficher les règles du jeu\n"
        "4- Quitter la partie\n"))
    

    ################

    if choix == 1:
        cmbt = combat(force_adversaire)

        if cmbt == 0:
            print(f"Votre niveau de vie est maintenant à {hp}")

        elif cmbt == 1:
            print(f"Vous avez maintenant {nombre_victoires_consecutives} victoires consécutives!")
            print(f"Votre niveau de vie est maintenant à {hp}")

    ################

    elif choix == 2:
        hp -= 1
        print("Vous contournez l'adversaire mais il arrive a vous toucher et vous perdez 1 point de vie.")

    ################
        
    elif choix == 3:
        print("Voici les règles du jeu:\n")
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire."
        "Une défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire.  Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire."
        "La partie se termine lorsque les points de vie de l'usager tombent sous 0."
        "L'usager peut combattre ou éviter chaque adversaire, dans le cas de l'évitement, il y a une pénalité de 1 point de vie.")
        time.sleep(10)

    ################
        
    elif choix == 4:
        print("Merci et au revoir...")
        hp = 0
        time.sleep(3)

    ################
        
    os.system("cls")
