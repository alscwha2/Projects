from typing import List
from sys import argv as argv

'''
	Shift all elements of first array over n spaces so that the buffer is in the beginning of array
	Use two pointers and compare 
'''

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		for i in range(m+n-1, n-1, -1):
			nums1[i] = nums1[i-n]
		i,j = n,0
		for k in range(m+n):
			if j == n:
				return
			if i == m+n or nums2[j] <= nums1[i]:
				nums1[k] = nums2[j]
				j += 1
			else:
				nums1[k] = nums1[i]
				i += 1





# argv[1]
# print(Solution())
