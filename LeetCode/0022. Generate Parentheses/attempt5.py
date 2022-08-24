"""
    Good, but has a lot of function calls
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.finish_parenthesis(0, 0, n)

    def finish_parenthesis(self, opened, closed, n):
        if opened + closed == n:
            return [')' * opened]

        combinations = []
        if opened > 0:
            for rest in self.finish_parenthesis(opened-1, closed+1, n):
                combinations.append(')' + rest)
        for rest in self.finish_parenthesis(opened+1, closed, n):
            combinations.append('(' + rest)
        return combinations

for i in range(6):
    print(Solution().generateParenthesis(i))