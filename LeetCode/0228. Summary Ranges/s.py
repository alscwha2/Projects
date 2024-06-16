from typing import List
from itertools import pairwise


class Solution:
    def summaryRanges(self, nums: List[int]) -> List [str]:
        if not nums:
            return ''

        ranges = [[nums[0], nums[0]]]
        for a, b in pairwise(nums):
            if b == a + 1:
                ranges[-1][1] = b
            else:
                ranges.append([b, b])

        ranges = [f'{a}->{b}' if a != b else str(a) for a, b in ranges]
        return ranges


