import pytest
from calculator.calculator import Calculator

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.execute_command('divide', 10, 0)
