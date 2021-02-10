from typing import List
from sys import argv as argv
from functools import reduce

'''
	recursive divide and conquer using indices to edit in place to save space and time
'''

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		def helper(i,j):
			# base cases
			if j == i+2: 
				nums[i], nums[i+1] = nums[i+1], nums[i]
				return
			if j == i+1:
				nums[i] = 1
				return

			# split array into 2
			k = i + (j-i)//2
			
			# find product of both halves 
			firsthalfproduct, secondhalfproduct = 1, 1
			for x in range(i,k):
				firsthalfproduct *= nums[x]
			for x in range(k,j):
				secondhalfproduct *= nums[x]
			
			# recursively execute on both halves
			helper(i,k)
			helper(k,j)
			
			# multiply the product of one half to the other
			for x in range(i,k):
				nums[x] *= secondhalfproduct
			for x in range(k,j):
				nums[x] *= firsthalfproduct
				
		helper(0,len(nums))
		return nums


# argv[1]
print(Solution().productExceptSelf([1,2,3,4]))