# test_jar.py

from jar import Jar

import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    jar.deposit(3)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(6)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3


def test_default_capacity_and_size():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0
    assert str(j) == ""

def test_negative_and_nonint_raises():
    with pytest.raises(ValueError):
        Jar(-1)

    j = Jar(5)

    with pytest.raises(ValueError):
        j.deposit(-2)

    with pytest.raises(ValueError):
        j.withdraw(-1)

    with pytest.raises(ValueError):
        j.deposit(2.5)

    with pytest.raises(ValueError):
        j.withdraw(1.2)

def test_overflow_deposit():
    j = Jar(3)
    j.deposit(2)
    with pytest.raises(ValueError):
        j.deposit(2)

def test_over_withdraw():
    j = Jar(3)
    j.deposit(1)
    with pytest.raises(ValueError):
        j.withdraw(2)
