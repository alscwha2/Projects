from typing import List
from sys import argv as argv
from functools import reduce

'''
	O(nlogn)
	recursive divide and conquer
'''

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		# base cases
		if len(nums) == 2: return nums[::-1]
		if len(nums) == 1: return [1]

		# split array into 2
		halfway = len(nums)//2
		firsthalf, secondhalf = nums[:halfway], nums[halfway:]
		
		# find product of both halves 
		def product(a,b): return a*b
		firsthalfproduct, secondhalfproduct = reduce(product, firsthalf), reduce(product, secondhalf)
		
		# recursively execute on both halves
		firsthalf, secondhalf = self.productExceptSelf(firsthalf), self.productExceptSelf(secondhalf)
		
		# mltiply the product of one half to the other
		for i in range(len(firsthalf)):
			firsthalf[i] *= secondhalfproduct
		for i in range(len(secondhalf)):
			secondhalf[i] *= firsthalfproduct
			
		# combine and return
		return firsthalf + secondhalf


# argv[1]
# print(Solution())
