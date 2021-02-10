from typing import List
from sys import argv as argv

class Solution:
	i = 0
	def decodeString(self, s: str) -> str:
		def compute_inner() -> str:
			answer = ''
			while self.i < len(s):
				if s[self.i].isnumeric():
					n = 0
					while s[self.i].isnumeric():
						n = 10 * n + int(s[self.i])
						self.i += 1
					self.i += 1
					string = compute_inner()
					for i in range(n):
						answer += string
				elif s[self.i] == ']':
					self.i += 1
					return answer
				else:
					answer += s[self.i]
					self.i += 1
			return answer

		answer = compute_inner()
		self.i = 0
		return answer



# argv[1]
print(Solution().decodeString('100[leetcode]'))