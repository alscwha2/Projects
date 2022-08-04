from typing import List
from sys import argv as argv
'''
	Binary search:
		left and right can be answers
			(therefore: if num[middle]<target: left = middle+1])
		middle is using floor, so will always be on the left side
		base case:
			left == right
			left == right-1
'''

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
				if nums[left] == target:
					return [left, left]
				else:
					return [-1, -1]

			if left == right - 1:
				if nums[left] == target:
					if nums[right] == target:
						return [left, right]
					else:
						return [left, left]
				else:
					if nums[right] == target:
						return [right, right]
					else:
						return [-1, -1]

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
		leftBound = left
		rightBound = right
		middlePointer = middle

		# find left bound
		right = middle
		while True:
			if nums[left] == target:
				leftBound = left
				break
			if left == right-1:
				leftBound = right
				break

			middle = left + (right-left)//2
			if nums[middle] == target:
				right = middle
			else:
				left = middle+1

		# find right bound
		left = middlePointer
		right = rightBound
		while True:
			if nums[right] == target:
				rightBound = right
				break;
			if left == right-1:
				rightBound = left
				break;

			middle = left + (right-left)//2
			if nums[middle] == target:
				left = middle
			else:
				right = middle-1
		return [leftBound, rightBound]

# argv[1]
# print(Solution().searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))