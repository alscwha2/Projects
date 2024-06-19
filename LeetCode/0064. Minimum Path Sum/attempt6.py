from typing import List
from itertools import product


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        class Grid_Values:
            def __getitem__(self, cell):
                row, column = cell
                return grid[row][column]

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
        first_row_left_to_right = ((0, i) for i in range(1, n))
        first_column_top_to_bottom = ((j, 0) for j in range(1, m))
        cells_top_left_to_bottom_right = product(range(1, m), range(1, n))
        last_cell = (m-1, n-1)

        for cell in first_row_left_to_right:
            value_of[cell] += value_of[cell_to_the_left(cell)]
        for cell in first_column_top_to_bottom:
            value_of[cell] += value_of[cell_above(cell)]
        for cell in cells_top_left_to_bottom_right:
            value_of[cell] += min(value_of[cell_above(cell)], value_of[cell_to_the_left(cell)])
        return value_of[last_cell]
