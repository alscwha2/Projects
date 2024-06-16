class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n >= 1 and not n & (n-1) and not n & 0b10101010101010101010101010101010
