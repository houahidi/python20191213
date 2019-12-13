"""
les  blocs : if , for, while, def , class
"""
liste = [3, 8 , 9 , 4, 7]
print("liste : ", liste)
print("parcours de la fin vers le debut avec un pas de 2")
for indice in range(len(liste), 0, -1):
    print("indice : ", indice,"=", liste[indice - 1 ])
print("parcours du debut vers la fin avec un pas de 1")
for indice in range(0, len(liste), 1):
    print("indice : ", indice,"=", liste[indice ])
print("while")
indice = len(liste) - 1
while indice >= 0 :
    print("indice : ", indice, "=", liste[indice])
    indice -= 2