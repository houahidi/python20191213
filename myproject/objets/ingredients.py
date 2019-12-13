"""
Définir des ingredients
"""


class Ingredient:
    """
    Définir la class ingredient avec un prix et un nom
    """

    def __init__(self, name, price):
        """
        Initialiser l'ingredient
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Afficher la boisson
        """
        return "{}: {}, Prix: {}".format(self.__class__.__name__, self.name, self.price)

    def ajouter(self, ingredient2):
        """
        Ajouter un ingredient
        """
        self.price += ingredient2.price
        self.name += " avec {}".format(ingredient2.name)
        return self.price

    def __add__(self, ingredient2):
        self.ajouter(ingredient2)
