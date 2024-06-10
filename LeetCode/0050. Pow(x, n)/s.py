from typing import List
from sys import argv as argv
from math import log2, floor

"""
    The straightforward solution is O(N), which is too slow.
    This solution is O(LogN)
    We are going to take advantage of the fact that if you continually square
        a number it grows exponentially, as opposed to constantly multiplying it
        by the original number
        x*x*x*x*x*x*x*x*x*x*x*x*x*x*x*x == (((total=x * total) * total) * total) * total

    Any number can be expressed as a sum of powers of 2
        (which is basically just the binary representation of the number)
    We can express the power (n) as a sum of powers of two


    Also, addition of exponents distributes to multiplication

    answer = 1
    total_x_power_of_two = x
    for each power of two:
        if that power of two is in the n-sum:
            answer *= total_x_power_of_two
        total_x_power_of_two *= total_x_power_of_two
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def base_10_to_binary_array(n):
            if n == 0:
                return [0]
            powers = floor(log2(n))
            bit_array = [0] * (powers + 1)
            power_2 = 1
            for _ in range(powers):
                power_2 *= 2
            for i in range(powers, -1, -1):
                bit_array[powers - i], n = divmod(n, power_2)
                power_2 = power_2 // 2
            return bit_array

        if n == 0:
            return 1
        sign = -1 if n < 0 else 1
        n = abs(n) # taking this liberty because no one said I have to worry about overflow
        answer = 1

        bit_array = base_10_to_binary_array(n)
        current = x
        for bit in reversed(bit_array):
            if bit:
                answer *= current
            current *= current
        return answer if sign == 1 else 1/answer

# argv[1]
# print(Solution())
