from typing import List

'''
	same thing basically but cleaner

	took out initial check if 1 is in the array to make code smaller
	used a lot of % operator so that I don't have to check separately for n
'''

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)

		# first pass - turning 0's negatives, and >n's into -1s
		for i,num in enumerate(nums):
			if num == 0 or num > n:
				nums[i] = -1

		# second pass - for each number making sure that its spot in array has zero
		i = 0
		while i < n:
			num = nums[i]
			if num < 1:
				pass
			elif num%n == i:
				nums[i] = 0
			elif num > 0:
				temp = nums[num%n]
				nums[num%n] = 0
				if temp > 0:
					nums[i] = temp
					continue
			i += 1

		# third pass - find smallest number that doesn't have a zero
		for i in range(1, n+1):
			if nums[i%n] != 0:
				return i
		return n+1

print(Solution().firstMissingPositive([1]))