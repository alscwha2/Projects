"""
A pretty straightforward solution, not particularly clever.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign, bound = (-1, "2147483648") if x < 0 else (1, "2147483647")
        reversed_abs_string = str(x)[::-1] if x >= 0 else str(x)[:0:-1]
        if x > 1000000000 or x < -1000000000:
            for a, b in zip(reversed_abs_string, bound):
                if a > b:
                    return 0
                if b > a:
                    break
        return sign * int(reversed_abs_string)

print(Solution().reverse(-123))