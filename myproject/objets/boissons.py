"""
Définir des boissons
"""
from objets.ingredients import Ingredient


class Boisson(Ingredient):
    """
    Définir la class Boisson avec un prix et un nom
    """

    def __init__(self, name, price):
        """
        Initialiser la boisson
        """
        super().__init__(name, price)
        self.name = name
        self.price = price


if __name__ == '__main__':
    DRINK1 = Boisson('Coca', 7)
    print(DRINK1)
    DRINK2 = Boisson('Chocolat', 2)
    print(DRINK2)
    DRINK1+DRINK2
    print(DRINK1)
    INGR1 = Ingredient('lait', 3)
    print(INGR1)
    DRINK1.ajouter(INGR1)
    print(DRINK1)
