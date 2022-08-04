from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		i,j = 0,len(nums)-1
		while i <= j:
			k = i + (j-i)//2
			if nums[k] < target:
				i = k+1
			else:
				j = k-1
		return i