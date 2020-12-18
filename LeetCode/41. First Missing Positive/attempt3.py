from typing import List
from sys import argv as argv
'''
	using a list as a makeshift hashmap
'''
class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		needed = [True for i in range(len(nums) + 2)]
		needed[0] = False
		for num in nums:
			try:
				needed[num] = False
			except:
				pass
		for i,need in enumerate(needed):
			if need:
				return i


print(Solution().firstMissingPositive([1,2,0]))