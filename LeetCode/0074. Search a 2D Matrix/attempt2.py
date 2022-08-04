from typing import List
from sys import argv as argv

'''
	I think that the double binary search version runs faster
	I think that that is because it doesn't have to do as much math like // and %
'''

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		if not matrix or not matrix[0]:
			return False
		m,n = len(matrix), len(matrix[0])
		i,j = 0, m*n-1
		while i <= j:
			k = i + (j-i)//2
			num = matrix[k//n][k%n]
			if num > target:
				j = k-1
			elif num < target:
				i = k+1
			else:
				return True
		return False


# argv[1]
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))