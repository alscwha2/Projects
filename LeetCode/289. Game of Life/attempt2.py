from typing import List
from sys import argv as argv

'''
	trying to fix the madness...
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
		neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
		def liveNeighbors(i,j):
			liveneighbors = 0
			for neighbor in neighbors:
				a,b = i+neighbor[0], j+neighbor[1]
				if a >= 0 and b >= 0 and a < m and b < n and board[a][b] > 0:
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
