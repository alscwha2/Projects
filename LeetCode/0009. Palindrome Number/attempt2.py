"""
First one was better
"""

from math import log10, floor

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        digits = floor(log10(x))
        for digit in range(digits, 0, -2):
            l = (x // pow(10, digit) % 10)
            x, r = divmod(x, 10)
            print(l,r,x)
            if l != r:
                return False
        return True


print(Solution().isPalindrome(-121))