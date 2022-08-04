from typing import List
from sys import argv as argv
from s import Solution as sol

'''
I tweaked the "One-pass Simulation" approach slightly to make it (in my opinion) much more intuitive, without affecting performance at all.

You want to make the most money that you can by completing two transactions. You can do this with one pass through the array. You have to keep track of three pieces of information:

	1 - If I completed the best transaction until this point, how much money would I make (i.e. the first problem in the series).

	2 - At which point can I acquire a second stock and keep the most money in my pocket. The money that I have will be firstProfit-secondPrice. (Note that this value could be negative, if the second stock costs more than you made from the first one. This is not a problem, as you will make that money back when you sell the second stock)

	You can solve the problem in one iteration through the array. The way to accomplish this is to ask: If I do the best transaction until now and buy the second stock at the current price, will I end up with more money in my pocket than I would have in a previous stage of the iteration.

		mostMoneyInPocket = max(mostMoneyInPocket, firstTransactionProfit - currentPrice)

	3 - What is the highest price that I can sell that second stock for? Since I already bought it all I have to do is find the highest price to sell it for.
	
	As you iterate, ask: if I sold it at the current price, would it make more money than selling it earlier?
		
		profitFromTwoTransactions = max(secondProfit, mostMoneyInPocket + currentPrice)
'''

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		firstTransactionCost = prices[0]
		firstTransactionProfit = 0

		mostMoneyInPocket = -prices[0] 
		profitFromTwoTransactions = 0 

		for currentPrice in prices:
			firstTransactionCost = min(firstTransactionCost, currentPrice) 
			firstTransactionProfit = max(firstTransactionProfit, currentPrice-firstTransactionCost)

			mostMoneyInPocket = max(mostMoneyInPocket, firstTransactionProfit-currentPrice)
			profitFromTwoTransactions = max(profitFromTwoTransactions, mostMoneyInPocket+currentPrice)
		return profitFromTwoTransactions



# argv[1]
array = [7,6,4,3,1]
print('Output:', Solution().maxProfit(array))
print('Expected:', sol().maxProfit(array))