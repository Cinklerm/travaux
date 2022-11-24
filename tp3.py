import arcade
from random import random

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Martin Cinkler TP3"
STATUS_VICTOIRE = "victoire"
STATUS_DEFAITE = "defaite"
NOMBRE_DE_DES = 2
#variables
force_adversaire = 0
numero_adversaire = 0
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
combat_status = STATUS_VICTOIRE

# la classe qui implemente le game loop
class Combat(arcade.Window):
    """Main welcome window
    """
    def __init__(self):
        """Initialize the window
        """

        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background window
        arcade.set_background_color(arcade.color.WHITE)
#imprime les informations du jeu
    def imprimer_statut():
        """ imprime les informations du jeu
        """
        global numero_adversaire,force_adversaire, niveau_vie,numero_combat
        print(f"Adversaire : {numero_adversaire}")
        print(f"Force de l’adversaire : {force_adversaire}")
        print(f"Niveau de vie de l’usager : {niveau_vie}")
        print(f"Combat {numero_combat} : {nombre_victoires} vs {nombre_defaites}")  

    def on_draw(self):
        """Called whenever you need to draw your window
        """
        arcade.start_render()
  
    def contourner():
        """ On saute cette adeversaire et on passe au suivant
        """
        global niveau_vie,force_adversaire
        #On diminue les points de vie quand on contourne un adversaire
        niveau_vie = niveau_vie - 1
        # On force la creation d'un nouvelle adversaire
        force_adversaire = 0

    #On imprime le menu
    def menu():
        print()
        print("Que voulez-vous faire ? ")
        print(" 1- Combattre cet adversaire")
        print(" 2- Contourner cet adversaire et aller ouvrir une autre porte")
        print(" 3- Afficher les règles du jeu")
        print(" 4- Quitter la partie")
    
    # On quitte le programme
    def quitter():
        print ("merci et au revoir")
        quit()

    # On cree un adversaire et  on definit sa force
    def creer_monstre():
        """ On cree un adversaire et  on definit sa force.
        Chaque 3me est un boss
        """
        global force_adversaire,numero_adversaire
        if numero_adversaire>0 and numero_adversaire % 3 == 0:
            print("Vous avez tombe sur un boss")
            force_adversaire = (3 + int( random() * 5 * NOMBRE_DE_DES) )
        else:
            force_adversaire = (1 + int( random() * 5 * NOMBRE_DE_DES) )

        numero_adversaire = numero_adversaire + 1 
        print ("Vous tombez face à face avec un adversaire de difficulté " + str(force_adversaire))
        Combat.menu()

    # On montre les regles aux joueurs
    def regles():
        print ("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print ("Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print ()
        print ("La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
        print ()
        print ("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

        
    def combattre():
        global force_adversaire,niveau_vie,nombre_victoires,nombre_defaites,combat_status
        global nombre_victoires_consecutives,numero_combat 
        Combat.imprimer_statut()
        # On calcule le score
        score_de = (1 + int(random() * 6)) * NOMBRE_DE_DES
        print(f"Lancer du dé : {score_de}")
        numero_combat = numero_combat + 1
        # Si c'est une victoire on augmente le nombre de victoire consecutive et le niveau de vie
        if (score_de > force_adversaire):
            if (combat_status == STATUS_VICTOIRE):
                nombre_victoires_consecutives = nombre_victoires_consecutives + 1
            combat_status = STATUS_VICTOIRE
            nombre_victoires = nombre_victoires + 1
            niveau_vie=niveau_vie + force_adversaire
            # On demande de creer le prochin adversaire
            force_adversaire = 0
            print("Victoire!")
            print(f"Niveau de vie : {niveau_vie}")
            print("Nombre de victoires consécutives")
            print( nombre_victoires_consecutives)
        # si c'est une defaite on diminue le nombre de vie et on augmente le nombre de defaie
        else:
            nombre_victoires_consecutives = 0
            combat_status = STATUS_DEFAITE
            niveau_vie = niveau_vie - force_adversaire
            force_adversaire = 0
            nombre_defaites = nombre_defaites + 1
            print("Defaite")
            print(f"Niveau de vie : {niveau_vie}")

        #On definit quelle touche va corespondre a quelle action 
    def on_key_press(self, symbol: int, modifiers: int):
        touche = chr(symbol)
        if (touche == "1"):
            Combat.combattre()
        if (touche == "2"):
            Combat.contourner()
        if (touche == "3"):
            Combat.regles()
        if (touche == "4"):
            Combat.quitter()
        return super().on_key_press(symbol, modifiers)
    #Les conditions pour que la partie ce termine
    def on_update(self, delta_time: float):
        global force_adversaire,niveau_vie,nombre_victoires,nombre_defaites
        if (niveau_vie <= 0):
            print (f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
            nombre_victoires = 0
            nombre_defaites = 0
            niveau_vie = 20
        if  (force_adversaire == 0):
            Combat.creer_monstre()
        return super().on_update(delta_time)


# Main code entry point
if __name__ == "__main__":
    app = Combat()
    arcade.run()
