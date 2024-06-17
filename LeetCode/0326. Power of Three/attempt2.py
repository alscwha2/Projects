"""
    My approach is O(log2(log3(n)))

    Here are other answers:

    This was in one of the answers. Good idea.

    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            return n > 0 and 3**19 % n == 0


    Also the following code is amazing:

    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            if n <= 0:
                return False
            logValue = log10(n) / log10(3)
            return logValue == int(logValue)
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        three_to_2_to_i = [3]
        while three_to_2_to_i[-1] <= n:
            three_to_2_to_i.append(three_to_2_to_i[-1] ** 2)
        for num in reversed(three_to_2_to_i):
            if num <= n:
                n /= num
        return n == 1
