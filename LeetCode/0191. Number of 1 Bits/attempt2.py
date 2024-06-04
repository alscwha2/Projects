from math import log2, floor


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0 # because log2(0) is illegal

        total = 0
        for i in range(floor(log2(n)), -1, -1):
            digit, n = divmod(n, 2**i)
            total += digit
        return total
