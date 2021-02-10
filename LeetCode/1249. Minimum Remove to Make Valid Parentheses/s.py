from typing import List
from sys import argv as argv

class Solution:
	def minRemoveToMakeValid(self, s: str) -> str:
		close = s.count(')')
		open = 0
		
		answer = []
		for char in s:
			if char == ')':
				close -= 1
				if open > 0:
					open -= 1
					answer.append(char)
			elif char == '(':
					if close > open:
						open += 1
						answer.append(char)
			else:
				answer.append(char)
		return ''.join(answer)

# argv[1]
print(Solution().minRemoveToMakeValid("())()((("))