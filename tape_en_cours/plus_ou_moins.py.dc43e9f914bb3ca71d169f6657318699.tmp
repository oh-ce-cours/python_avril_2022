import random

NOMBRE_A_TROUVER = 5
CHAINE_CEST_PLUS = "c'est plus"
CHAINE_CEST_MOINS = "c'est moins"

# demande un nombre à l'utilisateur
def demande_a_l_utilisateur():
    return input("Entre un nombre s'il vous plait: ")


def est_un_nombre(valeur: str) -> bool:
    try:
        float(valeur)
    except (ValueError, TypeError) as e:
        return False
    except IndexError:
        return False
    else:
        return True


def demander_un_nombre_a_l_utilisateur() -> float:
    entree = demande_a_l_utilisateur()
    while not est_un_nombre(entree):
        entree = demande_a_l_utilisateur()
    return float(entree)


def plus_ou_moins(nombre_propose, nombre_a_trouver):
    if nombre_propose < nombre_a_trouver:
        return 1
    if nombre_propose > nombre_a_trouver:
        return -1


def gagne(nombre_propose, nombre_a_trouver):
    return nombre_a_trouver == nombre_propose


# essayer de convertir la chaine en nombre
# indique si c'est plus ou moins
# indique si c'est gagné


def main():
    while True:
        nombre_propose = int(demander_un_nombre_a_l_utilisateur())
        valeur_plus_moins = plus_ou_moins(nombre_propose, NOMBRE_A_TROUVER)
        if valeur_plus_moins:
            if valeur_plus_moins < 0:
                print(CHAINE_CEST_PLUS)
            if valeur_plus_moins > 0:
                print(CHAINE_CEST_PLUS)
        if gagne(nombre_propose, NOMBRE_A_TROUVER):
            break
    print("bravo")


if __name__ == "__main__":
    main()
