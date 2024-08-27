#
__init__:       # Gives all instances/ ojects spefic attributes with the class.
__init__(self): # Self allows methods within a class to access and modify the instance's attributes.

# Structure
class Dog:              # Class: The blueprint/ template of an object/ instance (e.g., Dog).
    def bark():         # Method: A function that defines what the instance can do (e.g., bark()).
        print("Woof!")

my_dog = Dog()          # An object/ instance of the Dog class.
my_dog.bark             # Call the bark method on the instance.

# Attributes:   What an object is/ has. Name, age, height.
# Method:       What an object can do. Eat, sleep, breathe.

# Data Types
string = 1,2,3,4        # Immutable.
list =  [1, 2, 3, 4]    # Mutable. 0 Index. Iterable.
tuple = (1, 2, 3, 4)    # Immutable. 0 Index. Iterable. Faster.
set =   {1, 2, 3, 4}    # Immutable (Add/ Remove ONLY). Unordered. No index. No Duplicates. Iterable.
dict =  {'A':1,'B':2}   # Key: Value
dict["C"] = 3           # Add C:3 to the dictionary.
dict = {name: age}      # Create dictionary using parameters.
set()                   # Create and empty set, removes duplicates.

# String Formatting
Name = "Susan"
Number = 123456789
print("Hello, {}. You are {} years old.".format(Name, Number))
print("Hello, {}. You are {} years old.".format(Number, Name))
# F-String Altenative
print(f"Hello, {Name}. You are {Number} years old.")

string.split()          # String only. Creates list. Hello world = ['Hello', 'world']
string.title()          # String only. Capitalises All Words + Aren'T.
string.capitalize()     # String only. Capitalises All Words only.
stringA = len("Hello")  # String Len. Output: 5
listA = len([1, 2, 3, 4]) # Output: 4
if stringA >= listA:
    print("Comparing the len()")

# Zero Based Indexing
stringB = "Hello"
print(stringB[0])                   # Print the index 0 value
print(stringB[len(stringB) - 1])    # Print the last index value

# String Looping
for i in range(len(stringA)):
    print(stringA[i])

# String Concatenation
    stringC = stringA + stringB
    if len(stringC) > 10:
        return "Too Long"
    return stringC

print(list[0])          # List, Tuple.
print(tuple[::-1])      # Start:End:Step
print(1 in set)         # True
print(len(set))         # Length of Set
print(list.index(1))    # Return index location
print(list.count(2))    # Total 2's

# Modulo
%2 == 0:                # Modulo even
%2 != 0:                # Modulo odd

# List Commands
list[0] = 1             # Assign value 1 to index 0.
list[-1]                # Print the last index value.
list[-3:]               # Print the last 3 values of a list.
list.append(5)          # Add for list
set.add(5)              # Add for set
mySet = set(myList)     # Convert a list to set.
list.remove(5)
list.pop(0)             # Removes the element at index 0.
list.insert(0, 0)       # Insert 0 at [0]
list.sort()
list.reverse()
list = min(1,9)         # Returns the lower value
list = max(1,9)         # Returns the highest value
if 2 in list            # Returns boolean True
if 2 not in list        # Returns boolean False

def count_x(nums: int, x: int) -> int:      # List Looping
    result = 0
    for n in nums:
        if n == x:
            result += 1
    return result

# List Comprehension
listcomp = [x.upper() for x in fruits if x != "apple"]
listcomp = [expression for item in iterable if condition == True]

set.add(5)
set.remove(5)

for x in list:
    print(x)
''.join(sorted((set(a+b))))     # Merge two sets of data, sort and remove duplicate values.

while b:                        # is equivalent to while b != 0, the value of b is a boolean.

# Dictionary convert from List      
def list_to_dictionary(words: list) -> dict:
    new_Dict = {}
    for i in range(len(words)):
        w = words[i]
        new_Dict[w] = i
    return new_Dict

# Dictionary Count Charaters
def countChars(word: str) -> Dict:
    count = {}                          # Empty dictionary.
    for char in word:
        if char not in count:           # If char does not exist in count (error), set value to 0.
            count[char] = 0
        count[char]= count[char] + 1    # Then incrememnt it by 1.
    return count

# Dictionary Function
myDict = {"a": 1, "b": 2, "c": 3, }
myDict.pop("a")                         # Removes a from the dictionary
myDict.pop("a", 0)                      # Returns 0 if an error occurs.
myDict.values()                         # Returns dictionary values, mot keys.
list(myDict.values())                   # Convert dictionary values to a list. Output [1, 2, 3]

