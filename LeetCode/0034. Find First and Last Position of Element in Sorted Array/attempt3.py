from typing import List
from sys import argv as argv

'''
	modular version of code, modified to always be O(logN)
'''

class Solution:
	def searchRange(self, nums: List[int], target: int) -> List[int]:

		# ---------------------- FUNCTIONS ---------------------------------

		def binarySearch(nums: List[int], target: int) -> int:
			left = 0
			right = len(nums)-1
			while left <= right:
				middle = left + (right-left)//2
				num = nums[middle]
				if num == target:
					return (middle, left, right)
				if num > target:
					right = middle-1
				if num < target:
					left = middle+1
			return (-1, left, right)

		def binarySearchLeftBound(nums: List[int], left: int, right: int):
			while True:
				if left >= right:
					return left

				middle = left + (right-left)//2
				if nums[middle] == target:
					right = middle
				else:
					left = middle+1


		def binarySearchRightBound(nums: List[int], left: int, right: int):
			while True:
				if right <= left:
					return left

				middle = left + (right-left)//2 + 1
				if nums[middle] == target:
					left = middle
				else:
					right = middle-1

		# -------------------------- CODE STARTS HERE -------------------------------------------

		# find the bounds
		middle, left, right = binarySearch(nums, target)

		if middle == -1:
			return [-1,-1]

		leftBound = binarySearchLeftBound(nums, left, middle)
		rightBound = binarySearchRightBound(nums, middle, right)

		return [leftBound, rightBound]


# argv[1]
print(Solution().searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))