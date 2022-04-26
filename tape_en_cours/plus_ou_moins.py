import random
from tkinter.messagebox import NO

NOMBRE_A_TROUVER = 5

# demande un nombre à l'utilisateur
# essayer de convertir la chaine en nombre
# indique si c'est plus ou moins
# indique si c'est gagné


while True:
    nombre_propose = int(input("Entre un nombre s'il vous plait: "))
    if nombre_propose > NOMBRE_A_TROUVER:
        print("c'est moins")
    elif nombre_propose < NOMBRE_A_TROUVER:
        print("c'est plus")
    else:
        break


print("bravo")
