from typing import List
from sys import argv as argv

'''
	test whether it can be divisible by 2, 3, etc numbers:
		compute all of the extra that the later numbers have over ther first one
			if n is number of groups then it's n(n-1)/2 or the sum from 1 to n-1
		subtract from N
		see if remainder is divisible by n
		if yes then it is the sum from remainder/n to remainder/n + n-1. so add 1 to answer
		if remainder is less than n then you will never find another group because the numbers will keep on increasing.
'''

class Solution:
	def consecutiveNumbersSum(self, N: int) -> int:
		answer = 1
		for i in range(2,N):
			seq = (i-1) * (i-2) // 2
			rest = N - seq
			if rest < i:
				break
			if rest % i == 0:
				answer += 1
		return answer

# argv[1]
# print(Solution())
