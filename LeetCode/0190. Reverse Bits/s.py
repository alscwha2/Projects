from itertools import starmap
from math import floor, log2


class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0

        binary_places = floor(log2(n)) + 1
        binary_array = [0] * 32
        for i in range(binary_places):
            binary_array[32 - binary_places + i], n = divmod(n, 2**(binary_places-i-1))

        return sum(starmap(lambda i, digit: digit*(2**i), enumerate(binary_array)))
