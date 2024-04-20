# List Filtering (7th Kyu)
# Create a function that takes a list of non-negative integers and strings.
# Returns a new list with the strings filtered out.

# Solutuion One: Simple
def filter_list(l):
    new_list = []
    for item in l:
        if type(item) == int:
            new_list.append(item)
    return new_list

def filter_list(l):
    return [item for item in l if isinstance(item, int)]

# Solution Two: Advanced


# Solution Three: Community

