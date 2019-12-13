"""
les structures évoluées de python : ensemble
    - ensemble modifiable avec doublons : list
    - ensemble non modifiable avec doublons : tuple
    - ensemble sans doublons : dictionnaire

"""
import copy

liste = [] # ensemble vide
liste = list() # ensemble vide
liste = [1,1,1] # list([1,1,1])
print("liste : ", liste, type(liste))
# cas I : modification d'un élément
liste1 = liste # je ne créee pas de nouvelle liste
                # la liste peut etre manipulée avec liste ou liste1
liste[0] = 1000 #liste.__setitem__(0, 1000)
print("liste : ", liste, type(liste))
print("liste1 : ", liste1, type(liste1))
print("je crée une nouvelle liste")
liste2 = list(liste)  # je crée une nouvelle liste
liste[1] = 1000
print("liste : ", liste, type(liste))
print("liste2 : ", liste2, type(liste2))
print("cas II : supprimer un élément (dernier)")
# cas II : supprimer un élément (dernier)
del(liste[-1])
print("liste : ", liste, type(liste))
print("liste1 : ", liste1, type(liste1))
print("liste2 : ", liste2, type(liste2))
# cas III : ajouter un nouveau élément à la fin
print("ajouter un nouveau élément à la fin : append")
liste1.append(2000)
print("liste : ", liste, type(liste))
print("liste1 : ", liste1, type(liste1))
print("liste2 : ", liste2, type(liste2))
print("inserer à une position un nouveau élément : insert")
liste1.insert(1, 3000)
print("liste1 : ", liste1, type(liste1))
print("liste2 : ", liste2, type(liste2))
# slicing
chaine= "bonjour tout le monde"
souchaine = chaine[ : chaine.index('t',9)]
print("sous chaine : ", souchaine)
liste = chaine.split(' ')
print("liste : ", liste)
# faire attention le slincing copie les addresses des objets
objet1 = [1,1]
objet2 = [2,2]
liste = (objet1, objet2) # tuple
sousliste = liste[-1: ]
clone = copy.deepcopy(liste[-1:])
objet2.append(1000)
print("objet2 :", objet2)
print("liste : ", liste)
print("sousliste : ", sousliste)
print("clone : ", clone)

# dictionnaire =
dico = dict()
dico = {}
dico["cle1"] = "valeur1"
dico.__setitem__("cle2", "valeur2")
print("dico : ", dico)
print("taille : ", len(dico), dico.__len__())
print("cle1 in dico ", "cle1" in dico, dico.__contains__("cle1"))





