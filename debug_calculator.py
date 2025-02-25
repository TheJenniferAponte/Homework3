class Calculator:
    """Minimal calculator for debugging division by zero."""

    @staticmethod
    def execute_command(command, a, b):
        print(f"DEBUG: Command = {command}, a = {a}, b = {b}")  # Debugging output
        if command == "divide":
            if float(b) == 0:
                print("DEBUG: Raising ValueError for division by zero")
                raise ValueError("Cannot divide by zero")
            return float(a) / float(b)
        return f"Error: Unknown command '{command}'"

# Manual test
if __name__ == "__main__":
    try:
        Calculator.execute_command('divide', 10, 0)
    except ValueError as e:
        print(f"Caught Exception: {e}")
