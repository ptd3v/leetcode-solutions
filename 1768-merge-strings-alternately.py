# Merge Strings Alternately (1768)
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.

# Functions Required: len(), .join(), append(), max(), while loop.

# My Solution:
class Solution(object):
    def mergeAlternately(self, word1, word2):

        merged = ""
        i, j = 0, 0  # Init pointers for word1 and word2    
   
        while i < len(word1) and j < len(word2): # Alternate between word1 and word2
            merged += word1[i] + word2[j]  # Merge characters
            i += 1  # Move pointer forward
            j += 1       
        merged += word1[i:] # Append any remaining characters, string slicing
        merged += word2[j:] 

        return merged  # Return the merged string

# Community Solution:
class Solution(object):
    def mergeAlternately(self, word1, word2):

        merged = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1     

        return ''.join(merged)