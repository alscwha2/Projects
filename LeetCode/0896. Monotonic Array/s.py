"""
    This is the simple solution. not so elegant. 
"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        def is_monotonitcally_increasting(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True

        def is_monotonitcally_decreasing(nums):
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return False
            return True
        
        return is_monotonitcally_decreasing(nums) or is_monotonitcally_increasting(nums)

