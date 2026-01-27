#Exercise 2: Basic Arithmetic Operations
#This program performs basic arithmetic operations on two variables
#and prints the results to the console.

#First, we define two variables with numerical values
a = 10
b = 3

#Now, we perform basic arithmetic operations
print(f"The sum of {a} and {b} is: {a + b}")          # Addition
print(f"The difference when {b} is subtracted from {a} is: {a - b}")  # Subtraction
print(f"The product of {a} and {b} is: {a * b}")       # Multiplication

#Important: In Python, we have 2 types of division
print(f"The decimal division of {a} by {b} is: {a / b}")        #Division with decimals (3.3333....)
print(f"The integer division of {a} by {b} is: {a // b}")       #Cuts the decimal part (3)

#Modulus operation gives the remainder of the division
#10 divided by 3 is 3 with a remainder of 1
print(f"The remainder of the division of {a} by {b} is: {a % b}")  # Modulus %


#Now I'll try to make the program ask for user input
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print(f"The sum of {a} and {b} is: {a + b}")          # Addition
print(f"The difference when {b} is subtracted from {a} is: {a - b}")  # Subtraction
print(f"The product of {a} and {b} is: {a * b}")       # Multiplication
print(f"The decimal division of {a} by {b} is: {a / b}")        #Division with decimals (3.3333....)
print(f"The integer division of {a} by {b} is: {a // b}")       #Cuts the decimal part (3)
print(f"The remainder of the division of {a} by {b} is: {a % b}")  # Modulus %