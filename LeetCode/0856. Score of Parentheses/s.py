from typing import List


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        opener, closer = '(', ')'
        stack = []
        current = 0
        prev = None
        for char in s:
            if prev == opener and char == closer:
                current += 1
            if prev == opener and char == opener:
                stack.append(current)
                current = 0
            if prev == closer and char == closer:
                current = current * 2 + stack.pop()
            prev = char
        return current

print(Solution().scoreOfParentheses('(()(()))'))
