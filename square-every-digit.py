# Square Every Digit (7th Kyu)
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Solution One
def square_digits(num):
    nums = str(num)  # Convert num to a string
    result = ''      # Initialize an empty string to store the squared digits
    for x in nums:   # Iterate over each character in the string representation of num
        result += str(int(x) ** 2)  # Square the digit, convert it back to a string, and append it to the result
    return int(result)  # Convert the concatenated string of squared digits back to an integer and return it

# Solution Two: Advanced
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

# Solution Three: Community
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
