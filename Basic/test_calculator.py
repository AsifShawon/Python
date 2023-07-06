from Calculator import square_of

def main():
    assert test_negative(2) == 4


def test_zero():
    assert square_of(0) == 0


def test_positive():
    assert square_of(2) == 4
    assert square_of(3) == 9


def test_negative():
    assert square_of(-2) == 4
    assert square_of(-3) == 9


if __name__ == "__main__":
    main()