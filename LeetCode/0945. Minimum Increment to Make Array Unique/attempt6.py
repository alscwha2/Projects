from itertools import pairwise

"""
    This assumes that all integers are positive
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freqs = [0] * (max(nums) + len(nums) - 1)
        for num in nums:
            freqs[num] += 1
        moves = 0
        dups = 0
        for i, freq in enumerate(freqs):
            moves += dups
            if freq > 1:
                dups += freq - 1
            elif freq == 0:
                if dups:
                    dups -= 1
        return moves


