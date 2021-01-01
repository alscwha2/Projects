from typing import List
from sys import argv as argv
from collections import deque

'''
	bitmask
'''

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		answer = []
		for i in range(2**n, 2**(n+1)):
			bitmask = bin(i)[3:]
			answer.append([nums[j] for j in range(n) if bitmask[j] == '1'])
		return answer




# argv[1]
print(Solution().subsets([i for i in range(3)]))