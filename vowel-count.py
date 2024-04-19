# Vowel Count (7th Kyu)
# Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y).

# Solutuion One: Simple
def get_count(sentence):
    vowels = 0
    for char in sentence:
        if char in 'aeiou':
            vowels += 1
    return vowels

# Solution Two: Advanced
def getCount(sentence):
    return sum(1 for char in sentence if char in "aeiou")

# Solution Three: Community
def getCount(sentence):
    return sum(char in 'aeiou' for char in sentence)