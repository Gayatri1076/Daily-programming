# Ask the user for numbers separated by spaces
user_input = input("Enter multiple numbers separated by spaces: ")

# Split the string by spaces and convert each item to a float
numbers = [float(num) for num in user_input.split()]

# Calculate and display the sum
print(f"The sum of entered numbers is: {sum(numbers)}")
