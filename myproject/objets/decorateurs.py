"""
exemple de manipulateur de decorateur
"""

class Boisson :
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
    def __str__(self):
        return "{}".format(self.nom)
    def calculer_prix(self):
        return self.prix

class BoissonDecorateur(Boisson):
    def __init__(self, boisson, nom, prix):
        self.boisson = boisson
        self.nom = nom
        self.prix = prix
    def __str__(self):
        return "[ {} (avec {}) ]".format(str(self.boisson), self.nom)

    def calculer_prix(self):
        return self.boisson.calculer_prix() + self.prix


if __name__ == '__main__':
    CAFE = Boisson("cafe", 2.5)
    print(CAFE, CAFE.calculer_prix())
    CAFE_CHANTILLY = BoissonDecorateur(CAFE, "chantilly", 1.50)
    print(CAFE_CHANTILLY, CAFE_CHANTILLY.calculer_prix())
    CAFE_CHAN_SUCRE = BoissonDecorateur(CAFE_CHANTILLY, "sucre", 0)
    print(CAFE_CHAN_SUCRE, CAFE_CHAN_SUCRE.calculer_prix())



