from typing import List
from sys import argv as argv

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		i,end = 0,len(nums)-1
		while i + nums[i] < end:
			if nums[i] == 0:
				return False
			currentrange = i + nums[i]
			maxrange, maxindex = 0,0
			for j in range(i+1, currentrange+1):
				if j + nums[j] > maxrange:
					maxrange, maxindex = j+nums[j], j
			i = maxindex

		return True
		
# argv[1]
# print(Solution())
