from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i, num in enumerate(nums):
            if num:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
