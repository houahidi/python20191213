"""
Exercice 4 - rectangle
"""

import math
import sys

class Rectangle:
    """
    Définit un rectangle par sa largeur et sa longueur
    """
    def __init__(self, longueur = 0, largeur = 0):
        """
        Initialise la largeur et la longueur du rectangle
        :param longueur:
        :param largeur:
        """
        try:
            self.longueur = float(longueur)
            self.largeur = float(largeur)
        except ValueError:
            print("Vous devez rentrez les nombres à virgules pour utiliser l'objet (ex: r& = Rectangle(0.7, 5))")
            sys.exit(1)

    def afficher(self):
        """
        Affiche la largeur et la longueur du rectangle
        """
        print("Votre reclangle fait ", self.largeur, " en largeur et ", self.longueur, " en longueur")

    def surface(self):
        """
        Imprime la surface du rectangle
        :return:
        """
        surface = self.longueur * self.largeur
        print("La surface de votre rectangle est de : ", surface)

    def permietre(self):
        """
        Imprime le périmètre de l'objet rectangle
        :return:
        """
        perimetre = self.longueur *2 + self.largeur*2
        print("le périmètre de votre rectangle est de : ", perimetre)


class Cercle:
    """
    Définit un rectangle par sa largeur et sa longueur
    """
    def __init__(self, rayon=0):
        """
        Initialise le rayon du cercle
        :param rayon:
        """
        try:
            self.rayon = float(rayon)
        except ValueError:
            print("Vous devez rentrez les nombres à virgules pour utiliser l'objet (ex: c1 = Cercle(0.8)")
            sys.exit(1)

    def __str__(self):
        """
        Affiche le rayon du cercle
        """
        return "Votre Cercle à un rayon de : {}".format(self.rayon)

    def surface(self):
        """
        Imprime la surface du cercle
        :return:
        """
        surface = self.rayon **2 * math.pi
        return surface


    def perimetre(self):
        """
        Imprime le périmètre de l'objet cercle
        :return:
        """
        perimetre = 2 * math.pi * self.rayon
        return perimetre


if __name__ == "__main__":
    R1 = Rectangle(5, 5)
    R1.afficher()
    R1.surface()
    R1.permietre()
    print(type(R1))
    print("\n")

    C1 = Cercle(9.5)
    print(C1)
    print("La surface de votre cercle est de : ", C1.surface())
    print("le périmètre de votre cercle est de : ", C1.perimetre())
    print(str(type(C1)).split('.')[1].split('\'')[0])
