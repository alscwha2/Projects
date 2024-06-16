from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1), set(nums2)
        if len(nums1) > len(nums2): # got this from the editorial - small optimization
            nums1, nums2 = nums2, nums1
        return[num for num in nums1 if num in nums2]
