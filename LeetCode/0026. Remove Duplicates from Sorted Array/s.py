from typing import List
from sys import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		dups = 0
		for i in range(1, len(nums)):
			if nums[i] == nums[i-1]:
				dups += 1
			else:
				nums[i - dups] = nums[i]

		# new length is equal to length of array minus the number of duplicates
		return len(nums) - dups

sys.argv[1]
print(Solution())
