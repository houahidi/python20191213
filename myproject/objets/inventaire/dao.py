"""
accès aux bases de données (mysql)

"""
from abc import abstractmethod, ABCMeta



class DaoException(BaseException):
    """ Problème d'accès aux données"""
    def __init__(self, *args):
        BaseException.__init__(self, *args)

    def __str__(self):
        return "DaoExceptin: args={}".format(self.args)

class MediaDao(object,metaclass=ABCMeta):
    """Accès aux medias """
    @abstractmethod
    def lister(self):
        """ la liste des médias
            raise DaoException
            """
        pass

    @abstractmethod
    def listerParId(self, id):
        """ rcupérer un media
            raise DaoException
            """
        pass

