string = 1,2,3,4
list =  [1, 2, 3, 4]    # Ordered. Changeable. 0 Index. Iterable.
tuple = (1, 2, 3, 4)    # Ordered. Unchangeable. 0 Index. Faster. Iterable.
set =   {1, 2, 3, 4}    # Unordered. Unchangeable (Add/ Remove ONLY). No index. No Duplicates. Iterable.
#set()                  # Empty Set
dict =  {'A':1,'B':2}   # Key: Value

print(list[0])          # List, Tuple.
print(tuple[::-1])      # Start:End:Step
print(1 in set)         # True
print(len(set))         # Length of Set
print(list.index(1))    # Return index location
print(list.count(2))    # Total 2's

string.split()          # String only. Creates list. Hello world = ['Hello', 'world']
string.title()          # String only. Capitalises All Words + Aren'T.
string.capitalize()     # String only. Capitalises All Words only.

list[0] = 1             # Assign new value
list.append(5)
list.remove(5)
list.insert(0, 0)       # Insert 0 at [0]
list.sort()
list.reverse()
list = min(1,9)         # Returns the lower value
list = max(1,9)         # Returns the highest value

# List Comprehension =
listcomp = [x.upper() for x in fruits if x != "apple"]
listcomp = [expression for item in iterable if condition == True]

set.add(5)
set.remove(5)

for x in list:
    print(x)

''.join(sorted((set(a+b))))     # Merge two sets of data, sort and remove duplicate values.