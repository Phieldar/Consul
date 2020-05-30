import random
from tkinter import *


#window = Tk()
#window.title("Le Doge")
#window.geometry("640x360")
#window.mainloop()


class Cite:

    def __init__(self, name, population, factions, wealth, order, defence, strength, diplomacy):
        self.name = name
        self.population = population
        self.factions = factions
        self.wealth = wealth
        self.order = order
        self.defence = defence
        self.strength = strength
        self.diplomacy = diplomacy

    def get_name(self):
        return self.name

    def get_order(self):
        return self.order

    def get_wealth(self):
        return self.wealth

    def description_cite(self):
        print("La cité de" + str(self.name) + " est sympa.")


class Player:

    def __init__(self, name, health, wealth, influence, virtues, vices, traits):
        self.name = name
        self.health = health
        self.wealth = wealth
        self.influence = influence
        self.virtues = virtues
        self.vices = vices
        self.traits = traits
        print("Bienvenue au nouveau consul " + str(self.name) + ". " + "Tu as " + str(self.wealth) + " de richesse.")

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_wealth(self):
        return self.wealth

    def get_influence(self):
        return self.influence

    def augmenter_influence(self, quantite):
        self.influence = self.influence + quantite
        return self.influence

    def decision_player(self):
        decision_joueur = True
        while decision_joueur == True:
            print ((str(self.name)+ " doit faire un choix. \n1) Lire \n2) organiser une journée de marché. "))
            print("3) détourner des richesses.")
            print("4) explorer la cite")
            print("5) Quitter le jeu")
            choix = int(input("Quel est votre choix?"))
            if choix is not int:
                print (str(self.name) + " doit y avoir un choix.")
            if choix == 1:
                print ("Le Consul lit. Il augmente son influence. Celle-ci était de :" + str(self.influence))
                self.augmenter_influence(2)
                print ("Elle est maintenant de :" + str(self.influence))
                decision_joueur = False
            if choix == 2:
                decision_joueur = False
            if choix == 3:
                decision_joueur = False
            if choix == 4:
                cite_joueur.description_cite()
                decision_joueur = False
            if choix == 5:
                decision_joueur = False
            else:
                decision_joueur = False

        return self


class Factions:

    def __init__(self, nom, effectifs, richesse, force, cohesion):
        self.nom = nom
        self.effectifs = effectifs
        self.richesse = richesse
        self.force = force
        self.cohesion = cohesion


# Création de la cité
liste_nom_cite = ["Laval", "Mordor", "Candiac", "Laval", "Londres", "Arcadia"]

nom_cite = random.sample(liste_nom_cite, k=1)
population_cite = random.randint(500,1000)
factions_cite = {
          "noblesse": Factions("noblesse", 100, 100, 100, 5),        # effectifs, richesse, force
          "clerge": Factions("clerge", 30, 30, 300, 5),
          "marchand": Factions("marchand", 50, 150, 50, 5),
          "plebe": Factions("plebe", 500, 2, 500, 5)
          }
richesse_cite = random.randint(2,10)
ordre_cite = random.randint(2,10)
defence_city = random.randint(2,10)
cite_strenght = random.randint(2,10)
diplomacy_cite = []

cite_joueur = Cite(nom_cite, population_cite, factions_cite, richesse_cite, ordre_cite, defence_city,cite_strenght , diplomacy_cite)

## Création joueur 1
richesse_joueur = random.randint(1,5)

joueur_nom = str(input("Quel est le nom du nouveau consul élu dans la cité de " + str(cite_joueur.get_name()) + "!"))
player1 = Player(joueur_nom, 10, richesse_joueur, 5, ["Courage", "Humilité"], ["Avarice"], ["Grand"])

#### Structure du jeu #####

fin_du_jeu = False
tour = 1

while fin_du_jeu == False:
    print("##### " + str(tour) + " #####")
    player1.decision_player()
    #Player.decision_player(player1)
    print("Fin!")
    tour += 1
    if tour == 5:
        fin_du_jeu = True
