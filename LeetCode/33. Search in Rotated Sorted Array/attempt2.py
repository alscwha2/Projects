from typing import List
from sys import argv as argv

'''
	define pivot point as the point with the smallest value
	find the pivot point using binary search

	convert to pivoted indices by doing ri = (pi + pivot) % len(nums)
'''

class Solution:
	def search(self, nums: List[int], target: int) -> int:

		# find pivot point (i.e index of smallest element in array)
		i = 0
		j = len(nums)-1
		while j > i:
			k = i + (j-i)//2
			if nums[k] > nums[j]:
				i = k+1
			if nums[k] <= nums[j]:
				j = k

		pivot = i

		# fn to convert from ideal 0...n-1 ideces to the indices of num array
		def convert(i):
			return (i + pivot) % len(nums)

		# binary search to find target
		i = 0
		j = len(nums) - 1
		while j >= i:
			k = i + (j-i)//2
			num = nums[convert(k)]

			if num == target:
				return convert(k)
			if num > target:
				j = k-1
			if num < target:
				i = k+1

		return -1

# argv[1]
print(Solution().search([4,5,6,7,0,1,2],0))