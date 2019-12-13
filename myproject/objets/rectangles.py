"""
Gestion des rectangles 2D
"""
import copy
from objets.points import Point


class Rectangle:
    """
    Rectangle 2D avec longeur et largeur
    """
    def __init__(self, long: float, larg: float, origine: Point = Point(0, 0)):
        """
        Définir un rectangle 2D
        R = Rectangle(1,2)
        :param long: longueur
        :param larg: largeur
        """
        self.long = float(long)
        self.larg = float(larg)
        self.origine = copy.deepcopy(origine)
    def __str__(self):
        """Afficher le rectangle"""
        return "Rectangle : long={}, larg={}, origine ={}".format(self.long,
                                                                  self.larg,
                                                                  self.origine)
    def surface(self):
        """calculer la surface """
        return self.long * self.larg
    def perimetre(self):
        """calculer le perimetre"""
        return 2 * (self.long + self.larg)
    def deplacer(self, diffx, diffy):
        """deplacer le rectangle"""
        self.origine.deplacer(diffx, diffy)


if __name__ == "__main__":
    PT1 = Point(0, 0)
    print("PT1", PT1)
    print("créer REC1 avec 3, 5")
    REC1 = Rectangle(3, 5, PT1)
    REC2 = Rectangle(1, 1, PT1)
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
