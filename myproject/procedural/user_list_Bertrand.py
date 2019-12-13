"""
    Programme interactif  de manipulation d'une liste

"""

# Les définitions


# Scenario de tests
if __name__ == "__main__":

    listSize = 'reset'

    while listSize != "quit" :
        if listSize == 'reset':
            myList = list()
            listSize = input("Veuillez indiquer la taille de la liste à créer : ")

        if listSize and listSize.isnumeric():
            listSizeNum = int(listSize)
            for i in range(0, listSizeNum):
                element = input("Veuillez indiquer l'élément numérique n°"+str(i)+" : ")
                while not element.isnumeric():
                    element = input("Veuillez indiquer l'élément numérique n°" + str(i) + " : ")

                myList.append(int(element))

            iAvg = sum(myList)/ len(myList)
            iMin = min(myList)
            iMax = max(myList)
            print(myList)
            print("Min : "+str(iMin))
            print("Max : "+str(iMax))
            print("Avg : "+str(iAvg))
            listSize = 'reset'
        if not listSize.isnumeric():
            listSize = input("'" + listSize + "' n'est pas un nombre. Merci de saisir un nombre : ")
