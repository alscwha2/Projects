from typing import List

'''
	using negative sign instead of zero as marker
	got this from someone in the discussion but I think that the solution doc had it this way as well.
'''

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)

		# first pass - turn all negatives and zero into n+2
		for i,num in enumerate(nums):
			if num <= 0:
				nums[i] = n+2

		# second pass - for each number making sure that num-1 is marked negative
		for num in nums:
			num = abs(num)
			if 1 <= num <= n:
				nums[num-1] = -abs(nums[num-1])

		# third pass - find smallest number that doesn't have a zero
		for i in range(n):
			if nums[i] > 0:
				return i+1
		return n+1

print(Solution().firstMissingPositive([1]))