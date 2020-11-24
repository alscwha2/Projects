from typing import List
from sys import argv as argv

# This one is much prettier
# O(N) for long substring of target
# O(logN) for short substring of target

class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:

		def binarySearch(nums: List[int], target: int) -> int:
			left = 0
			right = len(nums)-1
			while left <= right:
				middle = left + (right-left)//2
				num = nums[middle]
				if num == target:
					return middle
				if num > target:
					right = middle-1
				if num < target:
					left = middle+1
			return -1

		index = binarySearch(nums, target)
		if index == -1:
			return [-1,-1]

		# find the bounds
		right = left = index
		while (left-1) >= 0 and nums[(left-1)] == target:
			left -= 1
		while (right+1) < len(nums) and nums[(right+1)] == target:
			right += 1
		return [left, right]


# argv[1]
# print(Solution().searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))