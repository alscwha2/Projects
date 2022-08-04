from typing import List
from sys import argv as argv

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""

		n = len(matrix)
		# rotating layer by layer
		for i in range(n//2):
			m = n - (2*i)
			for j in range(0, m-1):
				temp = matrix[i][i+j]
				matrix[i][i+j] = matrix[i + (m-1) - j][i]
				matrix[i + (m-1) - j][i] = matrix[i + (m-1)][i + (m-1) - j]
				matrix[i + (m-1)][i + (m-1) - j] = matrix[i+j][i + (m-1)]
				matrix[i+j][i + (m-1)] = temp