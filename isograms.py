# Isograms (7th Kyu)
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.

# Solution One
def is_isogram(string):
    isogram = set(string.lower()) # Create new set, make all lowercase.
    if len(string) == len(isogram): # Check if the set is the same as the original.
        return True
    return False

# Solution Two
def is_isogram(string):
    return len(set(string.lower())) == len(string)

# Solution Three: Community
is_isogram = lambda s: len(set(s.lower())) == len(s) # There's always one..