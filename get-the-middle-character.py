# Get the Middle Character (7th Kyu)
# Your job is to return the middle character of the word.
# If the word's length is even, return the middle 2 characters.

# Solution One
def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid -1: mid +1]
    else:
        return s[mid]

# Solution Two: Advanced
def get_middle(s):
    mid = len(s) // 2
    return s[mid - 1: mid + 1] if len(s) % 2 == 0 else s[mid]

# Solution Three: Community
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
