from typing import List
from sys import argv as argv

'''
	fibonnacci iteration solution
'''

class Solution:
	def climbStairs(self, n: int) -> int:
		previous,current = 0,1
		for i in range(n):
			next = previous + current
			previous = current
			current = next
		return current
		


		

# argv[1]
# print(Solution())
