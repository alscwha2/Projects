from typing import List

'''
	O(N) space
	3 linear passes
	not pretty
'''

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)
		contains1 = False
		for i,num in enumerate(nums):
			if num < 1 or num > n:
				nums[i] = -1
			elif num == 1:
				contains1 = True

		if not contains1:
			return 1

		i = 0
		while i < n:
			num = nums[i]
			if num == i:
				nums[i] = 0
				i += 1
			elif num <= 0:
				i += 1				
			elif num > 0 and num < n:
				temp = nums[num]
				nums[num] = 0
				if temp > 0:
					nums[i] = temp
				else:
					i += 1
			elif num == n:
				nums[0] = 0
				i += 1


		for i in range(1, len(nums)):
			if nums[i] != 0:
				return i
		if nums[0] != 0:
			return n
		return n+1

print(Solution().firstMissingPositive([2,1]))