"""
Gestion des rectangles 2D
"""
import copy

from objets.heritage.formes import Forme
from objets.points import Point


class Rectangle (Forme): # Rectangle hérite de la classe Forme
    """
    Rectangle 2D avec longeur et largeur
    """
    def __init__(self, origine:Point, long: float, larg: float ):
        """
        Définir un rectangle 2D
        R = Rectangle(point, 1,2)
        :param long: longueur
        :param larg: largeur
        """
        Forme.__init__(self, origine)
        #super(Rectangle, self).__init__(origine)
        self.long = float(long)
        self.larg = float(larg)

    def __str__(self):
        """Afficher le rectangle"""
        return "{}, long={}, larg={}".format(Forme.__str__(self), self.long, self.larg)
    def surface(self):
        """calculer la surface """
        return self.long * self.larg

    def perimetre(self):
        """calculer le perimetre"""
        return 2 * (self.long + self.larg)



if __name__ == "__main__":
    PT1 = Point(0, 0)
    print("PT1", PT1)
    print("créer REC1 avec 3, 5")
    REC1 = Rectangle(PT1, 3, 5)
    REC2 = Rectangle(PT1, 1, 1)
    print("REC1", REC1)
    print("REC1 surface : ", REC1.surface())
    print("REC1 perimetre : ", REC1.perimetre())
    print("REC2", REC2)
    print("REC2 surface : ", REC2.surface())
    print("REC2 perimetre : ", REC2.perimetre())
    #deplacer le REC1
    print("deplacer REC1 3, 4")
    REC1.deplacer(3, 4)
    PT1.deplacer(1, 1)
    print("REC1", REC1)
    print("REC2", REC2)
    print("PT1", PT1)
