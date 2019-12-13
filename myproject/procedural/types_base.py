"""
les types de base : int, float, boolean, str
"""

#entier
import copy

my_variable = 1
print("my_variable : ", my_variable, "type(my_variable)", type(my_variable))
my_variable = int("1")
print("my_variable : ", my_variable, "type(my_variable)", type(my_variable))

my_variable = int("2")
print("my_variable : ", my_variable, "type(my_variable)", type(my_variable))
#reel
my_variable = 1.0
my_variable = float("1.0")
my_variable = float(1)
print("my_variable : ", my_variable, "type(my_variable)", type(my_variable))
#chaine de caractere
my_variable = "1.0"
my_variable = '1.0'
my_variable = str(1.0)
print("my_variable : ", my_variable, "type(my_variable)", type(my_variable))
#boolean
my_variable = True
my_variable = False
print("my_variable : ", my_variable, "type", type(my_variable))
my_variable = bool(1)
print("my_variable :  bool(1) ", "type", type(my_variable))
my_variable = bool(0)
print("my_variable : bool(0)", "type", type(my_variable))
my_variable = bool("")
print("my_variable : ''", "type:", type(my_variable))
my_variable = bool(None)
print("my_variable : bool(None):",my_variable, "type:", type(bool(None)))

chaine = "bonjour "
print("chaine : ", chaine)
chaine1 = chaine
print("chaine1 : ", chaine1)
del(chaine) # chaine = None
chaine = "New chaine"
print("chaine : ", chaine)
print("chaine1 : ", chaine1)
print(chaine)

# les types simples sont des valeurs unitaires => chaque operation genère
# une  nouvelle valeur y compris l'opertateur =
chaine[0] = 'n' # n'est pas possible







