import sys
from typing import List

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''
	start with ''
	for each iteration of n, take string, isert () wherever possible
	'' -> '()' -> '()()' '(())' '()()' -> 
	'()()()' '(())()' '()()()' '()(())' '()()()' '()(())' '(()())' '((()))' '(()())' '(())()' 

	as you can see, there are many duplicates. using a set to take care of those

	time:
	n executions of for loop
	for each execution, doing i*2 operations
	I don't know how many strings there are per n but I would guess more than n strings
	~O(n^3)
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stringset = {''}
        while n > 0:
        	newset = set()
        	for string in stringset:
        		for i in range(len(string) + 1):
        			newset.add(string[:i] + '()' + string[i:])
        	stringset = newset
        	n -= 1

        return list(stringset)

print(Solution().generateParenthesis(int(sys.argv[1])))