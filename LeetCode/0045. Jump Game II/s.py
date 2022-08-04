from typing import List
from sys import argv as argv

class Solution:
	def jump(self, nums: List[int]) -> int:
		if len(nums) <= 1:
			return 0
			
		jumps = 1
		i = 0
		end = len(nums)-1
		num = nums[i]
		while i + num < end:
			maxrange, maxindex = (0,0)
			for j in range(i+1, i+num+1):
				if j + nums[j] > maxrange:
					maxrange, maxindex = (j+nums[j], j)

			i = maxindex
			num = nums[i]
			jumps += 1

		return jumps


# argv[1]
# print(Solution())
