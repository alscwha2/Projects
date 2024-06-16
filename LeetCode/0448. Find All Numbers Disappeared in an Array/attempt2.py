from typing import List

"""
    Linear time, constant space (not including return value) as per the challenge.
"""


class Solution:
    def findDisappearedNumbers(self, nums: List [int]) -> List[int]:
        for i in range(len(nums)):
            num = abs(nums[i])
            nums[num-1] = -abs(nums[num-1])
        return [i+1 for i, num in enumerate(nums) if num > 0]
