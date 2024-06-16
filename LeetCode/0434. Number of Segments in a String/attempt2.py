from itertools import accumulate


class Solution:
    def countSegments(self, s: str) -> int:
        return sum(1 if a == ' ' and a != b else 0 for a, b in pairwise(' ' + s))
