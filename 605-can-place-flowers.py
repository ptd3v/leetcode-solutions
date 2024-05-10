# 605 - Can Place Flowers?
# Given an array of integers, find the one that appears an odd number of times.

# Key Functions: 

# Solution One
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1): # Skip first and last
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

# Community Solution