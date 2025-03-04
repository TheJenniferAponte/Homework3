import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Calculator:
    """Calculator class with logging"""

    @staticmethod
    def execute_command(command, a, b):
        logging.info(f"Executing command: {command} with values {a}, {b}")

        if command == "divide":
            if float(b) == 0:
                logging.error("Attempted to divide by zero!")
                raise ValueError("Cannot divide by zero")
            return float(a) / float(b)

        if command == "add":
            return float(a) + float(b)

        if command == "subtract":
            return float(a) - float(b)

        if command == "multiply":
            return float(a) * float(b)

        logging.warning(f"Unknown command: {command}")
        return f"Error: Unknown command '{command}'"
