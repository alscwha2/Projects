from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def combinationSumHelper(i, target):
            combinations = []
            for index in range(i, len(candidates)):
                num = candidates[index]
                if index > i and num == candidates[index - 1]:
                    continue
                if num < target:
                    combinations.extend([num] + comb for comb in combinationSumHelper(index + 1, target - num))
                else:
                    if num == target:
                        combinations.append([num])
                    break
            return combinations

        return combinationSumHelper(0, target)




print(Solution().combinationSum2([10,1,2,7,6,1,5],  8))
