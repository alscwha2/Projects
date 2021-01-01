from typing import List
from sys import argv as argv
'''
	This way you don't need memoization 
'''

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		if k == 1:
			return [[i] for i in range(1,n+1)]
		if k == n:
			return [[i for i in range(1,n+1)]]
		answer = self.combine(n-1,k)
		for comb in self.combine(n-1,k-1):
			comb.append(n)
			answer.append(comb)
		return answer

		

# argv[1]
print(Solution().combine(17,9))