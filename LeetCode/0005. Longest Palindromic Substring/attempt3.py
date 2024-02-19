"""
    * iterate through string
    * find out how big the center is
    * iterate one step in both directions afterwards until you see how big it is
    * see how big it ends up being
    * compare to length of previous biggest

   This implementation beats the previous one since it doesn't iterate over
   characters that were already included in an extended center.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        current = 0
        while current < len(s):
            char = s[current]

            # figure out how big the center is
            i = j = current
            while j + 1 < len(s) and s[j+1] == char:
                 j += 1

            # set up for next iteration
            current = j + 1

            # go step by step from the center
            while i - 1 >= 0 and j + 1 < len(s) and s[i-1] == s[j+1]:
                i -= 1
                j += 1

            # if this substring is longer, document as longest seen
            if j - i + 1 > len(longest):
                longest = s[i:j+1]

        return longest