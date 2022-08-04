import sys
from typing import List

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''
	recursive solution, much cleaner
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    	if n is 0: return ['']
    	stringset = set()
    	for string in self.generateParenthesis(n-1):
    		for i in range(len(string) + 1):
    			stringset.add(string[:i] + '()' + string[i:])
    	return list(stringset)


print(Solution().generateParenthesis(int(sys.argv[1])))