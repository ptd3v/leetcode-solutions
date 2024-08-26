def defaultPara(name="default"):    # Default name will be default
    print("Hello, " + name + "!")

defaultPara()           # Will print default
defaultPara("Steve")    # Will print Steve

# Condition inside if statements do not have their own scope?
if True:                # Will always be True
    message = "Hello, True"

print(message)          # Can execute code in the if statement

def condStat(balance):
    if balance <= 50:
        message2 = "Balance is low"
    print(message2)

condStat(50)
#print(message2)     

def sum_and_difference(a, b):
    return a + b, a - b

sum_and_difference(10,5)            # Works, but doesn't print anything.
print(sum_and_difference(10,5))

def add(a, b):
    return a + b

add(2, 3)                           # Works, but doesn't print anything.

# While Loop
i = 0
while i < 2:
    print("Hello")
    i += 1

# While Loop Count
z = 0
while z < 10:
    print(z)
    z += 1

# For Loops
for i in range(10):     # Prints 0-9. Number-1. 
    print(i)

# Loop Range defined
for i in range(10, 21): # Print 10 - 20. 
    print(i)

# Loop Steps
for i in range(10, 21, 2): # Print 10 - 20. 2 steps.
    print(i)

# Loop Steps Reversed
for i in reversed(range(10, 20)):
    print(i)

# Nested Loops
for i in range(1, 4):       # Runs: 1-3.
    for j in range(1,4):    # Runs: 1,1. 1,2. 1,3. 2,1. 2,2. etc.
        print(i, j)

# Break Loop
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)

# Continue Loops Example
for num in range(10):
    if num % 3 != 0:
        continue  # Skip numbers not divisible by 3
    print(num)  # Only prints numbers divisible by 3

for i in range(1, 8):
    if i == 3:
        continue
    elif i == 6:
        break
    print(i)

stringA = len("Hello")      # Output: 5
listA = len([1, 2, 3, 4])   # Output: 4
if stringA >= listA:
    print("What?")

# Zero Based Indexing
stringB = "Hello"
print(stringB[0])                   # Print the index 0 value
print(stringB[len(stringB) - 1])    # Print the last index value

def count_x(nums: int, x: int) -> int:
    result = 0
    for n in nums:
        if n == x:
            result += 1
    return result

ui = input("User input here: ")
print(ui)

Name = "Susan"
Number = 123456789
print("Hello, {}. You are {} years old.".format(Name, Number))
print("Hello, {}. You are {} years old.".format(Number, Name))
print(f"Hello, {Name}. You are {Number} years old.")

for i in range(len(stringB)):
    print(stringB[i])

for i in stringB:
    print (i)

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
