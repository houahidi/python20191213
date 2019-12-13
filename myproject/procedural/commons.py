"""
fonction communes

"""


def saisir_chiffre(chaine):
    """saisi d'un chiffre """
    is_chiffre = False
    while not is_chiffre:
        try:
            chiffre = int(input(chaine))
            is_chiffre = True
        except ValueError:
            print("ceci n'est pas un entier ")
    return chiffre
