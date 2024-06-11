from typing import List
from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        cells = product(range(m), range(n))

        def value(cell):
            row, column = cell
            return board[row][column]

        def neighbors(cell):
            row, column = cell
            other_cells = []
            if row > 0:
                other_cells.append((row-1, column))
            if column > 0:
                other_cells.append((row, column-1))
            if row < m-1:
                other_cells.append((row+1, column))
            if column < n-1:
                other_cells.append((row, column+1))
            return other_cells


        def dfs(cell, word_index, seen):
            if cell in seen:
                return False

            seen.add(cell)

            answer = False
            if word_index == len(word)-1:
                answer = value(cell) == word[-1]
            elif value(cell) == word[word_index]:
                answer = any(dfs(neighbor, word_index+1, seen) for neighbor in neighbors(cell))

            seen.remove(cell)
            return answer

        return any(dfs(cell, 0, set()) for cell in cells)
