"""
    Someone on leetcode had the following idea. Though it takes longer and more space.
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return sorted(nums) == nums or sorted(nums, reverse=True) == nums
