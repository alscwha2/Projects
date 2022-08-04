from typing import List
from sys import argv as argv

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		n = len(nums)

		count = 1
		spacer = 0
		for i in range(1,n):
			if nums[i] == nums[i-1-spacer]:
				count += 1
				if count > 2:
					spacer += 1
			else:
				count = 1
			if spacer:
				nums[i-spacer] = nums[i]
		return n-spacer


# argv[1]
# print(Solution())
