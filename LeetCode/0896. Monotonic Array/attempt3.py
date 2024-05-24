"""
    another solution from leetcode. This is the clean solution I wanted
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        increasing = decreasing = True

        for i in range(1, len(nums)):
            current, previous = nums[i], nums[i-1]
            if current < previous:
                decreasing = False
            if current > previous:
                increasing = False
            if not decreasing and not increasing:
                return False
        return True
