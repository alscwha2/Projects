from math import log2, floor


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0 # because log2(0) is illegal

        binary_places = floor(log2(n)) + 1
        binary_array = [0] * binary_places
        for i in range(binary_places):
            binary_array[i], n = divmod(n, 2**(binary_places-i-1))
        return sum(binary_array)
