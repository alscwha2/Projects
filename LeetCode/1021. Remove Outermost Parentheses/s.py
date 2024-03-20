from typing import List


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = [char for char in s]
        depth = 0
        for i, char in enumerate(answer):
            if char == '(':
                depth += 1
                if depth == 1:
                    answer[i] = ''
            elif char == ')':
                depth -= 1
                if depth == 0:
                    answer[i] = ''
        return ''.join(answer)
