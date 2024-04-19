# Convert boolean values (8th Kyu)
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# Solutuion One: Simple
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

# Solution Two: Advanced
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'

# Solution Three: Community
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
