from typing import List
from sys import argv as argv

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		s = s.strip()
		for i in range(len(s)-1, -1, -1):
			if s[i] == ' ':
				return len(s)-1-i
		return 0


# argv[1]
# print(Solution())
