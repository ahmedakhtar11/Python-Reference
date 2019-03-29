		   # Python CheatSheet
		   
print("Python CheatSheet by Ahmed Akhtar!")
print()

			  # Variables

# Strings in Python
print("Strings in Python:")
print('-' * 30)

x = "Hello World"
print(x) #=> Prints Hello World

# Strings in Python (Continued)
name = 'Ahmed'
print('Hello ' + name) 
#=> Prints Hello Ahmed
#Alternatively:
print(f"Hello {name}")
#=> Prints Hello Ahmed

# To Print a new Line
# print('\n') or print()
print() #=> Skips to Next Line

# Integers in Python
print("Integers in Python:")
print('-' * 30)

x = 10
x = "10"
y = int(x)
print(y + 2) #=> Prints 12
print()

# Floats/Doubles in Python
print("Floats/Doubles in Python:")
print('-' * 30)

x = 20.00
x = "20"
y = float(x)
print(y * 2) #=> Prints 40
print()

# Booleans in Python
print("Booleans in Python:")
print('-' * 30)

x = False
x = "false"
y = bool(x)
print(x) #=> Prints False
print()

#Round in Python
print("Rounding in Python:")
print('-' * 30)

print(round(9/4)) #=> Prints 2
# Alternatively, for Division:
print(9//4) #=> Prints 2
print()

# Dictionaries
print("Dictionaries in Python:")
print('-' * 30)
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"]) #=> Prints 24
print(ages["Mary"]) #=> Prints 42
print()

# Lists/Arrays in Python
print("Lists/Arrays in Python:")

# Example of an array of Strings
suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

# Example of an array of Integers
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Splicing Lists
print("Splicing Lists in Python:")
print('-' * 30)

# Count Number of Values in Array
print(len(squares)) #=> Prints 10

# Sum Values in Array
print(sum(squares)) #=> Prints 285

# Minimum of Values in Array
print(min(squares)) #=> Prints 0

# Print Max of Values in Array
print(max(squares)) #=> Prints 81

# Printing Elements of the List
print(squares[2]) #=> Prints 4

# Adding to a List
squares.append(64) #=> Adds 64 to the end

#Prepending or Adding to a location
squares.insert(0, 9) #=> Adds 9 to start

# Print All Even Numbers
print(squares[::2]) 
#=> Prints: [9, 1, 9, 25, 49, 81]

# Print All Values Before the Second Index
print(squares[:2]) #=> Prints [9, 0]

# Print values between the second and fifth index
print(squares[2:5])
#=> Prints [1, 4, 9]

# Print values between the seond and eigth index in increments of 3!
print(squares[2:8:3])
#=> Prints [1, 16]

# Check if value exists
print(4 in squares) #=> Prints True

# Check if value doesn't exist
print(5 not in squares) #=> Prints True

# Print number of instances of value
print(squares.count(4)) #=> Prints 1
print()

# Tuples in Python
# Note: You Cannot Add or Delete Items from a Tuple
print("Tuples in Python:")
print('-' * 30)

this_tuple = ("apple", "banana", "cherry")

# Printing First Index of Tuple
print(this_tuple[1]) #=> Prints 'banana'

# Count Number of Items in the Tuple
print(len(this_tuple)) #=> Prints 3

# Check If Items Exist in Tuple
if "apple" in this_tuple:
	print("Yes, 'apple' is in the fruits tuple") #=> Prints 'Yes, 'apple' is in the fruits tuple'
print()

# Inputs

# name = input("What is you name?")f
# age = input("What is your age?")
# new_patient = input("Are you a new Patient?")
# print(name + " is " + age + " years old and new patient is " + new_patient)
# print(f"The Person's Name is {name}")

# If Statements in Python
print("If statements in Python:")
print('-' * 30)

x = False
y = True

# Standard If, Elif, Else Statment
if x is True:
	print("X is True")
elif x is False:
	print("X is False")
else:
	print("Error")
#=> Prints "X is False"

# Multiple Conditions
if x is False and y is True:
	print("X is False and Y is True")
else:
	print("Error")
#=> Prints "X is False and y is True:"
print()

# For Loops
print("For Loops in Python:")
print('-' * 30)

words = ["dog", "cat", "frog"]
for word in words:
 print(word + "!")
#=> Prints dog! cat! frog!
print()

# While Loop
print("While Loops in Python:")
print('-' * 30)

i = 1
while i < 6:
  print(i)
  i += 1
#=> Prints 1 2 3 4 5
print()

# Functions
print("Functions in Python:")
print('-' * 30)

def my_func():
 print("wow")
 print("wow")
 print("wow")
 
my_func() #=> Prints wow wow wow
print()

# Math Functions
print("Math Functions in Python:")
print('-' * 30)

def add(x, y):
	return x + y
print(add(17, 5)) #=> Returns 22

def subtract(x, y):
	return x - y
print(subtract(10, 5)) #=> Returns 5

def multiply(x, y):
	return x * y
print(multiply(2, 2)) #=> Returns 4
	
def divide(x, y):
	return x / y
print(divide(8, 2)) #=> Returns 4.0
print()

# Useful Functions (Built-In)
print("Useful/Built-In Functions in Python:")
print('-' * 30)

# Join Function
print(", ".join(["bread", "eggs", "potato"]))
#=> prints "bread, eggs, potato"

# Split Function
print("bread, eggs, potato".split(", "))
#=> prints "['bread', 'eggs', 'potato']"

# Replace Function
print("Hello ME".replace("ME", "world"))
#=> prints "Hello world"

# Startwith Function
print("This is a planet.".startswith("This"))
#=> prints "True"

# Endswith Function
print("This is a planet.".endswith("planet."))
#=> prints "True"

# Upper Case Function
print("I am uppercase.".upper())
#=> prints 'I AM UPPERCASE'

#Lower Case Function
print("I AM LOWERCASE".lower())
#=> prints 'i am lowercase'

nums = [88, 77, 77, 66, 22]

if all([i > 5 for i in nums]):
	print("All larger than 5")
#=> prints 'All larger than 5'

if any([i % 2 == 0 for i in nums]):
	print("At least one is even")
#=> prints 'At least one is even'

for v in enumerate(nums):
	print(v)
#=> prints:
# (0, 88)
# (1, 77)
# (2, 77)
# (3, 66)
# (4, 22)
print()

# Classes in Python
print("Classes in Python:")
print('-' * 30)

class Dog:

	def __init__(self, name):
		self.name = name
		self.tricks = []	
# create a new empty list for each dog

	def add_trick(self, trick):
		self.tricks.append(trick)

a = Dog('Bobby')
b = Dog('Buddy')
a.add_trick('catch the ball')
b.add_trick('play fetch')

print(a.tricks)
#=> Prints ['catch the ball']

print(b.tricks) 
#=> Prints ['play fetch']
