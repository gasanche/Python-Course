# Booleans in Python
# Booleans represent one of two values: True or False
# We learned earlier that in Python, True is represented by 1 and False by 0
# So, in this session, we'll explore the operators that yield boolean values

# Operators that return boolean values
print("----------- AND Operator -----------")

age = int(input("Enter your age: ")) # Converting input string to integer
has_id = input("Do you have an ID? (yes/no): ") == 'yes' 
# This will be True if the user types 'yes', otherwise False. ('has_id' will save a boolean variable)

if age >= 18 and has_id:   # Both conditions must be True to print the message
    print("\nYou are allowed to drive. Congrats!")
else:
    print("\nYou are not allowed to drive. Sorry :(") # This will print if at least one condition is False




print("\n----------- OR Operator -----------")
is_student = input("Are you a student? (yes/no): ") == 'yes'
is_senior = age >= 65  # We are reusing the 'age' variable from before
if is_student or is_senior:  # At least one condition must be True to print the message
    print("\nYou are eligible for a discount!")
else:
    print("\nYou are not eligible for a discount...")


print("\n----------- NOT OPERATOR -----------")

is_raining = input("Is it raining? (yes/no): ") == 'yes'
if not is_raining:  # The condition is True if 'is_raining' is False
    print("\nIt's a sunny day! Go touch some grass!")

# What is magical from Python is that you can read these conditions almost like plain English
# "If age is greater than or equal to 18 AND has ID, then print the message"

# IMPORTANT: Python reads conditions with AND and OR operators from left to right
# Why is this important? Because if you have multiple conditions, the order can affect the outcome


print("\n----------- Comparison Operators -----------")
x = 10
y = 5
print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")   # We're checking if x is greater than y
print(f"x < y: {x < y}")   # We're checking if x is less than y
print(f"x == y: {x == y}") # We're checking if x is equal to y
print(f"x != y: {x != y}") # We're checking if x is not equal to y
print(f"x >= y: {x >= y}") # We're checking if x is greater than or equal to y
print(f"x <= y: {x <= y}") # We're checking if x is less than or equal to y


# These operators compare two values and return a boolean result (True or False)