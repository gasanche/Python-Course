# As I come from C, I want to understand how memory management works in Python
# In C, we have to manually allocate and free memory using malloc() and free()
# In Python, memory management is handled automatically by the Python Memory Manager


print(" --- Memory Management in Python --- ")

# Python does "Interning" for small integers and some strings
# This means that small integers (usually from -5 to 256) and some strings are stored in a special memory area
# and reused to save memory and improve performance

x = 10
y = 10
z = 257
w = 257

print(f"x: {x}, id(x): {id(x)}")
print(f"y: {y}, id(y): {id(y)}")
# we use id() function to get the memory address of the object

print(f"x and y refer to the same object?\n{x is y}")  # True, because of interning for small integers
# is operator checks if both variables point to the same object in memory
# Dont confuse with == operator which checks for value equality!

print("-" * 40)  # Separator line

print(f"z: {z}, id(z): {id(z)}")
print(f"w: {w}, id(w): {id(w)}")
print(f"z and w refer to the same object?\n{z is w}")  # False, usually no interning for integers > 256

# ------------Important------------
# The behavior for integers > 256 can vary between Python implementations
# and if you run this in an interactive shell vs a script
# If your result is True for z is w, don't be surprised! It's due to optimizations in compiler/interpreter.
# Python sees that both z and w have the same value and optimizes memory usage by pointing them to the same object
# In case you want to force the false behavior, you can use the following trick:
# z = 257
# w = int("257")
# This forces Python to create a new integer object for w
# Now you can print the result of z is w again and it should be False