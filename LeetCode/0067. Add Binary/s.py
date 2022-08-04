from typing import List
from sys import argv as argv
from collections import deque

class Solution:
	def addBinary(self, a: str, b: str) -> str:
		longer, shorter = (a,b) if len(a) > len(b) else (b,a)
		shorter = shorter.rjust(len(longer), '0')
		a,b = longer, shorter

		sum = deque()
		a = deque(a)
		b = deque(b)
		overflow = 0
		for i in range(len(a)):
			num = overflow + int(a.pop()) + int(b.pop())
			if num > 1:
				overflow = 1
				num -= 2
			else:
				overflow = 0
			sum.appendleft(str(num))

		if overflow:
			sum.appendleft('1')

		return ''.join(sum)

# argv[1]
print(Solution().addBinary('10', '1'))
