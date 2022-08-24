"""
    Modifying attempt5 to be cleaner using side-effects. Much cleaner
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        def finish_parenthesis(string, opened, closed):
            if opened + closed == n:
                combinations.append(string + (')' * opened))
                return

            if opened > 0:
                finish_parenthesis(string + ')', opened - 1, closed + 1)

            finish_parenthesis(string + '(', opened + 1, closed)

        finish_parenthesis('', 0, 0)
        return combinations


for i in range(6):
    print(Solution().generateParenthesis(i))