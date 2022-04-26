import random

NOMBRE_A_TROUVER = 5

# demande un nombre à l'utilisateur
def demande_a_l_utilisateur():
    return input("Entre un nombre s'il vous plait: ")


def est_un_nombre(valeur: str) -> bool:
    try:
        float(valeur)
    except ValueError:
        return False
    else:
        return True


def demander_un_nombre_a_l_utilisateur() -> float:
    entree = demande_a_l_utilisateur()
    while not est_un_nombre(entree):
        entree = demande_a_l_utilisateur()
    return float(entree)


# essayer de convertir la chaine en nombre
# indique si c'est plus ou moins
# indique si c'est gagné


def main():
    while True:
        nombre_propose = int(demander_un_nombre_a_l_utilisateur())
        if nombre_propose > NOMBRE_A_TROUVER:
            print("c'est moins")
        elif nombre_propose < NOMBRE_A_TROUVER:
            print("c'est plus")
        else:
            break
    print("bravo")
