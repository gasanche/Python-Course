# These are high level exercises to practice what we've learned about Booleans in Python
# Don't worry if you find them challenging at first, take your time to think through the problems
# Remember, programming is all about problem-solving and practice makes perfect!

print("----------- Exercise 1: Medical Check -----------")
# In this exercise, we will classify patients based on their symptoms and risk factors
# You can change these variables to test different scenarios
age = 50
chest_pain = True
respiratory_issues = False
risk_factor = True  # e.g., smoking, obesity, family history
fever = 38  # Celsius
abdominal_pain = False


is_high_risk = (age > 60 or risk_factor) and (chest_pain or respiratory_issues)
is_medium_risk =  (fever >= 39 or abdominal_pain) and not is_high_risk

if is_high_risk:
    print("This patient is classified as HIGH RISK. Immediate medical attention required!")
elif is_medium_risk:
    print("This patient is classified as MEDIUM RISK. Monitor closely and consider further evaluation.")
else:
    print("This patient is classified as LOW RISK. No immediate action required.")


print("\n----------- Exercise 2: Short circuit evaluation -----------")
# We will use 'def' to define a function that simulates a data check
# In this exercise, we want to avoid unnecessary computations if the data is invalid

def data_check(data_list):
    if data_list and data_list[0] and data_list[0] != 0:
        result = 100 / data_list[0]
        print(f"Data check passed. Result: {result}")
    else:
        print("Data check failed. Invalid data.")

# Test cases
data_check([25, 50, 75])  # Valid data
data_check([0, 50, 75])   # First element is zero. Should not attempt division.
data_check([])             # Empty list. Should not attempt to access elements.
data_check(None)           # NoneType. Should not attempt to access elements.


print("\n----------- Exercise 3: Truthiness Cleaner -----------")

user = {
    "name": "", # Empty string is considered False
    "email": "camila@test.com",
    "age": 0,   # Zero is considered False, but is a valid age or not provided? Hmm...
    "preferences": []  # Void list is considered False
        }

# We want to check if the user has provided valid information
# If any of the fields are "falsy", we will prompt the user to complete their profile

if user["name"]:
    print("Name provided")
else:
    print("Name is missing")

if user["preferences"]:
    print("Preferences provided")
else:
    print("Preferences are missing. Void list detected.")

# Now we're goint to check the age. If age is 0, it might be a valid age, like a newborn.
# So it's better to check numbers with 'is not None' to see if the user provided any age at all.
if user["age"] is not None:
    print(f"Age provided: {user['age']}")
