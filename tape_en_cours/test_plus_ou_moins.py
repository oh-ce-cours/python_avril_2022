from plus_ou_moins import est_un_nombre, plus_ou_moins


def test_est_un_nombre():
    assert est_un_nombre("3")
    assert est_un_nombre("3.7")
    assert not est_un_nombre("toto")


def test_plus_ou_moins():
    nombre_propose = 1
    nombre_a_trouver = 2
    res = plus_ou_moins(nombre_propose, nombre_a_trouver)
    assert res > 0

    nombre_propose = 2
    nombre_a_trouver = 1
    res = plus_ou_moins(nombre_propose, nombre_a_trouver)
    assert res < 0

    nombre_propose = 2
    nombre_a_trouver = 2
    res = plus_ou_moins(nombre_propose, nombre_a_trouver)
    assert res is None
