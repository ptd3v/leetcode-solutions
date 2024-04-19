# String ends with? (7th Kyu)
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Solutuion One: Simple
# Takes the text, slices it up to the length of ending, working backwards. Gets the last x letters, from x length and compares.
def solution(text, ending):
    if text.endswith(ending):
        return True
    return False

# Solution Two: Advanced
def solution(text, ending):
    if text[-len(ending):] == ending:
        return True
    return False

# Solution Three: Community
def solution(string, ending):
    return ending in string[-len(ending):]
