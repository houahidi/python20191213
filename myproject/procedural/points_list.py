"""
gestion de points 2D avec les liste

"""
import math

from commons import saisir_chiffre


def init(abcisse=None, ordonnee= None):
    """
    Initialisation d'un self
    PT1 = init(1,1)
    PT1 = init()
    """
    if not abcisse:
        abcisse = saisir_chiffre("Saisir l'abcisse :")
    if not ordonnee:
        ordonnee = saisir_chiffre("Saisir l'ordonnee :")
    return [abcisse, ordonnee]

def afficher(point):
    """afficher les coordonnes d'un self"""
    print("self x: {}, y : {}".format(point[0], point[1]))

def deplacer(point, diffx, diffy):
    """deplacer un self """
    point[0] += diffx
    point[1] += diffy

def distance(point1, point2):
    """ distance entre 2 points"""
    diffx = point1[0] - point2[0]
    diffy = point1[1] - point2[1]
    return math.sqrt(diffx ** 2 + diffy **2 )

if __name__ == "__main__":
    print("init PT1")
    PT1 = init()
    print("init PT2")
    PT2 = init(3, 5)
    print("afficher PT1")
    afficher(PT1)
    print("afficher PT2")
    afficher(PT2)
    print("deplacer PT2 de 3, 2")
    deplacer(PT2, 3, 2)
    afficher(PT2)
    print("distance entre PT1,PT2 :", distance(PT1, PT2))