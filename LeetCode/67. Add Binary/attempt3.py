from typing import List
from sys import argv as argv
from collections import deque

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		return format(int(a) + int(b), b)
# argv[1]
print(Solution().addBinary('10', '1'))
