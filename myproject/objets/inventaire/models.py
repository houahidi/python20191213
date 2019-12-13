"""
l'inventaire
"""

class Media:
    """medias de la bibliotheque"""
    def __init__(self, id, nom, auteur):
        self.__id = id
        self.__nom = nom
        self.__auteur = auteur
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, val):
        self.__id = val

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, val):
        self.__nom = val

    @property
    def auteur(self):
        return self.__auteur

    @id.setter
    def auteur(self, val):
        self.__auteur = val

    def __str__(self):
        return "Media: id={}, nom={}, auteur={}".format(self.__id,
                                                        self.__nom,
                                                        self.__auteur)
    def __eq__(self, other):
        status = False
        if other and isinstance(other, Media):
            return self.__id == other.__id
        return  status