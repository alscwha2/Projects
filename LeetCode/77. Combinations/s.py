from typing import List
from sys import argv as argv
'''
	used recursion and memoization.
'''

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def memoize(n,k,memo):
			if (n,k) in memo:
				return memo[(n,k)]
			if k == 1:
				return [[i] for i in range(1,n+1)]
			if k == n:
				return [[i for i in range(1,n+1)]]

			answer = []
			for i in range(1, (n+1)-k + 1):
				for rest in memoize(n-i,k-1,memo):
					answer.append([i] + [j+i for j in rest])
			memo[(n,k)] = answer
			return answer

		return memoize(n,k,{})
		

# argv[1]
(Solution().combine(17,9))
