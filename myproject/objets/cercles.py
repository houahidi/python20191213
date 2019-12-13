"""
Gestion des cercles 2D
"""
import copy
import math

from objets.points import Point


class Cercle:
    """Cercle avec rayon """
    def __init__(self, rayon: float = 0.0, origine: Point = Point(0, 0)):
        """
        Initialiser un nouveau Cercle
        C1 = Cercle(3)
        :param rayon: le rayon
        """
        self.rayon = float(rayon)
        self.origine = copy.deepcopy(origine)
    def __str__(self):
        """str(self)"""
        return "Cercle : rayon = {}, origine={}".format(self.rayon, self.origine)
    def surface(self):
        """calculer la surface """
        return math.pi * self.rayon ** 2
    def perimetre(self):
        """calculer le perimetre """
        return 2 * math.pi * self.rayon
    def deplacer(self, diffx, diffy):
        """deplacer le rectangle"""
        self.origine.deplacer(diffx, diffy)

if __name__ == "__main__":
    CER1 = Cercle(5)
    print(CER1)
    print("surface : ", CER1.surface())
    print("perimetre : ", CER1.perimetre())
    CER1.deplacer(4, 5)
    print(CER1)
