from typing import List
from sys import argv as argv

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		inword = False
		count = 0
		for i in range(len(s)-1, -1, -1):
			if not inword and s[i] == ' ':
				continue
			inword = True
			if s[i] == ' ':
				return count
			count += 1

		return count


# argv[1]
# print(Solution())
