from collections import Counter
from math import comb
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(comb(group, 2) for group in Counter(nums).values())
