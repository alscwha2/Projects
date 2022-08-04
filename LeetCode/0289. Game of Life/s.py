from typing import List
from sys import argv as argv

'''
	This was absolutely infuriating
	The solution was very simple but writing the liveNeighbors function was a debugging nightmare
	
	O(M*N) time - multiple passes through board
	O(1) space

'''

class Solution:
	def gameOfLife(self, board: List[List[int]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		if not board or not board[0]:
			return
		m, n = len(board), len(board[0])

		# get number of live neighbors for cell
		def liveNeighbors(a,b):
			liveneighbors = 0
			if a-1 >= 0:
				if b-1 >= 0 and board[a-1][b-1] > 0:
					liveneighbors += 1
				if board[a-1][b] > 0:
					liveneighbors += 1
				if b+1 < n and board[a-1][b+1] > 0:
					liveneighbors += 1
			if b-1 >= 0 and board[a][b-1] > 0:
				liveneighbors += 1
			if b+1 < n and board[a][b+1] > 0:
				liveneighbors += 1
			if a+1 < m:
				if b-1 >= 0 and board[a+1][b-1] > 0:
					liveneighbors += 1
				if board[a+1][b] > 0:
					liveneighbors += 1
				if b+1 < n and board[a+1][b+1] > 0:
					liveneighbors += 1
			return liveneighbors
		
		# check if cell should live or die
		for i in range(m):
			for j in range(n):
				alive = board[i][j]
				liveneighbors = liveNeighbors(i,j)
				if alive:
					if not 1 < liveneighbors < 4:
						board[i][j] = 2
				else:
					if liveneighbors == 3:
						board[i][j] = -1

		# change value of cells
		for i in range(m):
			for j in range(n):
				if board[i][j] == -1:
					board[i][j] = 1
				elif board[i][j] == 2:
					board[i][j] = 0

print('input')
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
for row in board:
	print(row)

Solution().gameOfLife(board)
print('output')
for row in board:
	print(row)

print('expected')
for row in [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]:
	print(row)



# argv[1]
# print(Solution())
