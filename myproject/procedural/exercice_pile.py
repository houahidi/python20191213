"""
programme interactif de manipulation d'une pile
"""


if __name__ == "__main__":
    c = input("saisir  la taille de la liste : ")
    while not c.isdigit() :
        print("ceci n'est pas un entier ")
        c = input("resaisir la taille de la liste  : ")

    liste = list()

    inst=input("taper 1 pour empiler 2 pour dépiler 3 pour le résultat")


    while inst != '3':
        if inst=='1':
            if len(liste) < int(c) :
                x = input("saisisser la valeur à empiler")
                while not x.isdigit():
                    tuple = "entier", x
                    print("{1:f} n'est pas un {0:f} ".format(*tuple))
                    x = input("saisisser à nouvreau la valeur à empiler")
                liste.append(int(x))
            else:
                print("pile plein, vous ne pouvez plus empiler")

        if inst=='2':
            if len(liste) > 0 :
                del liste[-1]
                print("dépilé avec succes")
            else :
                print("pile vide, vous ne pouvez plus dépiler")

        if inst not in ('1','2','3') :
            print("instruction non connue, veuillez taper 1 pour empiler 2 pour dépiler 3 pour le résultat ")


        inst=input("taper 1 pour empiler 2 pour dépiler 3 pour le résultat")

    print("votre liste est :",liste)
    print("la valeur min de la liste est :",min(liste))

    print("la valeur max de la liste est :",max(liste))

    print("la valeur moyenne de la liste est :",sum(liste)/len(liste))