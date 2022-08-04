from typing import List
from sys import argv as argv

'''
	mathematical solution
'''

class Solution:
	def getRow(self, rowIndex: int) -> List[int]:
		def combinations(n,r):
			return factorial(n) // (factorial(n-r) * factorial(r))
		return [combinations(rowIndex,i) for i in range(rowIndex+1)]


# argv[1]
# print(Solution())
