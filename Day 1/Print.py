#First project: Print "Hello (name)" to the console
print("My first project!")

#With "input" function, we stop the program until the user types something
name = input("Please, enter your name: ")

#Now we print "Hello (name)" to the console
print(f"Hello, {name}! Welcome to the world of programming!")

#What's the f that you see in the print function?
#The "f" before the string indicates that it is a formatted string literal (f-string).
#This allows us to show variables directly inside the string using curly braces {}.
#Another example:

language = "Python"
print(f"This sentence was built with f-string: \n{name}, you are learning {language}!")


# Curious fact: In python, you don't need to write the line break character "\n" to create a new line in the console.
# The print function automatically adds a new line at the end of each call.
# But, if you want a new line in the middle of your text, you can use "\n" as shown above.