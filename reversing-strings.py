# Reversed Strings - CodeWars (8th Kyu)
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow' and 'word'   =>  'drow'

# Solution 1 - String provided
def solution(string):
    return string[::-1]

# Solution 2 - Custom Strings
my_string = "Hello, world!"
reversed_string = my_string[::-1]
print(reversed_string)

# Both solutions use 'slicing', in the following format: [start-position:end-poition:step-size]
# For example, [1:10:2] = From position 1 to 10, show every second letter.
# In this case, [::-1] = For all position, print 1 step backwards.