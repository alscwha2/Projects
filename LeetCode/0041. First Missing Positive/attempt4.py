'''
	this is the way that we should have done it the whole time...
'''

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		nums = set(nums)
		for i in range(1, len(nums) + 2):
			if not i in nums:
				return i