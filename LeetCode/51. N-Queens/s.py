from typing import List
from sys import argv as argv

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for i in range(n)]
        queens = []
        for queen in range(n):
        	for column in range(n):

# argv[1]
# print(Solution())
