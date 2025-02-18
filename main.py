import sys

def calculate(a, b, operation):
    """Performs basic arithmetic operations"""
    try:
        a, b = int(a), int(b)
        if operation == "add":
            return f"The result of {a} add {b} is equal to {a + b}"
        elif operation == "subtract":
            return f"The result of {a} subtract {b} is equal to {a - b}"
        elif operation == "multiply":
            return f"The result of {a} multiply {b} is equal to {a * b}"
        elif operation == "divide":
            if b == 0:
                return "An error occurred: Cannot divide by zero"
            return f"The result of {a} divide {b} is equal to {a / b}"
        else:
            return f"Unknown operation: {operation}"
    except ValueError:
        return f"Invalid number input: {a} or {b} is not a valid number."

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    a, b, operation = sys.argv[1], sys.argv[2], sys.argv[3]
    print(calculate(a, b, operation))
