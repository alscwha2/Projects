class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 0, num
        while i <= j:
            k = (i+j) // 2
            difference = num - k * k
            if difference > 0:
                i = k + 1
            elif difference < 0:
                j = k - 1
            else:
                return k
        return False
