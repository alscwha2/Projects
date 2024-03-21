from typing import List
'''
    Straightforward. Linear time constant space
'''


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openers_to_add = 0
        closers_needed = 0
        for char in s:
            if char == '(':
                closers_needed += 1
            else:
                if closers_needed == 0:
                    openers_to_add += 1
                else:
                    closers_needed -= 1
        return openers_to_add + closers_needed
