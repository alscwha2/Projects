from sys import argv
from math import floor, log10

class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x <= 0:
			return not x

		def get_digit(place):
			return (x // (10 ** place)) % 10
		
		left = floor(log10(x))
		right = 0
		
		while left > right:
			if get_digit(left) != get_digit(right):
				return False
			left -= 1
			right += 1
		
		return True
		
print(Solution().isPalindrome(int(argv[1])))