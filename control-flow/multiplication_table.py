# multiplication_table.py

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):  # Loop through numbers 1 to 10
    result = number * i  # Multiply the user input with the current loop value
    print(f"{number} * {i} = {result}")  # Print the multiplication in the specified format
