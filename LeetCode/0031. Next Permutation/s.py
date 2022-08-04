from typing import List
from sys import argv as argv

'''
look at it from the back
as long as it is in descending order, keep looking
once you find a number that is smaller than the previous one that you looked at:
	swap it with the next higher number
	sort the rest in ascending order
if you never hit that number, sort the entire thing in ascending order

'''

class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		# nothing to do, and would make array accesses out of bounds
		if len(nums) < 2:
			return 

		# find the digit to increment (i)
		i = len(nums) - 2
		while nums[i] >= nums[i+1] and i > -1:
			i -= 1
		# find the amount to increment it by
		if i > -1:
			j = len(nums) - 1
			while nums[j] <= nums[i]:
				j -= 1

			# swap i and j so that i will be incremented and the rest of list is sorted descending 
			temp = nums[i]
			nums[i] = nums[j]
			nums[j] = temp

		# reverse the entire list behind i
		# if i == -1 this reverses the entire list
		nums[i+1:] = nums[i+1:][::-1]

		
# argv[1]
print(Solution())
