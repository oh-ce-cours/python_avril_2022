from fizz_buzz import logique_fizz_buzz, est_divisible_par


def test_fizz_buzz():
    assert logique_fizz_buzz(1) == "1"
    assert logique_fizz_buzz(3) == "fizz"
    assert logique_fizz_buzz(5) == "buzz"
    assert logique_fizz_buzz(15) == "fizzbuzz"


def test_fizz_buzz_avec_des_grands_nombres():
    assert logique_fizz_buzz(544566698896565) == "buzz"


def test_division():
    assert est_divisible_par(3, 3) == True
    assert est_divisible_par(5, 2) == False
