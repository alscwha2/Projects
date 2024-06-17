from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(char) for char in reversed(num1)]
        num2 = [int(char) for char in reversed(num2)]
        overflow = 0
        answer = []
        for a, b in zip_longest(num1, num2, fillvalue=0):
            answer.append(a + b + overflow)
            overflow, answer[-1] = divmod(answer[-1], 10)
        if overflow:
            answer.append(overflow)
        return ''.join(str(number) for number in reversed(answer))
