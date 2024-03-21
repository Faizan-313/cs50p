from jar import Jar


def test_init():
    jar = jar()
    assert jar.capacity = 12
    jar1 = jar(3)
    assert jar1.capacity = 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(3)
    assert jar.size == 3


def test_withdraw():
    jar = jar()
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    jar.withdraw(1)
    assert jar.size == 2
