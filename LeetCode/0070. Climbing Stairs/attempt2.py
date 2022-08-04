from typing import List
from sys import argv as argv

'''
	Recursion with Memoization
'''

class Solution:
	def climbStairs(self, n: int) -> int:
		dp = [0 for i in range(n+1)]
		def climb_backwards(n):
			if dp[n]:
				return dp[n]
			if n == 1 or n == 2:
				return n
			dp[n] = climb_backwards(n-1) + climb_backwards(n-2)
			return dp[n]
		return climb_backwards(n)
		


		

# argv[1]
print(Solution().climbStairs(2))