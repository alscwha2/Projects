class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        if n & (n-1):
            return False

        while n > 1:
            n >>= 2

        return n == 1
