"""
    linear space
    linear time
"""
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = [False for num in nums]

        longest = 0

        for num in nums:
            if not seen[num]:
                current = 0
                while not seen[num]:
                    seen[num] = True
                    current += 1
                    num = nums[num]
                longest = max(longest, current)

        return longest
