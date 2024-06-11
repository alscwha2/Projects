from typing import List
from itertools import product

'''
    Did away with the set and just marked it as seen on the board itself.
    Not an upgrade, just overcomplicates things. Better as a separate data structure.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        cells = product(range(m), range(n))

        def value(cell):
            row, column = cell
            return board[row][column][0]

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

        def mark_seen(cell):
            row, column = cell
            board[row][column] += 'X'

        def is_seen(cell):
            row, column = cell
            return len(board[row][column]) > 1

        def unmark(cell):
            row, column = cell
            board[row][column] = board[row][column][0]

        def dfs(cell, word_index):
            if is_seen(cell):
                return False

            mark_seen(cell)

            answer = False
            if word_index == len(word)-1:
                answer = value(cell) == word[-1]
            elif value(cell) == word[word_index]:
                answer = any(dfs(neighbor, word_index+1) for neighbor in neighbors(cell))

            unmark(cell)
            return answer

        return any(dfs(cell, 0) for cell in cells)
