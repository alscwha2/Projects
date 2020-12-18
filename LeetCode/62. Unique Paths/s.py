from typing import List
from sys import argv as argv

'''
	the answer to this should be 
	((n-1)+(m-1))C(n-1)

	length of path = (n-1) + (m-1)
	number of possible paths = length C (n-1) or length C (m-1)
'''

class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		length = (m-1) + (n-1)

		def nCr(n,r):
			return factorial(n) / (factorial(n-r) * factorial(r))

		return nCr(length, m-1)

		


# argv[1]
# print(Solution())
