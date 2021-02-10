from typing import List
from sys import argv as argv
from s import Solution as sol

'''
	my attempt at the One-pass constant space solution

	This is two-pass linear space, but it's to demonstrate the concept. What we are doing is iterating through the 
		array and asking "had I already completed trasaction 1 and made a profit, how much profit would I have left
		if I bought into transaction 2 right here?"

	Look at attempt5. The intuition/explanation is much better and the code is cleaner. It is a real implementaion 
		of the algorithm.
'''

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		newprices = prices.copy()

		minCost, profit = prices[0],0
		for i,price in enumerate(prices):
			minCost = min(minCost, price)
			profit = max(profit, price-minCost)
			newprices[i] -= profit

		minCost, profit = prices[0],0
		for i,price in enumerate(prices):
			minCost = min(minCost, newprices[i])
			profit = max(profit, price-minCost)
		return profit



# argv[1]
array = [7,6,4,3,1]
print('Output:', Solution().maxProfit(array))
print('Expected:', sol().maxProfit(array))