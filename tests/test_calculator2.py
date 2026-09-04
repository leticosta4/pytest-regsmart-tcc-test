from calculator2 import mult, div, seila


def test_mult():
    assert mult(2, 3) == 6


def test_div():
    assert div(6, 3) == 2


def test_seila():
    assert seila("test") == "seilatest"