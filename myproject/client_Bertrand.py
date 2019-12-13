"""
    Programme definissant les attributs et le comportement d'un client
"""

# Les définitions
#----------------
from datetime import date


class Client:
    """ Class décrivant un client """

    COMPTEUR_COMPTE = 0

    def __init__(self, nom: str, type: str):
        """ Constructeur de la class Client """
        self.nom = nom
        self.type = type
        self.comptes = dict()
        self.transactions = list()

    def __str__(self):
        printComptes = ""
        if len(self.comptes) == 0:
            printComptes = "   (pas de compte)\n"
        else:
            for pK, pV in self.comptes.items():
                printComptes += " - n°"+str(pK)+" ( "+str(pV)+"€ )\n"
        return self.nom+" ("+self.type+"):\n"+printComptes

    def ouvrirCompte(self):
        self.__class__.COMPTEUR_COMPTE += 1
        self.comptes[self.__class__.COMPTEUR_COMPTE] = 0.
        return self.__class__.COMPTEUR_COMPTE

    def crediterCompte(self, id, montant):
        if id in self.comptes.keys():
            self.comptes[id] += montant
            self.transactions.append((id, montant, date.today()))

    def debiterCompte(self, id, montant):
        if id in self.comptes.keys():
            self.comptes[id] -= montant
            self.transactions.append((id, -1*montant, date.today()))

    def fermerCompte(self, id: int):
        if id in self.comptes.keys():
            del(self.comptes[id])
            return True
        else:
            return False

    def afficherTransactions(self):
        for item in self.transactions:
            print("n°"+str(item[0])+", "+str(item[1])+"€, "+str(item[2]))

# Scenario de tests
#------------------
if __name__ == "__main__":
    CLIENT1 = Client("Pierre", "Personne Physique")
    print(CLIENT1)
    CLIENT2 = Client("Paul", "Personne Morale")
    COMPTE2_1 = CLIENT2.ouvrirCompte()
    print(CLIENT2)
    CLIENT3 = Client("Jacques", "Personne Physique")
    COMPTE3_1 = CLIENT3.ouvrirCompte()
    COMPTE3_2 = CLIENT3.ouvrirCompte()
    COMPTE3_3 = CLIENT3.ouvrirCompte()
    print(CLIENT3)
    CLIENT3.crediterCompte(COMPTE3_3, 100)
    CLIENT3.crediterCompte(COMPTE3_3, 200)
    CLIENT3.debiterCompte(COMPTE3_1, 1500)
    CLIENT3.debiterCompte(COMPTE3_3, 50)
    if CLIENT3.fermerCompte(COMPTE3_2):
        print(" => Compte n°{} fermé".format(COMPTE3_2))
    else:
        print(" => Pas de compte portant ce numéro ... :-(")
    print(CLIENT3)
    CLIENT3.afficherTransactions()
    pass
