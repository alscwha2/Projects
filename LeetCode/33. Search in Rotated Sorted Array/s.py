from typing import List
from sys import argv as argv

'''
	This is just a glorified linear search. It works, but clearly the answer should be log(n) binary search


	cmp to first number
	if greater increment
		if less return -1
	if less decrement %len(nums)
		if greater return -1
'''

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		if len(nums) == 0:
			return -1

		def increment(i):
			return (i+1)%len(nums)
		def decrement(i):
			return (i-1)%len(nums)

	
		i = 0
		if target > nums[0]:
			while target > nums[i] and nums[increment(i)] > nums[i]:
				i = increment(i)
				if i == 0:
					return -1
			return i if target == nums[i] else -1
		else:
			while target < nums[i] and nums[decrement(i)] < nums[i]:
				i = decrement(i)
				if i == 0:
					return -1
			return i if target == nums[i] else -1		

# argv[1]
print(Solution().search([4,5,6,7,0,1,2], 0))