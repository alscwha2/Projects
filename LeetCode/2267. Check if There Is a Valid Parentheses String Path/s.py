from typing import List
'''
    This code works, but it times out on larger inputs.
    Maybe because I'm doing it recursively?

    Maybe an optimization could be to go from both ends at once.
'''


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        def process(i, j, depth):
            if grid[i][j] == '(':
                depth += 1
            else:
                depth -= 1
            if depth < 0:
                return False
            elif i < m-1 and process(i+1, j, depth):
                return True
            elif j < n-1 and process(i, j+1, depth):
                return True
            elif i == m-1 and j == n-1 and depth == 0:
                return True
            return False
        return process(0, 0, 0)
