from typing import List
from sys import argv as argv
from math import inf as inf

'''
	I want to do this with one pass
	
	Convert the array to array of rolling sums
	find the biggest low-hi pair 
'''

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		if nums == []:
			return 0

		# transform array into rolling sum
		sum = 0
		for i in range(len(nums)):
			sum += nums[i]
			nums[i] = sum

		# find the biggest gap
		currentLow = 0 # because the sum is zero before we start looking at the array
		currentHigh = nums[0]
		currentMax = (currentHigh-currentLow)

		for i in range(len(nums)):
			if nums[i] > currentHigh:
				currentHigh = nums[i]
				if (currentHigh-currentLow) > currentMax:
					currentMax = (currentHigh-currentLow)

			if nums[i] < currentLow:
				currentLow = nums[i]
				currentHigh = -inf

		return currentMax

# argv[1]
print(Solution().maxSubArray([-2,-1]))
