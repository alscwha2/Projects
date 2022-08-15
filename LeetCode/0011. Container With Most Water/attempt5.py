"""
O(NlogN) time, O(N) space
Same as previous solution, using Functional with side effects
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

        def reducer(bounds, next):
            nonlocal maximum
            x, y = next
            bounds = expand_bounds(bounds, x)
            maximum = max(maximum, y * (bounds[1] - bounds[0]))
            return bounds

        maximum = 0
        ordered = sorted(enumerate(height), key=lambda x: -x[1])
        initializer = (ordered[0][0], ordered[0][0])
        reduce(reducer, ordered, initializer)

        return maximum


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
