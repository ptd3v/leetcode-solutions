# Classes and Objects
class Dog:
    def __init__(self):     # Initializes a new Dog instance.
        pass   
    def bark(self):         # Method: Defines what the Dog instance can do.
        print("Woof!")

my_dog = Dog()              # Create an instance of Dog.
my_dog.bark()               # Call the bark method on the instance.

# Data Types
string = "Hello"            # Immutable sequence of characters.
list = [1, 2, 3, 4]         # Mutable sequence of items.
array = [1, 2, 3, 4]        # Similar to list, typically used for numerical operations.
tuple = (1, 2, 3, 4)        # Immutable sequence. Faster than list.
set = {1, 2, 3, 4}          # Unordered collection of unique items.
dict = {'A': 1, 'B': 2}     # Key-value pairs. Mutable.

## Applies function to each item in an iterable and returns..
# A new iterable with the results.
map(str, [1, 2, 3])                 # Converts [1, 2, 3] to ['1', '2', '3']

# A new iterable containing only the items for which the function returns True.
filter(lambda x: x > 1, [1, 2, 3])  # Returns [2, 3]

## String Operations
# String Formatting
Name = "Susan"
Number = 123456789
print("Hello, {}. You are {} years old.".format(Name, Number))  # Old-style formatting.
print(f"Hello, {Name}. You are {Number} years old.")            # F-string formatting.

# String Methods
string = "hello world"
print(string[1:-1])             # Remove the first and last character.
print(string.split())           # Splits string into a list.
print(string.title())           # Capitalizes the first letter of each word.
print(string.capitalize())      # Capitalizes the first letter of the string.

bin(a + b)[2::]                 # Converts the result to Binary, removes the 0b added by bin().

# String Length
stringA = len("Hello")          # Length of a string.
listA = len([1, 2, 3, 4])       # Length of a list.
if stringA >= listA:
    print("Comparing the len()")

# String Concatenation
stringB = "world"
stringC = string + " " + stringB
if len(stringC) > 10:
    print("Too Long")
else:
    print(stringC)

## Lists
# List Operations
list = [1, 2, 3, 4]
print(list[0])          # Access first element.
print(list[-1])         # Access last element.
print(list[-3:])        # Slice the last 3 elements.
list.append(5)          # Add element to the end.
list.remove(5)          # Remove the first occurrence of 5.
list.pop(0)             # Remove element at index 0.
list.insert(0, 0)       # Insert 0 at index 0.
list.sort()             # Sort the list in place.
list.reverse()          # Reverse the list in place.
print(min(1, 9))        # Minimum value.
print(max(1, 9))        # Maximum value.
print(len(list))        # Length of the list.

#### Sets
# Set Operations
set = {1, 2, 3, 4}
set.add(5)              # Add element to the set.
set.remove(5)           # Remove element from the set.
mySet = set([1, 2, 3])  # Convert list to set.
print(len(set))         # Length of the set.

## Dictionaries
# Dictionary Operations
myDict = {"a": 1, "b": 2, "c": 3}
myDict.pop("a")                        # Remove item with key 'a'.
myDict.pop("a", 0)                     # Remove item with key 'a', return 0 if not found.
print(myDict.values())                 # Print dictionary values.
print(list(myDict.values()))           # Convert dictionary values to a list.

# Convert List to Dictionary
def list_to_dictionary(words: list) -> dict:
    new_Dict = {}
    for i, w in enumerate(words):
        new_Dict[w] = i
    return new_Dict

# Count Characters in a String
def count_chars(word: str) -> dict:
    count = {}
    for char in word:
        count[char] = count.get(char, 0) + 1
    return count

## Input and Parsing
# Input
user_input = input("User input here: ")             # Input as string.
user_input_int = int(input("Enter an integer: "))   # Convert input to int.
user_input_float = float(input("Enter a float: "))  # Convert input to float.

# Parsing Strings
s = "The Sky is Blue"
print(' '.join(s.split()[::-1]))  # Reverse words in string.
print(' '.join([''.join(reversed(word)) for word in s.split()][::-1]))  # Reverse characters and words.

#### Error Handling
# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as error:
    print("Error:", error)

## Math Functions
import math
print(math.sqrt(9))             # Square root of 9.
print(math.floor(3.7))          # Floor value of 3.7.
print(math.ceil(3.1))           # Ceil value of 3.1.
print(math.factorial(5))        # Factorial of 5.
print(math.log(100, 10))        # Log base 10 of 100.

# Basic Math Operations
sqrt_n = math.sqrt(9)           # Square root of 9.
pow_n = pow(3, 2)               # 3 squared.
round_value = round(3.14159, 2) # Round to 2 decimal places.

# Math Functions Expand
print(-abs(number))             # Turns a positive integer, negative.    

## Conditional Statements and Loops
# Conditional Statements
x = 15
if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is greater than 10")

# While Loops
i = 0
while i < 5:
    print("Hello")
    i += 1

# For Loops
for i in range(10):        # Prints 0-9.
    print(i)

for i in range(10, 21):   # Print 10 - 20.
    print(i)

for i in range(10, 21, 2): # Print 10 - 20 with step 2.
    print(i)

# Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Loop Control
for i in range(1, 8):
    if i == 3:
        continue   # Skip iteration when i == 3.
    elif i == 6:
        break      # Exit loop when i == 6.
    print(i)

## Functions
# Basic Function
def function_greet():
    print("Hello, I am a function.")

function_greet()  # Call function_greet.

# Function with Parameters
def two_parameters(param1, param2):
    variable = "Hello, " + param1 + param2
    print(variable)

two_parameters("Sherlock", "Holmes")

# Scope Example
def scope_test(n):
    n = n + 1
    print(n)

n = 10
scope_test(n)    # Prints 11.
print(n)        # Prints 10.

# Default Parameters
def default_para(name="default"):
    print("Hello, " + name + "!")

default_para()          # Prints "Hello, default!"
default_para("Steve")   # Prints "Hello, Steve!"

# Type Hints
def bill(balance: int, bill: int) -> int:
    return balance - bill