# Input()
input("User input here: ")              # String by default
int(input("User input here: "))         # Convert input to int
float(input("User input here: "))       # Convert input to float

# Parsing
rev_examples = "The Sky is Blue"
' '.join(s.split()[::-1])                                    # "blue is sky the"
' '.join([''.join(reversed(word)) for word in s.split()][::-1])     # "eulb si yks eht"

# Exception Handling
try:
    result = 10 / 0                   # Will throw an error alone
except:
    print("Error")                    # Will print error message instead.

# Error Catching
try:
    result = 10 / 0                   # Willproduce an error
except ValueError:
    print("Custom error message for Value Error")
except Exception as error:
    print("Error: ", error)           # Will print error message instead, along with the error.




print(float('inf'))  # Outputs: inf (guarantee that any number in the list will be LESS than the initial values)
print(float('-inf')) # Outputs: -inf (guarantee that any number in the list will be MORE than the initial values)
print(float('nan'))  # Outputs: nan (not a number)

print(bool("abc"))              # True. Any non-empty string evaluates to True.
print(bool(0))                  # False.

# Conditional Statements
x = 15
if x < 10:                      # With elif only ONE of these conditions will ever execute.
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

# While Loop Count
z = 0
while z < 10:
    print(z)

# For Loops
for i in range(10):     # Prints 0-9.
    print(i)

# Loop Range defined
for i in range(10, 21): # Print 10 - 20. 
    print(i)

# Loop Steps
for i in range(10, 21, 2): # Print 10 - 20. 2 steps.
    print(i)

# Reverse Loop
for i in reversed(range(10, 20)):
    print(i)

# Nested Loops
for i in range(1, 4):       # Runs: 1-3.
    for j in range(1,4):    # Runs: 1,1. 1,2. 1,3. 2,1. 2,2. etc.
        print(i, j)

# Control Flow
def example():
    if x == x:
        break       # Exit Loop immediately.
        continue    # Skips current iteration, moves to next.
        pass        # Not loop specific. Does nothing, placeholder.

# Pass and Break Loops:
for i in range(1, 8):
    if i == 3:      # Prints 1, 2, 4, 5.
        continue    # If 3, move on, do not process.
    elif i == 6:    # When 6 is reached..
        break       # Break or end the program.
    print(i)

# Functions
def functionGreet():    # Function = Block of reuable code
    print("Hello, I am a function.")

functionGreet()         # Run Greet function

def twoParameters(param1, param2):
    variable = "Hello, " + param1 + param2  # Only strings can be concatenated.
    print(variable)

twoParameters("Sherlock","Holmes") 

#Scope Example
def scopeTest(n):   # Inpendant Function
    n = n + 1       # Global 10 + Local 1
    print(n)        # Print 11

n = 10              # Global variable
scopeTest(n)        # Returns 11
print(n)            # Returns 10

def scopeTest2():
    local_variable = 10
    return

scopeTest2()        # Will return 10
print(scopeTest2)   # Will return an error, cannot access local variables

# Default Parameters
def defaultPara(name="default"):    # Default name will be default
    print("Hello, " + name + "!")

defaultPara()           # Will print default
defaultPara("Steve")    # Will print Steve

# Type hints/ type annotations
def bill(balance: int, bill: int) -> int:
    return balance - bill

def bill(balance, bill):    # Both of these code snippets will run the same.
    return balance - bill

# Return Statement Example
def add_numbers(a, b):      # Returning a value
    return a + b

result = add_numbers(3, 4)
print(result)               # Output: 7

def is_even(number):        # Returning a Computed Value
    return number % 2 == 0

print(is_even(10))          # Output: True
print(is_even(7))           # Output: False

# Program using all of the function used so far:
# Program to determine which Pokémon type is best to use in a battle based on conditions

pokemon_type = "Water"
opponent_type = "Fire"
has_advantage_item = True

if pokemon_type == "Grass" and not has_advantage_item:
    print("Your Grass-type Pokémon might struggle without an advantage item.")
elif (pokemon_type == "Water" and opponent_type == "Fire") or (has_advantage_item and pokemon_type != "Electric"):
    print("Your Water-type Pokémon has a type advantage over the Fire-type opponent!")
else:
    print("You might want to switch Pokémon or use an advantage item.")
