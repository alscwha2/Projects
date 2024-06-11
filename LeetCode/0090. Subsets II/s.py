from typing import List
from itertools import combinations, chain


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List [List[int]]:
        nums.sort()
        powerset = chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))
        subsets = set(powerset)
        return [list(combination) for combination in subsets]
