# Python Cheatsheet

print("hello world")

# Variables

# Integers in Python
x = 10
print(x * 2)

# Doubles in Python
y = 20.00
print(y * 3)

# Input Statement
s = input("Enter something please: ")
print(s)

# Else If Statement
x = 4
if x == 5:
    print("Yes")
else:
    print("No")


# Functions
def my_func():
    print("spam")
    print("spam")
    print("spam")


my_func()

# Dictionaries
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# For Loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

# Slicing Lists
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

