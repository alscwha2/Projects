from typing import List
from sys import argv as argv
'''
	Using backtracking. Did an optimization above the solution in the doc so that it doesn't 
		bother computing partial solutions that cannot be completed
'''

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def complete(comb, left, num):
			if left:
				for i in range(num, n+1-(left-1)):
					complete(comb + [i], left-1, i+1)
			else:
				answer.append(comb)
				
		answer = []
		complete([],k,1)
		return answer		


		

# argv[1]
print(Solution().combine(4,3))