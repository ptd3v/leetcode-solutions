# A square of squares (7th Kyu)
# Given an integral number, determine if it's a square number.

# Solution One
def is_square(n):
    return n >= 0 and int(n ** 0.5) ** 2 == n

# Solution Two: Advanced
import math
def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

# Solution Three: Community
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0 # Modulo usage, smort.