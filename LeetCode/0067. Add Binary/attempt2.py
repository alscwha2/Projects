from typing import List
from sys import argv as argv
from collections import deque

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		a,b = (int(a, 2), int(b, 2))
		while a != 0:
			a, b = (a & b) << 1, a ^ b
		return format(a, 'b')

# argv[1]
print(Solution().addBinary('11', '1'))
