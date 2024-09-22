# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Draw the pattern using a while loop
while row < size:
    # Print asterisks in one row using a for loop
    for _ in range(size):
        print("*", end="")  # Print asterisk without advancing to the next line
    print()  # Move to the next line after printing one row
    row += 1  # Increment the row counter
