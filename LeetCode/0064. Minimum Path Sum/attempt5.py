from typing import List
from itertools import product


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def cell_above(cell):
            row, column = cell
            return (row-1, column)

        def cell_to_the_left(cell):
            row, column = cell
            return (row, column-1)

        def value(cell):
            row, column = cell
            return grid[row][column]

        def add_value(cell, val):
            row, column = cell
            grid[row][column] += val

        first_row = ((0, i) for i in range(1, n))
        first_column = ((j, 0) for j in range(1, m))
        cells = product(range(1, m), range(1, n))
        last_cell = (m-1, n-1)

        for cell in first_row:
            add_value(cell, value(cell_to_the_left(cell)))
        for cell in first_column:
            add_value(cell, value(cell_above(cell)))
        for cell in cells:
            add_value(cell, min(value(cell_above(cell)), value(cell_to_the_left(cell))))
        return value(last_cell)
