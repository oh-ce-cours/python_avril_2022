from plus_ou_moins import est_un_nombre


def test_est_un_nombre():
    assert est_un_nombre("3")
    assert est_un_nombre("3.7")
    assert not est_un_nombre("toto")
