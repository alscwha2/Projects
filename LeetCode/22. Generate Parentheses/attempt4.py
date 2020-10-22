import sys
from typing import List

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''
	I'm going to try what leetcode calls the 'backtracking' approach

	I found out a few interesting things:
		Because of the relationship between the numOpen, numClosed, and length of the string
		you have a lot of options in terms of which information to keep track of. You can
		do simple arithmetic to figure out the information that you need to know

		It appears that the most efficient way to do it is by minimizing the amount of variable accesses
		by replacing them with int literals
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    	strings = []

    	def finishStrings(s: str = '', leftToOpen : int = n, leftToClose : int = 0):
    		if leftToOpen == leftToClose == 0: strings.append(s)
    		if leftToOpen > 0: finishStrings(s + '(', leftToOpen-1, leftToClose+1)
    		if leftToClose > 0: finishStrings(s + ')', leftToOpen, leftToClose-1)
    		
    	finishStrings()
    	return strings

print(Solution().generateParenthesis(int(sys.argv[1])))