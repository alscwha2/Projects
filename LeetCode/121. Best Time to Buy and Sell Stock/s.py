from typing import List
from sys import argv as argv

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if not prices:
			return 0
		profit = 0
		lowest = highest = prices[0]
		for num in prices:
			if num > highest:
				highest = num
				profit = max(profit, highest-lowest)
			elif num < lowest:
				lowest = highest = num
		return profit

# argv[1]
print(Solution().maxProfit([7,1,5,3,6,4]))