from typing import List
from sys import argv as argv

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		nextzero, next2 = 0, len(nums)-1

		i = nextzero
		while i <= next2:
			num = nums[i]
			if num == 0:
				nums[i], nums[nextzero] = nums[nextzero], 0
				i, nextzero = i+1, nextzero+1
			elif num == 2:
				nums[i], nums[next2] = nums[next2], 2
				next2 -= 1
			else:
				i += 1



		


# argv[1]
# print(Solution())
