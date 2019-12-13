"""Gestion des actions"""

import datetime

class Action:

    """définition de l'objet action avec nom et code"""

    def __init__(self, nom: str, spot):
        """définition des attributs """
        self.nom = nom
        self.spot = spot
        self.cours = {datetime.datetime.now(): self.spot}


    def __str__(self):
        """str(self)"""
        return self.nom

    def ajout_cours(self, spot):
        self.cours[datetime.datetime.now()] = spot
    def hight(self, date):
        pass


if __name__ == "__main__":
    BNPP = Action('BNPP', 30)
    SG = Action('BNPP',  36.5)
    BNPP.ajout_cours( 50.9)
    SG.ajout_cours( 38.5)
    print(BNPP.cours)
    #print("perf BNPP sur les deux derniers jo {0:.2%}".format((BNPP.cours]['close'] -1 )))