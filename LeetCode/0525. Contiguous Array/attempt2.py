from typing import List
from itertools import accumulate, starmap
from functools import reduce
"""
    overly complicated functional code
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        heights = list(accumulate((num if num == 1 else -1 for num in nums), initial=0))
        def get_lengths(i, num):
            seen = {}
            if num in seen:
                return i - seen[num]
            else:
                seen[num] = i
                return 0
        lengths = starmap(get_lengths, enumerate(heights))
        return reduce(max, lengths, 0)
