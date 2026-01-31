# Strings in Python
# Demonstrating various string operations and methods

# What is a string?
new_string = "Hello, World!" 
print(f"Original string: {new_string}")
# In python, strings are sequences of characters enclosed in single (' ') or double (" ") quotes
# These are complex objects that come with many built-in methods to manipulate and work with text data

# The indexing of strings starts at 0 which is similiar to other programming languages like C, Java, and JavaScript
# But Python also supports negative indexing, where -1 refers to the last character, -2 to the second last, and so on.

print('\n-------- Indexing --------')

print(new_string[0]) #This is 'H'
print(new_string[-1]) #This is '!'

print('\n-------- Slicing --------')
# String slicing allows us to extract a substring from a string using the syntax [start:end]
new_substring = new_string[0:5] 
# This will get characters from index 0 to 4. The slicing is exclusive of the end index, so 5 is not included.
print(new_substring) #This is 'Hello'

# Slicing can also omit the start or end index to go from the beginning or to the end of the string
print(new_string[:5])  #This is 'Hello'
print(new_string[7:])  #This is 'World!'

# Curiosity: slicing can also include a step value [start:end:step]
every_second_char = new_string[0:13:2]
print(every_second_char) #This is 'Hlo ol!'


# We're going to do some practical exercises with strings
print('\n-------- Practical Exercises --------')
raw_string = "  Price: $49.99  "
print(f"Raw string data: '{raw_string}'")

# We can clean the string step by step or chain the methods together

step_1 = raw_string.strip()  # Remove leading and trailing whitespace ' '
step_2 = step_1.replace("$", "")  # Remove the '$' symbol
clean_string = step_2.lower()  # Convert to lowercase for uniformity

print(f"Cleaned string data: '{clean_string}'")

# Now we're doing the same in one line
chained_clean_string = raw_string.strip().replace("$", "").lower()
print(f"Chained cleaned string data: '{chained_clean_string}'")


print('\n-------- f-Strings and Immutability --------')
# Somethin that you might have noticed is the f-strings that we have been using to print
# f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}
my_name = "Camila"
print(f"Hello, {my_name}! Welcome to this Python Course.")

# You can even do calculations inside the curly braces! That's crazy!
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")


# Okay, something important about strings in Python is that they are immutable
# This means that once a string is created, it cannot be changed.

my_name = "Camila"
# Trying to change the first character will result in an error
# my_name[0] = "c"  # This will raise a TypeError. Delete the '#' to see the error



