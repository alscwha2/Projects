from typing import List
from sys import argv as argv
from collections import deque

'''
	This is the method from the solution doc
'''

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		leftproduct, rightproduct = [1], 1
		for i in range(len(nums)-1):
			leftproduct.append(leftproduct[-1] * nums[i])
		for i in range(len(nums)-1, 0, -1):
			rightproduct *= nums[i]
			leftproduct[i-1] *= rightproduct
		return leftproduct

# argv[1]
# print(Solution())
