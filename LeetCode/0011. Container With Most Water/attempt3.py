"""
O(NlogN) time, O(N) space
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        ordered = sorted(enumerate(height), key=lambda x: -x[1])
        leftmost = rightmost = ordered[0][0]
        maximum = 0
        for x, y in ordered:
            domain = max(abs(x - leftmost), abs(x - rightmost))
            maximum = max(maximum, y * domain)
            leftmost = min(leftmost, x)
            rightmost = max(rightmost, x)

        return maximum


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
