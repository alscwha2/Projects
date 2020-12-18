from typing import List
from sys import argv as argv
from math import log

class Solution:
	def myPow(self, x: float, n: int) -> float:
		sign = -1 if n < 0 else 1
		answer = 1
		for i in range(abs(n)):
			answer *= x
		return answer if sign == 1 else 1/answer

# argv[1]
# print(Solution())
