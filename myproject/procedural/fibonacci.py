"""
suite de fibonacci
"""
u0, u1 = 1, 1
is_chiffre = False
while not is_chiffre:
    chiffre = input("Veuillez saisir un chiffre :")
    # if chiffre.isdigit():
    #     is_chiffre = True
    #     chiffre = int(chiffre)
    # else:
    #     print(chiffre, "n'est pas un chiffre")
    try:
        chiffre = int(chiffre)
        is_chiffre = True
    except :
        print(chiffre, "n'est pas un chiffre")

for indice in range(2, chiffre):
    un = u0 + u1
    print("u",indice , "= ", un, sep="")
    u0 = u1
    u1 = un
