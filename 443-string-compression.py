# 443. String Compression
# Given an array of characters chars, compress it using the algorithm.

# My Solution:
class Solution(object):
    def compress(self, chars):                    
        write = 0                       # Write compressed result
        read = 0                        # Read characters

        while read < len(chars):                                                # 0<10
            char = chars[read]          # Current character                     # a
            count = 0                   # Current count of current charater     # 1

            while read < len(chars) and chars[read] == char:                    # 0<10 and a == a
                read += 1
                count += 1

            chars[write] = char         # Write character                       # a
            write += 1                                                          # 1

            if count > 1:               # Write >1 character
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

# Community Solution:
class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans
  