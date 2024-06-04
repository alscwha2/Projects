from functools import reduce
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num, count = 0, 1
        return reduce(lambda pair_1, pair_2 : pair_1 if pair_1[count] > pair_2[count] else pair_2, Counter(nums).items())[num]
