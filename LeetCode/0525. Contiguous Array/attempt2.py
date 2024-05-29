from typing import List
from itertools import accumulate, starmap
from functools import reduce
"""
    overly complicated functional code
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ups_and_downs = map(lambda x: 1 if x else -1, nums)
        heights = accumulate(ups_and_downs, initial=0)

        seen = {}
        def get_lengths(i, num):
            if num in seen:
                return i - seen[num]
            else:
                seen[num] = i
                return 0

        lengths = starmap(get_lengths, enumerate(heights))
        return reduce(max, lengths, 0)
