"""
gestion de points 2D avec les liste

"""
import math

from procedural.commons import saisir_chiffre


class Point:
    """
    Un point 2D avec abcisse et ordonnee
    """
    # le constructeur : creer les objets
    def __init__(self, abscisse: int = 0, ordonnee: int = 0):
        """
        Initialisation d'un point
        PT1 = Point(1,1)
        PT1 = Point()
        """
        self.abscisse = int(abscisse)
        self.ordonnee = int(ordonnee)

    def __str__(self):
        """ str(self)"""
        return "Point:abscisse={}, ordonnee={}".format(self.abscisse, self.ordonnee)


    def deplacer(self, diffx: int, diffy: int):
        """deplacer un point """
        self.abscisse += diffx
        self.ordonnee += diffy


    def distance(self, point2):
        """ distance entre 2 points"""
        diffx = self.abscisse - point2.abscisse
        diffy = self.ordonnee - point2.ordonnee
        return math.sqrt(diffx ** 2 + diffy ** 2)

    def __sub__(self, other):
        """ self - other == self.__sub__(other) """
        return self.distance(other)

    def __copy__(self):
        return Point(self.abscisse, self.ordonnee)
    # def __getitem__(self, item):
    #     # """ self[indice] == self.__getitem__(indice) """
    #     #     if item == 0:
    #     #         return self.abscisse
    #     #     elif item == 1 :
    #     #         return  self.ordonnee
    #     #     else:
    #     #         raise StopIteration()
    # def __iter__(self):
    #     return iter( [self.abscisse, self.ordonnee])

    def __iter__(self):
        print("__iter__")
        self.indice = 0
        return self

    def __next__(self):
        print("__next__")
        self.indice += 1
        if self.indice == 1:
            return self.abscisse
        elif self.indice == 2 :
            return self.ordonnee
        else:
            del self.indice
            raise StopIteration()


if __name__ == "__main__":
    #Instanciation d'objet
    #ABS = saisir_chiffre("Saisir l'abcisse :")
    #ORD = saisir_chiffre("Saisir l'ordonnee :")
    print("init PT1")
    PT1 = Point()
    print("init PT2")
    PT2 = Point(3, 5)
    print("afficher PT1")
    print( str(PT1))
    print("afficher PT2")
    print(PT2)
    print("deplacer PT2 de 3, 2")
    PT2.deplacer(3, 2)
    print(PT2)
    print("distance entre PT1,PT2 :", PT1.distance(PT2))
    print("distance entre PT1 - PT2 :", PT1 - PT2)
    print(PT1)
    print(PT2)
    PT1 = Point(100, 300)

    print("comportement d'iterateur")
    print("__x, y = PT2")
    x, y = PT2
    print("x:",x, "y", y)
    print("__for elem in PT1")
    for elem in PT1:
        print("elem : ", elem)
        print("PT1.indice", PT1.indice)
    print("__iter(PT1)")
    it = iter(PT1)
    print("suivant : ", it.__next__())
    print("suivant : ", it.__next__())
    print("PT1.indice : ", PT1.indice)
    #print("PT1[1] : ", PT1[1])
