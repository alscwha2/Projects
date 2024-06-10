from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 if actual != expected else 0 for actual, expected in zip(heights, sorted(heights)))
