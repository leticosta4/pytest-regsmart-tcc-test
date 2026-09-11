from calculator import add, subtract, pre_aleatorio


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_pre_aleatorio():
    assert pre_aleatorio() == "oxe"
