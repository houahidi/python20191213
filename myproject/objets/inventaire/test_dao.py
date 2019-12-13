import unittest

from objets.inventaire.dao import DaoException
from objets.inventaire.mysql_dao import MediaDaoMySQL


class MediaDaoTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("avant tous les tests")
        cls.M_DAO = MediaDaoMySQL(host="192.168.16.100",
                              db="bibliotheque_db",
                              user="root",
                              password="admin")

    @classmethod
    def tearDownClass(cls) -> None:
        print("après tous les tests")
        cls.M_DAO = None

    def test_1_lister(self):
        try:
            MEDIAS = self.M_DAO.lister()
            self.assertEqual(3, len(MEDIAS))
        except DaoException as excpt:
            self.fail(excpt)

    def test_2_lister_par_id(self):
        try:
            MEDIA = self.M_DAO.listerParId(1)
            self.assertIsNotNone(MEDIA)
            self.assertEqual("Python pour les experts", MEDIA.nom)
        except DaoException as excpt:
            self.fail(excpt)
    def test_3_lister_par_id_avec_excep(self):
        self.assertRaises(DaoException,self.M_DAO.listerParId, (1))



if __name__ == '__main__':
    unittest.main()
