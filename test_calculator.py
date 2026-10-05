from calculator import add, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    # Intentional error
    assert multiply(3, 4) == 13
