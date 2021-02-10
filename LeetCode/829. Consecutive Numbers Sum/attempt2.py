from typing import List
from sys import argv as argv

'''
	This is a bit more efficient than the first attempt because in the first attempt we were recomputing the sum
		from 1 to i over and over again, here we just add on to the rest of the previous iteration
'''

class Solution:
	def consecutiveNumbersSum(self, N: int) -> int:
		answer = 1
		i = 1
		seq = 0
		while True:
			seq += i
			i += 1
			rest = N-seq
			if rest < i:
				break
			if rest % i == 0:
				answer += 1
		return answer


# argv[1]
print(Solution().consecutiveNumbersSum(15))