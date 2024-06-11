from collections import Counter
"""
    The length check here is an optimization
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
