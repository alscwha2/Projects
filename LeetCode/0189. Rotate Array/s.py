"""
    O(N) extra space
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tail = nums[-k:]
        head = nums[:len(nums)-k]
        nums[:k] = tail
        nums[k:] = head
