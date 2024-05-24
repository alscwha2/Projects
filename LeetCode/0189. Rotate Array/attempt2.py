"""
    O(k) extra space (except it's not<F7> because the slice in line 14 actually
        makes a copy)
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tail = nums[-k:]
        nums[k:] = nums[:len(nums)-k]
        nums[:k] = tail
