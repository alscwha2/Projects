from typing import List
from sys import argv as argv

'''
	This does not work. [1,6,9],12 will yield 9+1+1+1:4 but the real answer is 6+6:2
'''

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		print(amount)
		coins = sorted(coins)
		dp = {0:0}
		def helper(amount, i):
			if amount in dp:
				return dp[amount]
			if i == -1:
				return -1

			largest = coins[i]
			times, remainder = divmod(amount, largest)
			for _ in range(times+1):
				rest = helper(remainder, i-1)
				if rest != -1:
					print(amount, '==', largest, '*', times, '+', remainder)
					dp[amount] = times + rest
					return dp[amount]
				else:
					print(amount, largest, remainder)
					remainder += largest
					times -= 1
			dp[amount] = -1
			return -1
		answer = helper(amount, len(coins)-1)
		for entry in dp.items():
			print(entry)
		return answer
# argv[1]
print(Solution().coinChange([186,419,83,408],6249))