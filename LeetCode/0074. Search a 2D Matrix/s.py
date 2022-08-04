from typing import List
from sys import argv as argv

'''
	Binary search the columns, then binary search the rows
	O(1) space
	O(logM) + O(logN) time

	if I would just binary search the whole thing by converting coordinates
		then it would be O(log(M*N)) time, and remembering our log identities:
		log(M*N) = log(M) + log(N)
'''

class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		if not matrix or not matrix[0]:
			return False
		# find the right column:
		i,j = 0,len(matrix)-1
		while i <= j:
			k = i + (j-i) // 2
			num = matrix[k][0]
			if num > target:
				j = k-1
			elif num < target:
				i = k+1
			else:
				return True

		if j == -1:
			return False
		row = matrix[j]

		i,j = 0,len(row)-1
		while i <= j:
			k = i + (j-i) // 2
			num = row[k]
			if num > target:
				j = k-1
			elif num < target:
				i = k+1
			else:
				return True
		return False


# argv[1]
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3))