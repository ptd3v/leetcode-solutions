# Disemvowel Trolls (7th Kyu)
# Your task is to write a function that takes a string and return a new string with all vowels removed.

# Solutuion One: Simple
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in string_:
        if char not in vowels:
            result += char
    return result

# Solution Two: Advanced
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string_ if char not in vowels)


# Solution Three: Community
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
