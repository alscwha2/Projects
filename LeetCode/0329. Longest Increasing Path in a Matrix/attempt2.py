from functools import cache
from typing import List

"""
Don't bother constructing an adjacency list. Just figure it out as you go. And 
    cache the path_length function
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        def cells():
            return ((i, j) for i in range(m) for j in range(n))

        def value(cell):
            i, j = cell
            return matrix[i][j]

        def children(cell):
            def within_bounds(coordinates):
                x, y = coordinates
                return (0 <= x < m) and (0 <= y < n)

            i, j = cell
            candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            return [candidate for candidate in candidates if within_bounds(candidate)]

        @cache
        def path_length(cell):
            greater_children = [child for child in children(cell) if value(child) > value(cell)]
            return 1 + max(0, 0, *(path_length(child) for child in greater_children))

        return max(path_length(cell) for cell in cells())


print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))