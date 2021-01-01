from typing import List
from sys import argv as argv

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		if not numRows:
			return []
		answer = [[1]]
		for i in range(numRows-1):
			prev = answer[-1]
			next = [1]
			i,j = 0,1
			while j < len(prev):
				next.append(prev[i] + prev[j])
				i,j = i+1, j+1
			next.append(1)
			answer.append(next)
		return answer


# argv[1]
# print(Solution())
