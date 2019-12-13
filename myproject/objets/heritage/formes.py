"""
les formes géometriques 2D
"""
import copy
from abc import abstractmethod, ABCMeta

from objets.points import Point


class Forme(object, metaclass=ABCMeta):
    """Forme 2D """

    def __init__(self, origine=Point()):
        """F = Forme(point)"""
        self.origine = copy.deepcopy(origine)

    def __str__(self):
        """Afficher le rectangle"""
        return "{} : origine={}".format(self.__class__.__name__, self.origine)

    @abstractmethod
    def surface(self):
        """calculer la surface """
        pass

    @abstractmethod
    def perimetre(self):
        """calculer le perimetre"""
        pass

    def deplacer(self, diffx, diffy):
        """deplacer le rectangle"""
        self.origine.deplacer(diffx, diffy)

if __name__ == "__main__":
   FO1 = Forme()
   print(FO1)
   FO1.deplacer(4, 5)
   print(FO1)
   print("surface ", FO1.surface())