"""
    someone on LC had this awesome code:

    class Solution:
        def guessNumber(self, n: int) -> int:
            return bisect_left(range(n), 0, key=lambda num: -guess(num))
"""



# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 0, n-1
        while i <= j:
            k = (i+j)//2
            result = guess(k)
            if result == -1:
                j = k - 1
            elif result == 1:
                i = k + 1
            else:
                return k
        return i
