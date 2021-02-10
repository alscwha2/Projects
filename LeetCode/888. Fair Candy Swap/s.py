from typing import List
from sys import argv as argv

class Solution:
	def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
		to_transfer = (sum(A) - sum(B))//2
		A.sort(), B.sort()

		i,j = 0,0
		while A[i] - B[j] != to_transfer:
			if A[i] - B[j] < to_transfer:
				i += 1
			else:
				j += 1
		return [A[i],B[j]]

# argv[1]
print(Solution().fairCandySwap([1,1],[2,2]))