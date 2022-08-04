from typing import List
from sys import argv as argv

class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:
		if nums == []:
			return [-1, -1]

		left = 0
		right = len(nums)-1

		middle = -1
		while True:
			# base cases:
			if left == right:
				if nums[left] != target:
					return [-1, -1]
			if left > right:
				return [-1,-1]

			# find middle
			middle = left + (right-left)//2
			num = nums[middle]

			# if found:
			if num == target:
				break

			# if not found, update:
			if num < target:
				left = middle + 1
			if num > target:
				right = middle - 1

		# at this point we found the target, but don't know the range of it
		left = middle
		right = middle
		while left-1 >= 0 and nums[left-1] == target:
			left -= 1
		while right+1 < len(nums) and nums[right+1] == target:
			right += 1
		return [left, right]

# argv[1]
# print(Solution().searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))