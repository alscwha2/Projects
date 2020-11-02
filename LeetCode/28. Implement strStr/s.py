from typing import List
from sys import argv as argv

class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if needle == '':
			return 0
			
		for i in range(len(haystack)):
			if haystack[i] == needle[0]:
				if len(needle) == 1:
					   return i
				if len(needle) + i > len(haystack):
					return -1
				j = 1
				while j < len(needle):
					if haystack[i+j] != needle[j]:
						break
					j += 1
				if j == len(needle):
					return i
		return -1
print(Solution().strStr('aaa', 'aaa'))
