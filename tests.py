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
