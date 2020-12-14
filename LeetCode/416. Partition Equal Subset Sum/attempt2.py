from typing import List
from sys import argv as argv

'''
	find sum of numbers O(N)
	if n%2 return false
	subsetsum of n/2

	(if n/2 is in set then return true)


	things to consider:
		making two arbitrary partitions and swapping
		slowly building up the partitions in a way that will produce the answer
		backtracking
			where should we start? at the beginning?
			THIS DIDN'T WORK! too slow



'''

class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		total = sum(nums)

		if total % 2 == 1:
			return False

		target = total//2
		nums = sorted(nums)

		def finishGroup(remaining, index) -> bool:
			for i in range(index, len(nums)):
				num = nums[i]
				if num < remaining:
					if finishGroup(remaining-num, i+1):
						return True
				elif num > remaining:
					return False
				elif num == remaining:
					return True
			return False

		return finishGroup(target, 0)






# argv[1]
print(Solution().canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))