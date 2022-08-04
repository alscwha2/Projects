from typing import List
from sys import argv as argv

'''
	From the solution doc. This is O(N) instead of my solution which was O(logN)
'''

class Solution:
	def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
		to_transfer = (sum(A) - sum(B))//2
		B = set(B)

		for candy_bar in A:
			if candy_bar - to_transfer in B:
				return [candy_bar, candy_bar - to_transfer]

# argv[1]
print(Solution().fairCandySwap([1,1],[2,2]))