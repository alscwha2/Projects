from sys import argv
from math import floor, log10

class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x <= 0:
			return not bool(x)
		
		power = floor(log10(x))
		place = 0
		
		while power > place:
			if  x // 10 ** power % 10 != x // 10 ** place % 10:
				return False
			power -= 1
			place += 1
		
		return True
		
print(Solution().isPalindrome(int(argv[1])))