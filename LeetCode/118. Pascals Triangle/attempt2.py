from typing import List
from sys import argv as argv
from math import factorial

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:

		def combinations(n,r):
			return factorial(n)//(factorial(n-r) * factorial(r))

		answer = []
		for i in range(0, numRows):
			next = []
			for j in range(0, i+1):
				next.append(combinations(i,j))
			answer.append(next)
		return answer

# argv[1]
print(Solution().generate(3))
