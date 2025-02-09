# tests/test_calculator.py

import pytest
from calculator.calculator import Calculator, Calculations

@pytest.fixture
def clear_history():
    """Fixture to clear history before each test."""
    Calculations.clear_history()

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8), (10, -5, 5), (0, 0, 0)
])
def test_add(clear_history, num1, num2, expected):
    assert Calculator.add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2), (10, -5, 15), (0, 0, 0)
])
def test_subtract(clear_history, num1, num2, expected):
    assert Calculator.subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 15), (10, -5, -50), (0, 10, 0)
])
def test_multiply(clear_history, num1, num2, expected):
    assert Calculator.multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5), (-9, -3, 3), (7, 1, 7)
])
def test_divide(clear_history, num1, num2, expected):
    assert Calculator.divide(num1, num2) == expected

def test_divide_by_zero(clear_history):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(10, 0)

def test_calculation_history(clear_history):
    Calculator.add(2, 3)
    Calculator.multiply(4, 5)
    assert len(Calculations.history) == 2
    assert str(Calculations.get_last_calculation()) == "4 * 5 = 20"

def test_clear_history(clear_history):
    Calculator.subtract(10, 5)
    assert len(Calculations.history) == 1
    Calculations.clear_history()
    assert len(Calculations.history) == 0

