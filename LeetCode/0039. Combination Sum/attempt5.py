"""
    The DP solution is better for bigger arrays where most of the combination
        of the numbers smaller than target are possible.
        ^ I think
    The following solutions is better for smaller arrays - you only have to
        check the candidates that you have, not all of the possible numbers less
        than target.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combine_slice(i, target):
            combinations = []
            for index in range(i, len(candidates)):
                num = candidates[index]
                if num < target:
                    combinations.extend([num] + comb for comb in combine_slice(index, target - num))
                else:
                    if num == target:
                        combinations.append([num])
                    break
            return combinations

        return combine_slice(0, target)




print(Solution().combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
