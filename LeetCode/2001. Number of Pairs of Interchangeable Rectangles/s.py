from collections import Counter
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        return sum(group * (group-1) // 2 for group in Counter(width / height for width, height in rectangles).values())
