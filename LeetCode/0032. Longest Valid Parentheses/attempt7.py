from typing import List
from sys import argv as argv

'''
    Cleaned up version of attempt6
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0

        beginning_of_valid_string = [-1 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                # find the index where the '(' should be 
                j = i-1
                if beginning_of_valid_string[j] != -1:
                    j = beginning_of_valid_string[j] - 1

                # if the opener is where we expect it to be
                if j >= 0 and s[j] == '(':
                    # this substring goes until the opener
                    beginning_of_valid_string[i] = j

                    # combine the substring with a previous substring if it exists
                    if j > 0 and beginning_of_valid_string[j-1] != -1:
                        beginning_of_valid_string[i] = beginning_of_valid_string[j-1]


                    longest = max(longest, i - beginning_of_valid_string[i] + 1)
        return longest
