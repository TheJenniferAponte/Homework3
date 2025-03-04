import os
from dotenv import load_dotenv
from calculator.calculator import Calculator

# Load environment variables
load_dotenv()

def repl():
    environment = os.getenv("ENVIRONMENT", "production")
    print(f"Running in {environment} mode")
    
    print("Welcome to the interactive calculator!")
    print("Commands: add, subtract, multiply, divide, or 'exit' to quit.")
    
    while True:
        command = input("Enter command: ")
        if command == "exit":
            print("Exiting...")
            break

        try:
            a = input("Enter the first number: ")
            b = input("Enter the second number: ")
            result = Calculator.execute_command(command, a, b)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()

