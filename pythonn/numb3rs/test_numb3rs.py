from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate('1.2.3') == False
    assert validate('1.2.3.4.5') == False
    assert validate('1.2.3.4') == True
    assert validate('cat') == False


def test_range():
    assert validate('12.23.43.225') == True
    assert validate('225.226.765.1') == False


if __name__ == "__main__":
    main()
