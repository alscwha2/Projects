from typing import List
from sys import argv as argv

'''
	Each level is sum from 0 to n-1 of numTrees(i) * numTree(n-1-i)
'''

class Solution:
	def numTrees(self, n: int) -> int:
		memo = {0:1}

		def helper(n):
			if n in memo:
				return memo[n]
			answer = 0
			for i in range(n):
				answer += helper(i) * helper(n-1-i)
			memo[n] = answer
			return answer

		return helper(n)


# argv[1]
print(Solution().numTrees(3))