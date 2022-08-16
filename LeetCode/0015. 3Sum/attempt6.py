"""
    two_sum with target
    assuming sorted list

"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(target, i):
            pairs = set()
            seen = set()
            for j, num in enumerate(nums[i:]):
                if j > i + 1 and num == nums[j - 2]:
                    continue
                if target - num in seen:
                    pairs.add((num, target - num))
                seen.add(num)
            return [list(pair) for pair in pairs]

        nums = sorted(nums)
        triples = []

        for i, num in enumerate(nums):
            if i and num == nums[i - 1]:
                continue
            for pair in two_sum(-num, i + 1):
                triples.append(pair + [num])
        return triples

print(Solution().threeSum([0,0,0]))