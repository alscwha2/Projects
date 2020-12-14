from typing import List
from sys import argv as argv

'''
	This one is slower than attempt2. I think that that is because for every character we do the s[i]==' ' 
	comparison which is slower than the if inword test which just tests a boolean variable
'''

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		inword = False
		count = 0
		for i in range(len(s)-1, -1, -1):
			if s[i] == ' ':
				if inword:
					return count
				else:
					continue
			inword = True
			count += 1

		return count


# argv[1]
# print(Solution())
