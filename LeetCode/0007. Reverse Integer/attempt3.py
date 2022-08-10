"""
A pretty straightforward solution, not particularly clever.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign, bound, reversed_abs_string = \
            (-1, "2147483648", str(x)[:0:-1]) if x < 0 else\
            (1, "2147483647", str(x)[::-1])
        if (x > 1000000000 or x < -1000000000) and reversed_abs_string > bound:
            return 0
        return sign * int(reversed_abs_string)

print(Solution().reverse(123))