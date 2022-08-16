"""
This is a worse solution because it is O(N**3), as opposed to the others
    which are O(N **2)
"""


from collections import Counter
from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = combinations(nums, 2)
        nums = Counter(nums)
        triples = set()
        for a, b in pairs:
            complement = 0 - a - b
            if complement in nums:
                if complement == a and a == b:
                    if nums[a] < 3:
                        continue
                if complement == a:
                    if nums[a] < 2:
                        continue
                if complement == b:
                    if nums[b] < 2:
                        continue
                triples.add(tuple(sorted((a, b, complement))))
        return [list(t) for t in triples]