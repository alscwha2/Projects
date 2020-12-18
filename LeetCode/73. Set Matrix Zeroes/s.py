from typing import List
from sys import argv as argv

'''
	O(M*N) Time
	O(M+N) Space
'''

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		m,n = len(matrix),len(matrix[0])
		rows = set()
		columns = set()

		# find all of the rows and columns that are zero
		for row in range(m):
			for column in range(n):
				if matrix[row][column] == 0:
					rows.add(row)
					columns.add(column)

		# zero out all rows
		for row in rows:
			for column in range(n):
				matrix[row][column] = 0

		# only take the non-zero rows and zero out the columns
		rows = [row for row in range(m) if row not in rows]
		for row in rows:
			for column in columns:
				matrix[row][column] = 0


# argv[1]
# print(Solution())
