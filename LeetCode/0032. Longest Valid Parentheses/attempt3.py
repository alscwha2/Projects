from typing import List
from sys import argv as argv

'''
	Constant space. Code duplication. ugly


'''
class Solution:
	def longestValidParentheses(self, s: str) -> int:
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
		
		beginningIndex = len(s)-1
		remainingToClose = 0
		for i in range(len(s)-1, -1, -1):
			c = s[i]
			if c == ')':
				remainingToClose += 1
			if c == '(':
				remainingToClose -= 1
			if remainingToClose == 0:
				currentStreak = beginningIndex - i + 1
				biggestSeen = max(currentStreak, biggestSeen)
			if remainingToClose < 0:
				remainingToClose = 0
				beginningIndex = i - 1
		return biggestSeen

		
print(Solution().longestValidParentheses('(()'))