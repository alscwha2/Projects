from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def neighbors(row, column):
            answer = []
            if row < m-1:
                answer.append((row+1, column))
            if column < n-1:
                answer.append((row, column+1))
            return answer

        def dfs(row, column):
            if grid[row][column] >= 0:
                grid[row][column] = -(grid[row][column] + min((dfs(*neighbor) for neighbor in neighbors(row, column)), default=0))
            return -grid[row][column]

        return dfs(0,0)
