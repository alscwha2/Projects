"""
    This is too slow
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i, j = 0, n
        while i <= j:
            k = (i+j) // 2
            three_to_k = 3 ** k
            if three_to_k > n:
                j = k - 1
            elif three_to_k < n:
                i = k + 1
            else:
                return True
        return False
