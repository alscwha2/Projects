from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(group * (group - 1) // 2 for group in Counter(nums).values())
