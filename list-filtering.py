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

# Solution Two: Advanced
def filter_list(l):
    return [intonly for intonly in l if isinstance(intonly, int)]

# Solution Three: Community
def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

