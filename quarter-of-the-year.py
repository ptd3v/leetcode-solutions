# Quarter of the year: CodeWars (8th Kyu)
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Solution One (Simple):
def quarter(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    else:
        return 4

# Solution Two (Advanced):
def quarter_of(month):
    return (month -1) // 3 + 1
# Because Python rounds down by default, we need to remove and then add 1.
# 3 // 3 = 0 whereas 3-1 // 3 + 1 = 1.

# Community Solution:
from math import ceil
def quarter_of(month):
    return ceil(month / 3)
# The ceil function from the math package rounds up instead, removing the need for extra math.