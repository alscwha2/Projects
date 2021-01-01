from typing import List
from sys import argv as argv

'''
	using two pointers instead of recalculating spacer
'''

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		count = 1
		j = 0
		for i in range(1,len(nums)):
			if nums[i] == nums[j]:
				count += 1
				if count > 2:
					j -= 1
			else:
				count = 1
			j += 1
			nums[j] = nums[i]
		return j+1


# argv[1]
# print(Solution())
