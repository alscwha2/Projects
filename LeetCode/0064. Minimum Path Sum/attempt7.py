from typing import List
from itertools import product

"""
    This code is a big lie.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        class Grid_Values:
            def __getitem__(self, cell):
                row, column = cell
                return grid[row][column] if -1 not in cell else 200 * m * n

            def __setitem__(self, cell, value):
                row, column = cell
                grid[row][column] = value

        def cell_above(cell):
            row, column = cell
            return (row-1, column)

        def cell_to_the_left(cell):
            row, column = cell
            return (row, column-1)

        value_of = Grid_Values()
        cells_top_left_to_bottom_right = product(range(0, m), range(0, n))
        next(cells_top_left_to_bottom_right) # get rid of (0, 0)
        last_cell = (m-1, n-1)

        for cell in cells_top_left_to_bottom_right:
            value_of[cell] += min(value_of[cell_above(cell)], value_of[cell_to_the_left(cell)])
        return value_of[last_cell]
