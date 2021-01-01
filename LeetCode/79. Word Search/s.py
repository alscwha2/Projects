from typing import List
from sys import argv as argv

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		if not word:
			return True
		if not board or not board[0]:
			return False

		m,n = len(board), len(board[0])
		neighbors = [(-1,0),(0,1),(1,0),(0,-1)]


		for i in range(m):
			for j in range(n):
				if board[i][j] == word[0]:
					curr,end = 1,len(word)
					while curr < end:
						

					





# argv[1]
# print(Solution())
