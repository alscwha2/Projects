from itertools import product
from typing import List

'''
'''

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		for i, j in product(range(9), repeat=2):
			if board[i, j] == '.':
				board[i,j] = [num for num in range(9)]

print(Solution())