# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the size is positive
if size <= 0:
    print("Please enter a positive integer for the size.")
else:
    # Initialize a counter for the rows
    row = 0
    
    # Use a while loop to iterate through each row
    while row < size:
        # Inside the while loop, use a for loop to print asterisks for each column
        for column in range(size):
            print("*", end="")  # Print asterisk without moving to a new line
        print()  # Move to the next line after printing a row of asterisks
        row += 1  # Increment the row counter
