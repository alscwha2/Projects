from typing import List
from sys import argv as argv

class Solution:
	def numDecodings(self, s: str) -> int:
		memo = {len(s):1}
		def helper(i):
			if i in memo:
				return memo[i]
			if s[i] == '0':
				memo[i] = 0
			elif len(s)-i >= 2 and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) <= 6)):
				memo[i] = helper(i+1) + helper(i+2)
			else:
				memo[i] = helper(i+1)
			return memo[i]
		return helper(0)
# argv[1]
print(Solution().numDecodings('0'))
