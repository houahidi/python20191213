"""
Exercice 3
"""
import math

# definitions


class Point():

    def __init__(self, valeur1=None, valeur2=None):
        """
        Initialise un point avec valeur1 et valeur2 qui sont des valeurs numériques
        :param valeur1:
        :param valeur2:
        :return:
        """
        if not valeur1:
            valeur1 = input("Saisissez l'abcisse : ")
        if not valeur2:
            valeur2 = input("Saisissez l'ordonnée du point : ")
        dico = {}
        if valeur1.isnumeric():
            self.x = float(valeur1)
        else:
            print_rouge(" /!\  Vous devez donner des nombres dans la fonction init()")
            exit(1)
        if valeur2.isnumeric():
            self.y = float(valeur2)
        else:
            print_rouge(" /!\  Vous devez donner des nombres dans la fonction init()")
            exit(1)

    def __str__(self):
        """
        Affiche les coordonnées du point
        :param point:
        :return:
        """
        return "[{}, {}]".format(self.x, self.y)

    def afficher_coordonnees(self):
        """
        Affiche les coordonnées du point
        :param point:
        """
        print_vert("\nVotre point est placé en ", self.x, "(x) et en ", self.y, "(y)")

    def deplacer_point(self, mX, mY):
        """
        Permet de déplaçer un point
        :param point:
        :param mX:
        :param mY:
        """
        print("\nAncienne position : ", self)
        X = self.x
        Y = self.y
        self.x = float(X) + float(mX)
        self.y = float(Y) + float(mY)
        print_vert("Votre point s'est déplaçé de ", mX, " en X et de ", mY," en Y")
        print_vert("Nouvelle position : ", self)

    def distance_lineaire(self, point2, indice):
        """
        Mesure la distance en X ou en Y de deux points (x ou y en tant qu'indice)
        :param point1:
        :param point2:
        :param indice:
        :return:
        """
        if indice == "x":
            indice1 = self.x
            indice2 = point2.x
        elif indice == "y":
            indice1 = self.y
            indice2 = point2.y
        else:
            print_rouge("Le troisième paramètre 'indice' doit etre 'x' ou 'y'")
            exit(1)
        if indice1 > indice2:
            distance = indice1 - indice2
            print("\nLa distance en ", indice, " entre le point1 et le point2 est : ", distance)
        elif indice1 == indice2:
            distance = 0
            print("\nLa distance en ", indice, " entre le point1 et le point2 est : ", distance)
        else:
            distance = indice2 - indice1
            print("\nLa distance en ", indice, " entre le point1 et le point2 est : ", distance)

        return distance

    def distance_entre(self, point2):
        """
        Affiche la distance entre deux points
        :param point1:
        :param point2:
        :return:
        """
        print("\nPoint1 : ", self, " Point2 : ", point2)
        distanceX = self.distance_lineaire(p2, "x")
        distanceY = self.distance_lineaire(p2, "y")
        print_vert("\nLa distance entre les deux points est : ", math.sqrt(distanceX ** 2 + distanceY ** 2))

def print_rouge(*text):
    """
    Imprime les arguments en rouge
    :param text:
    """
    txt = ""
    if len(text) > 1:
        for i in text:
            txt = txt + str(i)
    else:
        txt = str(text)
    print('\x1b[6;31m' + str(txt) + '\x1b[0m')

def print_vert(*text):
    """
    Imprime les arguments en vert
    :param text:
    """
    txt = ""
    if len(text) > 1:
        for i in text:
            txt = txt + str(i)
    else:
        txt = str(text)
    print('\x1b[6;32m' + str(txt) + '\x1b[0m')

if __name__ == "__main__":
    p1 = Point("5", "4")
    p1.afficher_coordonnees()
    p1.deplacer_point("0", "8")
    p1.afficher_coordonnees()
    p2 = Point("1", "1")
    p1.distance_entre(p2)
    help(p1)