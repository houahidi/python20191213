"""
l'accès aux données avec mysql
"""
import mysql.connector
from objets.inventaire.dao import MediaDao, DaoException
from objets.inventaire.models import Media


class MediaDaoMySQL(MediaDao):
    """accès aux medias en mysql """

    def __init__(self, **kwargs):
        self.host = kwargs["host"]
        self.db = kwargs["db"]
        self.user = kwargs["user"]
        self.password = kwargs["password"]

    def listerParId(self, id):
        media, cursor, conn = (None,) * 3
        try:
            conn = mysql.connector.connect(host=self.host,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db)
            cursor = conn.cursor()
            request = "select id, nom, auteur from media_t where id ={}".format(id)
            cursor.execute(request)
            row = cursor.fetchone()
            if cursor.rowcount > 0:
                return Media(row[0], row[1], row[2])
            raise DaoException(1, "Le media avec id {} n'existe pas".format(id))

        except Exception as excep:
            raise DaoException(excep)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        return media

    def lister(self):
        medias, cursor, conn = (None,) * 3
        try:
            medias = []
            conn = mysql.connector.connect(host=self.host,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db)
            cursor = conn.cursor()
            request = "select id, nom, auteur from media_t"
            cursor.execute(request)
            for row in cursor.fetchall():
                media = Media(row[0], row[1], row[2])
                medias.append(media)
        except Exception as excep:
            raise DaoException(excep)
        finally:
            if cursor :
                cursor.close()
            if conn:
                conn.close()

        return medias

if __name__ == "__main__":
    try:
        print("lister les medias")
        M_DAO = MediaDaoMySQL(host="192.168.16.100",
                              db="bibliotheque_db",
                              user="root",
                              password="admin")
        MEDIAS = M_DAO.lister()
        for media in MEDIAS:
            print(media)
        print("lister un media par id ")
        M_1 = M_DAO.listerParId(1)
        print("M_1 : ", M_1)
        M_1 = M_DAO.listerParId(10)
        print("M_1 : ", M_1)
    except DaoException as excpt:
        print(excpt)
