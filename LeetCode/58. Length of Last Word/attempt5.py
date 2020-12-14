from typing import List
from sys import argv as argv

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		words = s.strip().split()
		return len(words[len(words)-1])


# argv[1]
# print(Solution())
