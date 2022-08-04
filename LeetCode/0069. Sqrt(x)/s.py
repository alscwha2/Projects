from typing import List
from sys import argv as argv
from math import log

class Solution:
	def mySqrt(self, x: int) -> int:
		i,j = (0,x)
		while i <= j:
			k = i + (j-i)//2
			num = k*k
			print(i,j,k,num)
			if num > x:
				j = k-1
			elif num < x:
				i = k+1
			else:
				return k
		return j//1

print(Solution().mySqrt(8))
