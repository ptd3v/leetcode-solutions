# Mumbling (7th Kyu)
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# Solution One
def accum(st):
    newlist = [] # Open a new list.
    for indx, st in enumerate(st, 1): # Start index at 1, instead of 0.
        newlist.append((st * indx).title()) # Title for first capital. st * index value. E.g C * 3.
    return '-'.join(newlist)

# Solution Three: Community
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s)) # Way too many smart cookies on here.