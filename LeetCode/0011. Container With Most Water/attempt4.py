"""
O(NlogN) time, O(N) space
Same as previous solution, using Functional programming
"""

from typing import List
from functools import reduce


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        def expand_bounds(bounds, new):
            left, right = bounds
            if new > right:
                return left, new
            if new < left:
                return new, right
            return bounds

        def reducer(prev, next):
            previous_bounds, maximum = prev
            x, y = next
            current_bounds = expand_bounds(previous_bounds, x)
            maximum = max(maximum, y * (current_bounds[1] - current_bounds[0]))
            return current_bounds, maximum

        ordered_by_height = sorted(enumerate(height), key=lambda x: -x[1])
        starting_bounds = (ordered_by_height[0][0], ordered_by_height[0][0])
        initializer = starting_bounds, 0

        return reduce(reducer, ordered_by_height, initializer)[1]


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
