# Descending Order (7th Kyu)
# Make a function that can take any non-negative integer as an argument and return it with its digits in descending order.

# Solution One
def descending_order(num):
    invert = sorted(str(num), reverse = True)
    return int(''.join(invert))

# Solution Two: Advanced
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
