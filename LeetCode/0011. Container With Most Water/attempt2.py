"""
O(N ** 2) time, O(N) space. Does not pass the Leetcode test
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        possible_left_boundaries = {}
        tallest_seen = 0
        for x, y in enumerate(height):
            if y > tallest_seen:
                tallest_seen = y
            possible_left_boundaries[x] = y
            for i, j in possible_left_boundaries.items():
                maximum = max(maximum, min(j, y) * (x - i))
        return maximum

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))