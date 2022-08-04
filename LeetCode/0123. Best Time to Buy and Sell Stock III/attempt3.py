from typing import List
from sys import argv as argv

'''
	optimized DP only using 1 array instead of 2
	two pass
'''

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		length = len(prices)
		maxRight = [0 for i in range(length)]

		# find the largest transactions right of price
		maxSell, maxProfit = prices[-1],0
		for i in range(len(prices)-1, -1, -1):
			price = prices[i]
			maxSell = max(maxSell, price)
			maxRight[i] = maxProfit = max(maxProfit, maxSell-price)

		# find the largest transactions left of price and add to right to get answer
		minCost, maxProfit, maxLeftProfit = prices[0],0,0
		for i,price in enumerate(prices):
			minCost = min(minCost, price)
			maxLeftProfit = max(maxLeftProfit, price-minCost)
			maxProfit = max(maxProfit, maxRight[i] + maxLeftProfit)

		return maxProfit




# argv[1]
print(Solution().maxProfit([1,4,2]))