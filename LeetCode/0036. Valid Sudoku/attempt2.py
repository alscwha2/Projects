from itertools import chain, product, islice
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(array):
            array = list(filter(lambda a: a != '.', array))
            return len(array) == len(set(array))

        for row in board:
            if not valid(row):
                return False

        for column in zip(*board):
            if not valid(column):
                return False

        for i, j in product((0, 3, 6), repeat=2):
            box = (islice(row, j, j + 3) for row in islice(board, i, i+3))
            if not valid(chain(*box)):
                return False

        return True


print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))