from typing import List
from sys import argv as argv

'''
	my attempt at the dp solution
	keep track of the best transactions to the right and to the left
	3 pass
'''

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		length = len(prices)
		maxLeft = [0 for i in range(length)]
		maxRight = [0 for i in range(length)]

		# find the largest transactions left of price
		minCost, maxProfit = prices[0],0
		for i,price in enumerate(prices):
			minCost = min(minCost, price)
			maxLeft[i] = maxProfit = max(maxProfit, price-minCost)

		# find the largest transactions right of price
		maxSell, maxProfit = prices[-1],0
		for i in range(len(prices)-1, -1, -1):
			price = prices[i]
			maxSell = max(maxSell, price)
			maxRight[i] = maxProfit = max(maxProfit, maxSell-price)

		# find point staddling sum of largest transactions
		maxProfit = 0
		for l,r in zip(maxLeft, maxRight):
			maxProfit = max(maxProfit, l+r)
		return maxProfit




# argv[1]
print(Solution().maxProfit([1,4,2]))