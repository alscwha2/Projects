from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List [int]) -> List[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        totals = {num: min(nums1[num], nums2[num]) for num in nums1 if num in nums2}
        answer = []
        for num, freq in totals.items():
            answer += [num]*freq
        return answer
