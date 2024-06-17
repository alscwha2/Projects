"""
    It is silly that I needed to be fed this one. This is just the easy way of
        doing what I did in the first attempt.
"""
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >1:
            if n % 3 == 2:
                return False
            n //= 3
        return True
