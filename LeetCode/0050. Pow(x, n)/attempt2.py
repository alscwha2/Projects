"""
    This is the better version of the previous answer
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_positive_exponenet = n > 0
        n = abs(n)
        answer = 1
        current = x
        while n > 0:
            if n & 1:
                answer *= current
            n >>= 1
            current *= current
        return answer if is_positive_exponenet else 1/answer
