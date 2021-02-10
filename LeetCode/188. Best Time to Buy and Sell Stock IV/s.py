from typing import List
from sys import argv as argv
from math import inf

'''
	You have k transactions available to do. The algorithm is:
	* Start with no transactions
	* repeat k times:
		* Find best avaialble transaction to do
			* can be buying and selling in between existing transactions
			* or can be splitting existing transactions into 2 separate ones buy selling and buying back in the middle
				* find the biggest drop in price mid-transaction
				* sell right before drop and buy back right after drop
				* the way that I implemented this was by iterating backwards and finding the biggest increase going backwards

	I used DP here so as not to repeat work when testing candidate transactions. It made a big difference when I added DP.
'''
class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		if not prices:
			return 0

		dp = {}
		# find the best transaction in current subarray in given direction
		# return (profit, buyindex, sellindex)
		def bestDeal(start, end, direction):
			if (start,end,direction) in dp:
				return dp[(start,end,direction)]

			cost, profit = (inf,0), (0,0,0)
			for i in range(start, end, direction):
				price = prices[i]
				cost = min(cost, (price,i))
				profit = max(profit, (price-cost[0], cost[1], i))
			dp[(start,end,direction)] = profit
			return profit
		
		# array to keep track of buy and sell points for previous transactions
		transactions = [0 for price in prices]
		BOUGHT, SOLD = 1,-1
		FORWARDS, BACKWARDS = 1,-1
		totalProfit = 0

		# for the number of transactions that you can do
		for i in range(k):
			# find the best next transaction
			best = (0,0,0)
			start, end = 0,0 
			for end, status in enumerate(transactions):
				# the 'transactions' array keeps track of whether a buy, sell, or nothing happened on a given day
				if status == BOUGHT:
					best = max(best, bestDeal(start,end+1,FORWARDS))
					start = end
				elif status == SOLD:
					best = max(best, bestDeal(end,start-1,BACKWARDS))
					start = end

			profit,buy,sell = max(best, bestDeal(start,end+1,1))
			if profit == 0: # if none of the remaining transactions are lucrative there is no reason to continue iteration
				break
			totalProfit += profit
			transactions[buy] = BOUGHT
			transactions[sell] = SOLD

		return totalProfit



# argv[1]
print(Solution().maxProfit(2,[3,2,6,5,0,3]))