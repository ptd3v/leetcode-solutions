# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# My Solution:
class Solution(object):
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])

# Community Solution:
class Solution:
    def reverseWords(self, s: str) -> str:
        # Trim the input string to remove leading and trailing spaces
        i, j = 0, len(s) - 1
        while i <= j and s[i] == ' ':
            i += 1  # Find the first non-space character
        while j >= i and s[j] == ' ':
            j -= 1  # Find the last non-space character
        s = s[i : j + 1]  # Extract the trimmed substring

        # Split the trimmed string into words based on spaces
        words = s.split()  # Tokenize the string into words

        # Initialize the output string
        out = []

        # Iterate through the words in reverse order
        for k in range(len(words) - 1, 0, -1):
            # Append the current word and a space to the output
            out.append(words[k])
            # Append the first word to the output (without trailing space)
        out.append(words[0])

        return ' '.join(out)  # Concatenate the reversed words
    