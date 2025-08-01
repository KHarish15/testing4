import pytest
from main import add, subtract, divide, multiply, is_even, get_max

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(1, 1) == 1
    with pytest.raises(ValueError):
        divide(5, 0)
    with pytest.raises(ValueError):
        divide(10, 0)

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 5) == -10

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False
    assert is_even(0) is True
    assert is_even(-2) is True

def test_get_max():
    assert get_max([1, 5, 3]) == 5
    with pytest.raises(ValueError):
        get_max([])
    with pytest.raises(ValueError):
        get_max(None)
    assert get_max([10]) == 10
    assert get_max([-1, -5, -3]) == -1
    assert get_max([5, 5, 5]) == 5

def test_fail_example():
    assert add(2, 2) == 4 #Correct expected value
