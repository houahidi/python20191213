"""
Gestion des cercles 2D
"""
import math

from objets.heritage.formes import Forme
from objets.points import Point


class Cercle(Forme):
    """Cercle avec rayon """
    def __init__(self, origine:Point, rayon: float):
        """
        Initialiser un nouveau Cercle
        C1 = Cercle(3)
        :param rayon: le rayon
        """
        Forme.__init__(self, origine)
        self.rayon = float(rayon)

    def __str__(self):
        """str(self)"""
        return "{}, rayon = {}".format(Forme.__str__(self), self.rayon)
    def surface(self):
        """calculer la surface """
        return math.pi * self.rayon ** 2
    def perimetre(self):
        """calculer le perimetre """
        return 2 * math.pi * self.rayon

if __name__ == "__main__":
    CER1 = Cercle(Point(), 5)
    print(CER1)
    print("surface : ", CER1.surface())
    print("perimetre : ", CER1.perimetre())
