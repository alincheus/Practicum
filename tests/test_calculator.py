import pytest
from src.calculations.calculator import Calculator

calculator = Calculator()

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert calculator.subtract(10, 4) == 6

def test_multiply():
    assert calculator.multiply(3, 3) == 9

def test_divide():
    assert calculator.divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

def test_large_numbers():
    assert calculator.add(1_000_000, 1_000_000) == 2_000_000
