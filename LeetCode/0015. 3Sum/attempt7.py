"""
    got the better version of two_sum from the first time
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(target, i):
            pairs = set()
            j = len(nums) - 1
            while i < j:
                difference = target - nums[i] - nums[j]
                if not difference:
                    pairs.add((nums[i], nums[j]))
                if difference >= 0:
                    i += 1
                elif difference <= 0:
                    j -= 1

            return [list(pair) for pair in pairs]


        nums = sorted(nums)
        triples = []

        for i, num in enumerate(nums):
            if i and num == nums[i - 1]:
                continue
            for pair in two_sum(-num, i + 1):
                triples.append(pair + [num])
        return triples

print(Solution().threeSum([-1,0,1,2,-1,-4]))