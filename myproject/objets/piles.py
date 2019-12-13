"""
    Gestion d'une pile
"""

# Les définitions
#----------------

class PileException(BaseException):
    def __init__(self, code, msg,  *args):
        BaseException.__init__(self, *args)
        self.code = code
        self.msg = msg

    def __str__(self):
        return "PileException: code={}, msg={}, args={}".format(self.code,
                                                              self.msg,
                                                              self.args)



class Pile:
    """ Class représentant une pile d'objets avec une taille max """

    def __init__(self, taille: int=10):
        """ Initialisation de la pile """
        self.elements = list()
        self.tailleMax = int(taille)

    def clear(self):
        """ Fonction de réinitialisation de la pile """
        self.elements.clear()

    def empiler(self, p_input):
        """ Empilement d'un élément sur la pile """
        if len(self.elements) >= self.tailleMax:
          raise PileException(1, "La Pile est pleine: la taill max {} est dépassée".format(self.tailleMax))

        self.elements.append(p_input)

    def depiler(self):
        """ Dépilement du dernier élément de la pile """
        if len(self.elements) > 0:
            self.elements.pop()
        else:
           raise PileException(2, "La Pile est vide")

    def __str__(self):
        """ Affichage des statistiques de la pile """
        return "Pile : tailleMAX={}, nombre d'elements={}".format(self.tailleMax, len(self.elements))


# Scenario de tests
#------------------
if __name__ == "__main__":

    PILE = Pile(2)
    INPUT = input("Que voulez-vous faire (+, -, =, reset) ? : ")
    while INPUT != "quit":
        if INPUT == 'reset':
            PILE.clear()
        elif INPUT == '=':
            disp = "Size : {}\n".format(len(PILE.elements))
            disp += "Min : {}\n".format(min(PILE.elements))
            disp += "Max : {}\n".format(max(PILE.elements))
            disp += "Avg : {}\n".format(sum(PILE.elements) / len(PILE.elements))
            print(disp)
        elif len(INPUT) > 0 and INPUT[0] in ('+', '-'):
            if INPUT[0] == '+':
                try:
                    PILE.empiler(int(INPUT[1:]))
                except PileException as excpt:
                    print(excpt)

            elif INPUT[0] == '-':
                try:
                    PILE.depiler()
                except PileException as excpt :
                    print(excpt)
            else:
                print("Je n'ai pas compris ... s'il vous plaît, auriez-vous l'amabilité de reformuler ?\n")
        else:
            print("Je n'ai pas compris ... merci de ré-essayer ?\n")


        print(PILE)
        INPUT = input("Que voulez-vous faire (+, -, =, reset) ? : ")
