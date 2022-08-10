"""
A pretty straightforward solution, not particularly clever.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        # get a string of the reversed absolute value
        reversed_string = str(x)[::-1]
        if sign == -1:
            reversed_string = reversed_string[:len(reversed_string)-1]

        # check that it's not too big
        if len(reversed_string) == 10:
            max_string = "2147483648" if sign == -1 else "2147483647"
            for a, b in zip(reversed_string, max_string):
                if a > b:
                    return 0
                if b > a:
                    break
        return sign * int(reversed_string)

print(Solution().reverse(-2147483412))