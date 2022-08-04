from typing import List
from sys import argv as argv

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		i = j = 0
		for i in range(len(s)-1, -1, -1):
			if s[i] != ' ':
				break

		for j in range(i, -1, -1):
			if s[j] == ' ':
				j += 1
				break
		return i-j+1



# argv[1]
# print(Solution())
