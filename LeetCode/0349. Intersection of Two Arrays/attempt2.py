from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        return[num for num in nums1 if num in nums2]
