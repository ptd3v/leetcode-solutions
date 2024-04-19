# Third Angle of a Triangle (8th Kyu)
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd. Note: only positive integers will be tested.

# Solutuion One: Simple
# The total degree of a triangle is 180. Subtract the two other given angles from it.
def other_angle(a, b):
    return 180 - a - b

# Solution Two: Advanced
def other_angle(a, b):
    return 180 - (a + b)

# Solution Three: Community
# As always, there's somebody with a lambda function.
other_angle = lambda a,b: 180 - (a+b)