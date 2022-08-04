from typing import List
from sys import argv as argv
from math import log

class Solution:
	def mySqrt(self, x: int) -> int:
		for i in range(x+2):
			if i*i > x:
				return i-1

print(Solution().mySqrt(8))
