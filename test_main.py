import pytest
from faker import Faker
from main import calculate

fake = Faker()

@pytest.fixture
def fake_numbers():
    """Generate random numbers for testing"""
    return str(fake.random_int(min=1, max=100)), str(fake.random_int(min=1, max=100))

@pytest.mark.parametrize("a, b, operation, expected_result", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
])
def test_calculator(a, b, operation, expected_result):
    """Test calculator operations"""
    assert calculate(a, b, operation) == expected_result

def test_calculator_with_faker(fake_numbers):
    """Test calculator operations using random numbers"""
    a, b = fake_numbers
    operation = fake.random_element(elements=['add', 'subtract', 'multiply', 'divide'])

    if operation == "add":
        expected_result = f"The result of {a} add {b} is equal to {int(a) + int(b)}"
    elif operation == "subtract":
        expected_result = f"The result of {a} subtract {b} is equal to {int(a) - int(b)}"
    elif operation == "multiply":
        expected_result = f"The result of {a} multiply {b} is equal to {int(a) * int(b)}"
    elif operation == "divide":
        expected_result = f"The result of {a} divide {b} is equal to {int(a) / int(b)}" if int(b) != 0 else "An error occurred: Cannot divide by zero"
    else:
        expected_result = f"Unknown operation: {operation}"

    assert calculate(a, b, operation) == expected_result
