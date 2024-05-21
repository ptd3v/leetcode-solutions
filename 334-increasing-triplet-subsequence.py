# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

# My Solution:
class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf')  # Initialize first and second to positive infinity
        for num in nums:
            if num <= first:
                first = num  # Update first if num is smaller
            elif num <= second:
                second = num  # Update second if num is between first and second
            else:
                return True  # Return true if you find a number larger than both first and second
        return False

# Community Solution:
class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False