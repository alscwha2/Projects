"""
    aparently the constant space solution would be:
        reverse the array
        reverse the first k elements
        reverse the rest of the elements.

    now the question is: can you do it with only one pass?
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(nums: List[int], i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums) - 1)
