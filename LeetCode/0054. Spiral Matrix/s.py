from typing import List
from sys import argv as argv

'''
	Because of the way that I defined the layers it wouldn't work for an
		innermost 1xn row or column, so I had to treat that case separately
'''

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		order = []
		m = len(matrix[0])
		n = len(matrix)

		# read each outer layer clockwise
		for layer in range(min(m,n) // 2):
			horizontalLength = m - 2*layer - 1
			verticalLength = n - 2*layer - 1

			for i in range(horizontalLength):                       # ---------->
				order.append(matrix[layer][layer+i])
			
			for i in range(verticalLength):                         #			|
				order.append(matrix[layer+i][(m-1)-layer])          #			|
																	# 			|
																	# 			V
			
			for i in range(horizontalLength):						# <----------
				order.append(matrix[(n-1)-layer][(m-1)-layer-i])
			
																	# ^
			for i in range(verticalLength):							# |
				order.append(matrix[(n-1)-layer-i][layer])			# |
																	# |
		# to deal with the innermost row or column, if it exists
		if min(m,n)%2 == 1:
			if m <= n:
				column = m//2
				for i in range(n-(m-1)):
					order.append(matrix[column+i][column])
			else:
				row = n//2
				for i in range(m-(n-1)):
					order.append(matrix[row][row+i])

		return order

		

# argv[1]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in matrix:
	print(i)
print(Solution().spiralOrder(matrix))
