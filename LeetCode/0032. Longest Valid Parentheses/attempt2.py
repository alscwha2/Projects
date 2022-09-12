from typing import List
from sys import argv as argv

'''
	Iterate through the string keeping track of the open/close ratio.
	keep track of max
	once it falls below zero, start over again
	^ this has the problem that it doesn't sense (()
	CAN WE FIX THIS?
	
	YES WE CAN

	just do it again, but reading backwards. LIFEHACK


'''
class Solution:
	def longestValidParentheses(self, s: str) -> int:
		inverse = {'(' : ')', ')' : '('}
		reverse = ''.join([inverse[c] for c in s])[::-1]
		return max(self.longestValidParenthesesHelper(s), self.longestValidParenthesesHelper(reverse))

	def longestValidParenthesesHelper(self, s: str) -> int:
		biggestSeen = 0
		beginningIndex = 0
		remainingToClose = 0

		for i in range(len(s)):
			c = s[i]
			if c == '(':
				remainingToClose += 1
			if c == ')':
				remainingToClose -= 1
			if remainingToClose == 0:
				currentStreak = (i+1) - beginningIndex
				biggestSeen = max(currentStreak, biggestSeen)
			if remainingToClose < 0:
				remainingToClose = 0
				beginningIndex = i + 1
		return biggestSeen

		
print(Solution().longestValidParentheses('(()'))