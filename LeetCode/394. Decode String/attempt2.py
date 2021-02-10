from typing import List
from sys import argv as argv
from collections import deque

'''
	using a stack instead of recursion. This one came out better
'''

class Solution:
	def decodeString(self, s: str) -> str:
		stack = deque([[1,'']])
		n = 0
		for char in s:
			if char.isnumeric():
				n = 10 * n + int(char)
				continue
			else:
				if char == '[':
					stack.append([n,''])
					n = 0
				elif char == ']':
					m, token = stack.pop()
					answer = ''
					for i in range(m):
						answer += token
					stack[-1][1] += answer
				else:
					stack[-1][1] += char
		return stack[-1][1]





# argv[1]
print(Solution().decodeString('100[leetcode]'))