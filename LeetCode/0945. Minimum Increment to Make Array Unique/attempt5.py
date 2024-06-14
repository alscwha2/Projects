from itertools import pairwise

"""
    Got this from the editorial... so much simpler
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for i in range(1, len(nums)):
            a, b = nums[i-1], nums[i]
            if b <= a:
                moves += a - b + 1
                nums[i] = a + 1
        return moves

