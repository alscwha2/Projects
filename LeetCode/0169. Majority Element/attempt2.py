from functools import reduce
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        num, count = 0, 1
        def higher_count(pair_1, pair_2):
            return pair_1 if pair_1[count] > pair_2[count] else pair_2
        return reduce(higher_count, counter.items())[num]
