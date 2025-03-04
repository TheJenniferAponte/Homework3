import os
import logging
from dotenv import load_dotenv
from calculator.calculator import Calculator

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def repl():
    environment = os.getenv("ENVIRONMENT", "production")
    logging.info(f"Running in {environment} mode")

    print("Welcome to the interactive calculator!")
    print("Commands: add, subtract, multiply, divide, or 'exit' to quit.")
    
    while True:
        command = input("Enter command: ")
        if command == "exit":
            logging.info("User exited the program")
            print("Exiting...")
            break

        try:
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            result = Calculator.execute_command(command, a, b)
            logging.info(f"Calculation result: {result}")
            print(f"Result: {result}")
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
