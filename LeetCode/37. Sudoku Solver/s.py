from typing import List
from sys import argv as argv

'''
	consider using an index PQ
'''

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		possibilities = [[set([i for i in range(1,10)]) for j in range(9)] for k in range(9)]

 
# argv[1]
print(Solution())