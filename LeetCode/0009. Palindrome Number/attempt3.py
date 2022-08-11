"""
first one is still better
"""

from math import log10, floor


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return not x

        def get_digit(place):
            return (x // (10 ** place)) % 10

        length = floor(log10(x))
        for left_place in range(length, length // 2, -1):
            if get_digit(left_place) != get_digit(length - left_place):
                return False
        return True


print(Solution().isPalindrome(10))
