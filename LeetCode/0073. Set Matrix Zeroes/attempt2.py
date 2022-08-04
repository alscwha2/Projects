from typing import List
from sys import argv as argv

'''
	This is much bigger and messier than it should be
'''

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		m,n = len(matrix),len(matrix[0])
		first_column_is_zero = not matrix[0][0]

		# check if first row is zero
		for cell in matrix[0]:
			if cell == 0:
				matrix[0][0] = 0
				break

		# check if first column is zero
		if not first_column_is_zero:
			for row in range(1,m):
				if matrix[row][0] == 0:
					first_column_is_zero = True
					break

		# check each cell and mark the bad rows and columns
		for row in range(1,m):
			for column in range(1,n):
				if matrix[row][column] == 0:
					matrix[row][0] = 0
					matrix[0][column] = 0

		# zero out all of the columns first so that you can zero out first row next
		for column in range(1,n):
			if matrix[0][column] == 0:
				for i in range(1,m):
					matrix[i][column] = 0

		# zero out all of the rows
		for row in range(0,m):
			row = matrix[row]
			if row[0] == 0:
				for i in range(1,n):
					row[i] = 0

		# zero out first column
		if first_column_is_zero:
			for i in range(m):
				matrix[i][0] = 0


# argv[1]
# print(Solution())
