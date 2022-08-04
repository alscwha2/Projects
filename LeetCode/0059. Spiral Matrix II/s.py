from typing import List
from sys import argv as argv

class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		matrix = [[0 for i in range(n)] for j in range(n)]
		

		# iterate through each of the outer layers:
		d = 1 # <-- you'll see why we need this later
		for i in range(n//2):
			# divide each layer into 4 identical rectangles 
			# - - - -|
			# |	     |
			# |	     |
			# |	     |
			# |- - - - 
			rectangle_length = n-(2*i)-1

			# figure out which value to put into the beginning of each rectangle
			a = d
			b = a + rectangle_length
			c = b + rectangle_length
			d = c + rectangle_length

			# for each recangle iterate through, incrementing the value for each cell
			for numbercell in range(rectangle_length):
				beginning = i
				end = (n-1)-i
				moving_forward = beginning + numbercell
				moving_backward = end - numbercell

				matrix[beginning][moving_forward] = a
				matrix[moving_forward][end] = b
				matrix[end][moving_backward] = c
				matrix[moving_backward][beginning] = d
				
				a,b,c,d = a+1,b+1,c+1,d+1

		# if n is odd then we couldn't reach the center of the matrix with the rectangle method
		# assign the center directly
		if n%2:
			matrix[n//2][n//2] = d

		return matrix



# argv[1]
matrix = Solution().generateMatrix(5)
for row in matrix:
	print(row)