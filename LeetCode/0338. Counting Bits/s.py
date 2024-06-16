from typing import List
"""
    There is no way that this is what they wanted fromm me.
"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i)[2:].count('1') for i in range(n+1)]
