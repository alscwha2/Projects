from typing import List
from sys import argv as argv

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		i = 0
		j = len(nums)-1
		while j >= i:
			k = i + (j-i)//2
			num = nums[k]
			if num < target:
				i = k + 1
			elif num > target:
				j = k - 1
			else:
				return k
		return i

# argv[1]
print(Solution())
