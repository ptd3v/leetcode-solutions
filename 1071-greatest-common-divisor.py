# Greatest Common Divisor of Strings (1071)
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Functions Required: 

# My Solution:
class Solution:
    def gcdOfStrings(self, str1, str2):
        # Check if the concatenation of the two strings in different orders results in the same string.
        if str1 + str2 != str2 + str1:
            return '' # If not, there is no common divisor string, so return an empty string.    
          
        len_gcd = self.gcd(len(str1), len(str2)) # Find the gcd of the lengths of the two strings - ???       
        return str1[:len_gcd] # Return the substring from 0 to len_gcd from the first string, which is the greatest common divisor string.
    
    def gcd(self, a, b): # Helper function to calculate the greatest common divisor
        while b:
            a, b = b, a % b
        return a

# Community Solution
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1) == len(str2):
            return str1
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])

# Hints
# If concatenating str1 and str2 is not equal to concatenating str2 and str1, then there's no common divisor possible. So, we return an empty string "".
# If the lengths of str1 and str2 are equal, and the concatenated strings are equal, then str1 (or str2) itself is the greatest common divisor, and we return str1 (or str2).
# If the length of str1 is greater than the length of str2, it means that str1 contains str2 as a prefix. In this case, we recurse with the substring of str1 after removing (slicing) the prefix that matches str2.
# If the length of str2 is greater than the length of str1, it means that str2 contains str1 as a prefix. In this case, we recurse with the substring of str2 after removing (slicing) the prefix that matches str1.