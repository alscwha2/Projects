"""
    Using stack instead of recursion. Didn't see any difference in performance
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finished = []
        current_iteration = [('', 0, 0)]
        next_iteration = []
        for _ in range(2 * n):
            for combination in current_iteration:
                string, opened, closed = combination
                if opened == n:
                    string = string + ')' * (n - closed)
                    finished.append(string)
                else:
                    next_iteration.append((string + '(', opened + 1, closed))
                    if opened > closed:
                        next_iteration.append((string + ')', opened, closed + 1))
            current_iteration = next_iteration
            next_iteration = []
        return finished



for i in range(6):
    print(Solution().generateParenthesis(i))