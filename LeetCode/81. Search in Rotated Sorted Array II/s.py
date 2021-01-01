from typing import List
from sys import argv as argv

'''
	LETS CALL THIS ATTEMPT A FAILURE FOR NOW

	Appraoch 1-
		binary search to find smallest element
		fix indicies
		binary search to find element
	Approach 2- 
		Find a way to binary search while accounting for the rotation in one pass
'''

class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		if not nums:
			return False

		n = len(nums)
		def searchStartingIndex(i=0,j=n-1):
			if i == j:
				return i-1

			if nums[i] == nums[j]:
				k = i + (j-i)//2
				if nums[k] > nums[i]:
					i = k+1
				if nums[k] < nums[j]:
					j = k
				if nums[k] == nums[i]:
					'''
						give starting index if not all equal else i-1
					'''
					left = searchStartingIndex(i,k)
					right = searchStartingIndex(k,j)
					if left == i-1 and right == k-1:
						return -1
					if left == i-1:
						return right
					if right == k-1:
						return left

			while i <= j:
			if nums[i] <= nums[j]:
				return i
			else:
				k == i + (j-i)//2
				if nums[k] >= nums[i]: # only one of these two can execute b/c nums[i]>nums[j]
					i = k+1
				if nums[k] <= nums[j]:
					j = k

		head = searchStartingIndex()
		if head == -1:
			return nums[0] == target

		print(head)
		def convert(i):
			return (i + head)%n

		i,j = 0,n-1
		while i <= j:
			k = i + (j-i)//2
			num = nums[convert(k)]
			if num < target:
				i = k+1
			elif num > target:
				j = k-1
			else:
				return True
		return False



# argv[1]
print(Solution().search([1,3,1,1,1],3))