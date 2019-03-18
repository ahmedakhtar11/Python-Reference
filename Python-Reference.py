# Python CheatSheet
print("Python CheetSheet!")
print()
# Variables

# Strings in Python
print("Strings in Python")
x = "Hello World"
print(x)
# To Print a new Line
# print('\n')
print()

# Integers in Python
print("Integers in Python")
x = 10
x = "10"
y = int(x)
print(y + 2)
print()

# Floats/Doubles in Python
print("Floats/Doubles in Python")
x = 20.00
x = "20"
y = float(x)
print(y * 2)
print()

# Booleans in Python
print("Booleans in Python")
x = False
x = "false"
y = bool(x)
print(x)
print()

# Dictionaries
print("Dictionaries in Python")
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
print()

# Lists/Arrays in Python (Slicing Lists)
print("Splicing Lists")
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Count Number of Items in Array
print(len(squares))
# Printing Elements of the List
print(squares[2])
# Adding to a List
squares.append(64)
# Print All Even Numbers
print(squares[::2])
# Print All Values Before the Second Index
print(squares[:2])
# Print values between the second and fifth index
print(squares[2:5])
# Print values between the seond and eigth index in increments of 3!
print(squares[2:8:3])
print()

# Tuples in Python
# Note: You Cannot Add or Delete Items from a Tuple
print("Tuples in Python")
this_tuple = ("apple", "banana", "cherry")
# Printing First Index of Tuple
print(this_tuple[1])
# Count Number of Items in the Tuple
print(len(this_tuple))
# Check If Items Exist in Tuple
if "apple" in this_tuple:
    print("Yes, 'apple' is in the fruits tuple")
print()

# Inputs

# name = input("What is you name?")f
# age = input("What is your age?")
# new_patient = input("Are you a new Patient?")
# print(name + " is " + age + " years old and new patient is " + new_patient)
# print(f"The Person's Name is {name}")

# If Statements in Python
print("If statements in Python")
x = False
y = True

# Standard If, Elif, Else Statment
if x is True:
    print("X is True")

elif x is False:
    print("X is False")
else:
    print("Error")
print()

# Multiple Conditions
if x is False + y is True
        print("X is False and Y is True")
    else:
        print("Error")

# For Loops
print("For Loops in Python")
words = ["hello", "world", "spam", "eggs"]
for word in words:
 print(word + "!")
print()

# Functions
print("Functions in Python")
def my_func():
 print("spam")
 print("spam")
 print("spam")

my_func()

print()


