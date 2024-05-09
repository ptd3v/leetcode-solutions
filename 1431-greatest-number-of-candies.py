# 1431. Kids With the Greatest Number of Candies
# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies

# Functions Required:

# My Solution:
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        highest = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= highest:
                result.append(True)
            else:
                result.append(False)
        return result
    
# List Comprehension:
def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

# Community Solution:
def kidsWithCandies(self, candies, extraCandies):
    mostCandies = max(candies)
    return map(
        lambda candyAmount: candyAmount + extraCandies >= mostCandies, # These people..
        candies
    )
