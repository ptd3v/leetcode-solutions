# Simple Multiplication - CodeWars (8th Kyu)
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# Example Data
number = 2 # Single data type only

# Solution One:
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
print (simple_multiplication(number))

# Solution Two:
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9 # It is more 'Pythonic' to use (return x if condition else y).
print (simple_multiplication(number))

# Community Solution:
def simple_multiplication(n) :
    return n * (8 + n%2) # Whilst I hate this, it is pretty clever.
# E.g 10 * (8 + 0).
# E.g 11 * (8 + 1).
# E.g 12 * (8 + 0).
# E.g 13 * (8 + 1).
