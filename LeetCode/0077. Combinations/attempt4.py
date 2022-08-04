from typing import List
from sys import argv as argv
from collections import deque
'''
	Used the solution doc optimization of appending and popping to the comb and then only 
		copying it when its finished
	Also took out 'left' parameter because it's only really used once so you could compute it on the fly
'''

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def complete(comb=deque(), next=1):
			if len(comb) == k:
				answer.append(list(comb))
			else:
				for i in range(next, n+1-(k-len(comb)-1)):
					comb.append(i)
					complete(comb, i+1)
					comb.pop()

		answer = []
		complete()
		return answer	


		

# argv[1]
print(Solution().combine(4,3))