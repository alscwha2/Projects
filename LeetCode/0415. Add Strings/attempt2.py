from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        overflow = 0
        answer = []
        for a, b in zip_longest(reversed(num1), reversed(num2), fillvalue=0):
            answer.append(int(a) + int(b) + overflow)
            overflow, answer[-1] = divmod(answer[-1], 10)
        if overflow:
            answer.append(overflow)
        return ''.join(str(number) for number in reversed(answer))
