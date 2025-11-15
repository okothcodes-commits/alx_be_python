# match_case_calculator.py

# Function to perform the calculation
def calculator():
    # Prompt user for the first and second numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for the type of operation
    operation = input("Choose the operation (+, -, *, /): ")

    # Match case statement to handle the operation
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print("Invalid operation. Please choose one of the following: +, -, *, /")

# Call the calculator function
calculator()
