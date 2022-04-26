def est_divisible_par(dividende, diviseur):
    """Indique si le dividende est divisible par le diviseur"""
    return dividende % diviseur == 0


def logique_fizz_buzz(nombre: int) -> str:
    res = ""
    if est_divisible_par(nombre, 3):
        res = "fizz"
    if est_divisible_par(nombre, 5):
        res += "buzz"
    if not res:
        res = str(nombre)
    return res


def fizzbuzz_mieux_testable(nombre_max):
    """ """
    all_res = []
    for nombre in range(1, nombre_max):
        all_res.append(logique_fizz_buzz(nombre))
    return all_res
