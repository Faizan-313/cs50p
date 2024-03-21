from bank import value

def main():
    test_zero()

def test_zer0():
    assert value("hello gi") == 0
    assert value("Hello") == 0
    assert value("Hello Gi") == 0
def test_twenty():
    assert value("htf") == 20
    assert value("H") == 20
def test_100():
    assert value("What are You Doing") == 100
    assert value("what's up") == 100

if __name__ == "__main__":
    main()
