ma_variable = 2


def ma_fonction():
    pass


ertyrserg = 2


class MaClasse:
    pass


a = ma_fonction()
a = MaClasse()


def logique_fizz_buzz(nombre: int) -> str:
    res = ""
    if nombre % 3 == 0:
        res = "fizz"
    if nombre % 5 == 0:
        res += "buzz"
    if not res:
        res = str(nombre)
    return res


logique_fizz_buzz(2)
