from typing import List
from itertools import pairwise, count

"""
    I don't understand why my earlier solutions are faster than my later solutions.
    They get progressively slower, even though I keep trying to make them faster!

    This solution uses a stack, whereas attempts 3 and 4 just use single variables
    and math! I even substitued summing numbers with using mathematical formulas
    in attempt4! Why is it slower?
"""


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        dups = []
        for a, b in pairwise(nums):
            differential = b-a
            if differential == 0:
                dups.append(b)
            else:
                available_nums = range(a+1, b)
                for num in available_nums:
                    if not dups:
                        break
                    moves += num - dups.pop()
        for dup, available_num in zip(dups, count(nums[-1]+1)):
            moves += available_num - dup
        return moves
