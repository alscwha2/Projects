from typing import List
from sys import argv as argv

'''
    this seems like a dp type solution.
    merge and expand as you go along.
    You're only going to have to attempt one merge per iteration because the second merge
        should have already been found by then
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        beginning_of_valid_string = [-1 for _ in range(len(s))]
        for i, char in enumerate(s):
            if char == ')' and i > 0:
                if s[i-1] == '(':
                    beginning_of_valid_string[i] = i-1
                    if i-1 > 0 and beginning_of_valid_string[i-2] != -1:
                        beginning_of_valid_string[i] = beginning_of_valid_string[i-2]
                elif beginning_of_valid_string[i-1] != -1:
                    j = beginning_of_valid_string[i-1] -1
                    if j >= 0 and s[j] == '(':
                        beginning_of_valid_string[i] = j
                        if j > 0 and beginning_of_valid_string[j-1] != -1:
                            beginning_of_valid_string[i] = beginning_of_valid_string[j-1]

        longest = 0
        for end, begin in enumerate(beginning_of_valid_string):
            if begin != -1:
                longest = max(longest, end - begin + 1)
        return longest
