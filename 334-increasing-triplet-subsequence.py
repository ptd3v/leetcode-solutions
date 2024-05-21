# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

# My Solution:
class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')                   # Initialize first and second to positive infinity
        for num in nums:
            if num <= first:
                first = num                             # Update first if num is smaller
            elif num <= second:
                second = num                            # Update second if num is between first and second
            else:
                return True                             # Return true if you find a number larger than both first and second
        return False

# Community Solution:
class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)                                   # Get the length of the input list
        for i in range(n - 2):                          # Iterate through the list until the third to last element
            for j in range(i + 1, n - 1):               # Iterate through elements after the current element
                for k in range(j + 1, n):               # Iterate through elements after the next element
                    if nums[i] < nums[j] < nums[k]:     # Check if there is an increasing triplet
                        return True                     # Return True if an increasing triplet is found
        return False                                    # Return False if no increasing triplet is found