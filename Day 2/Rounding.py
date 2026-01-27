# Here we demonstrate different rounding methods in Python

import math

# Sample numbers to demonstrate rounding methods
number1 = 3.5
number2 = 2.5
number3 = 2.9


# Analyzing number1
print(f"--- Analysing {number1} ---")
print(f"int (Truncates): {int(number1)}")    # Truncates decimal part to 3
print(f"round (Bankers Rounding): {round(number1)}")  # Rounds to nearest even number: 4
print(f"math.floor (Always down): {math.floor(number1)}")  # Always down to 3
print(f"math.ceil (Always up): {math.ceil(number1)}")    # Always up to 4



# Analyzing number2
print(f"\n--- Analysing {number2} ---")
print(f"int (Truncates): {int(number2)}")    # Truncates decimal part to 2
print(f"round (Bankers Rounding): {round(number2)}")  # Rounds to nearest even number: 2
print(f"math.floor (Always down): {math.floor(number2)}")  # Always down to 2
print(f"math.ceil (Always up): {math.ceil(number2)}")    # Always up to 3



# Analyzing number3
print(f"\n--- Analysing {number3} ---")
print(f"int (Truncates): {int(number3)}")    # Truncates decimal part to 2
print(f"round (Bankers Rounding): {round(number3)}")  # Rounds to nearest integer: 3
# Remember: .5 values round to nearest even number. Here it's 2.9, so it goes to 3
print(f"math.floor (Always down): {math.floor(number3)}")  # Always down to 2
print(f"math.ceil (Always up): {math.ceil(number3)}")    # Always up to 3



# Now we're making a comparison table for clarity
print("\nComparison Table:")
print(f"{'Number':<10}{'int()':<10}{'round()':<10}{'math.floor()':<10}{'math.ceil()':<10}")

# We use :<10 to left-align within 10 spaces, <15 for 15 spaces
# If you want to align to the right, use :>10 instead and :^10 for center alignment

print("-" * 40) # Just a separator line

for num in [number1, number2, number3]:
    print(f"{num:<10}{int(num):<10}{round(num):<10}{math.floor(num):<10}{math.ceil(num):<10}")

# How the for loop works:
# It iterates over the list of numbers [3.5, 2.5, 2.9]
# For each number, it prints the number itself and the results of the different rounding methods in a formatted way
# No worries, we'll cover loops in detail later!