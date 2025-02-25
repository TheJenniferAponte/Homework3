import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8), (10, -5, 5), (0, 0, 0)
])
def test_add(num1, num2, expected):
    assert Calculator.execute_command('add', num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2), (10, -5, 15), (0, 0, 0)
])
def test_subtract(num1, num2, expected):
    assert Calculator.execute_command('subtract', num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 15), (10, -5, -50), (0, 10, 0)
])
def test_multiply(num1, num2, expected):
    assert Calculator.execute_command('multiply', num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5), (-9, -3, 3), (7, 1, 7)
])
def test_divide(num1, num2, expected):
    assert Calculator.execute_command('divide', num1, num2) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.execute_command('divide', 10, 0)
