# Learning variables and different types of data in Python
# We will explore integers, floats, strings, and booleans

# A variable is a name that refers to a value stored in the computer's memory.
# It's a reference to that value, allowing us to use and manipulate it in our code.
# Python is a dynamically typed language, which means we don't need to declare the type of a variable explicitly.
# The type is inferred based on the value assigned to the variable.

# For example, let's create variables of different types:

# Integer
my_age = 25

# Float (decimal number but not accurate like in maths)
# This means that 0.1 + 0.2 is not exactly 0.3 due to how computers represent decimal numbers
my_height = 1.60

# String (text)
my_name = "Camila"
my_surname = 'Sanchez'  # Strings can be defined with single or double quotes

# Boolean (True or False)
# True is represented by 1 and False by 0 in Python
is_student = True
has_graduated = False


# As I already have some experience with C, we're going to make a little program to clean and convert data
# Let's say we receive some data as strings and we need to convert them to the appropriate types

raw_price = " $19.99 "

print(f"Raw price data: '{raw_price}' | Type: {type(raw_price)}")

# 'type' function tells us the type of the variable. Returns <class 'str'> for strings

# Now, let's clean the data by removing spaces and the dollar sign
clean_string = raw_price.strip().replace("$", "")

# .strip() removes leading and trailing whitespace " "
# .replace() replaces occurrences of a substring with another substring

print(f"Cleaned price data: '{clean_string}' | Type: {type(clean_string)}")

# Now we have a string with just the number (19.99), but it's still a string


# Let's convert it to different types with what we call "type casting"

price_float = float(clean_string) # Converting string to float
price_int = int(price_float)  # Converting float to int will truncate the decimal part, so 19.99 becomes 19

# In case we wanted to round instead of truncate, we could use the round() function before converting to int
# price_int = int(round(price_float))

# ----------------Important----------------
# Python uses "bankers rounding", so .5 values are rounded to the nearest even number.
# Example: round(2.5) = 2, round(3.5) = 4. Why? It's a method to reduce cumulative rounding error in repeated calculations.

# For more options, check the file Rounding.py in Day 2 folder

print(f"Price as float: {price_float} | Type: {type(price_float)}")
print(f"Price as int: {price_int} | Type: {type(price_int)}")


# Now we can use these variables in calculations
tax_rate = 0.21  # 21% tax rate
total_price = price_float * (1 + tax_rate)

# I'm gonna format the output to show only 2 decimal places
print(f"Total price with tax: {round(total_price, 2)}")  # round function to limit decimal places


