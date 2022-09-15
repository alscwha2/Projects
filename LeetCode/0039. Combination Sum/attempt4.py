from functools import cache
from itertools import product
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @cache
        def combinationSumHelper(target: int) -> set[tuple[int]]:
            combinations = {(target,)} if target in candidates else set()
            for i in range(1, target // 2 + 1):
                for comb_pair in product(combinationSumHelper(i), combinationSumHelper(target - i)):
                    combinations.add(tuple(sorted(comb_pair[0] + comb_pair[1])))
            return combinations

        return list(list(comb) for comb in combinationSumHelper(target))


print(Solution().combinationSum([2, 3, 6, 7], 7))
