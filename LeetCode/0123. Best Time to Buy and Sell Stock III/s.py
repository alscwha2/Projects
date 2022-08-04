from typing import List
from sys import argv as argv

'''
	find the best trasactions
	for the second transaction:
		add another before the first or 
		add another after the first or
		find biggest price drop in first 
'''

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		
		def findBestDeal(prices): # this is just the solution to the easier version of the question with only 1 transaction
			profit, buy, sell = 0,0,0 # these store the final anser
			lowest, highest = 0,0 # these store the indecies of the transaction that we are currently evaluating during iteration
			for i in range(1,len(prices)):
				if prices[i] <= prices[lowest]:
					lowest = highest = i
				if prices[i] > prices[highest]:
					highest = i
					if prices[highest]-prices[lowest] > profit:
						profit = prices[highest]-prices[lowest]
						buy, sell = lowest, highest
			return (profit, buy, sell) # return the highest profit and it's buy/sell indices


		profit, buy, sell = findBestDeal(prices)
		
		# the way that we find the biggest drop in price over buy:sell is actually by reversing 
		#    the array and finding the biggest increase in the reversed array
		bestBefore = findBestDeal(prices[:buy])[0]
		bestAfter = findBestDeal(prices[sell:])[0]
		biggestDip = findBestDeal(prices[buy:sell+1][::-1])[0]
		
		profit += max(bestBefore, bestAfter, biggestDip)
		return profit

# argv[1]
# print(Solution())
