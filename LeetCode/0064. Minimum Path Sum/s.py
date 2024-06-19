from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def neighbors(cell):
            row, column = cell
            answer = []
            if row < m-1:
                answer.append((row+1, column))
            if column < n-1:
                answer.append((row, column+1))
            return answer

        def value(cell):
            row, column = cell
            return grid[row][column]

        def dfs(cell):
            if value(cell) >= 0:
                row, column = cell
                grid[row][column] = -(value(cell) + min((dfs(neighbor) for neighbor in neighbors(cell)), default=0))
            return -value(cell)

        return dfs((0,0))
