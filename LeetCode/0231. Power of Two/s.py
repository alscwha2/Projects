from math import log2

"""
    You can use bitwise as well, but that is dependant on the integer encoding
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and log2(n) % 1 == 0
