"""
    This is the elegant solution that I was looking for. One pass. readable. beautiful.
"""
from typing import List
from itertools import pairwise


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = False, False
        for previous, current in pairwise(nums):
            if current < previous:
                decreasing = True
            elif current > previous:
                increasing = True
            if increasing and decreasing:
                return False
        return True
