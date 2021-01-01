from typing import List
from sys import argv as argv

'''
	Comparing from the back of the array, like Solution3 in the doc 
'''

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		i,j = m-1,n-1
		for k in range(m+n-1, -1, -1):
			if j == -1:
				return
			if i == -1 or nums2[j] >= nums1[i]:
				nums1[k] = nums2[j]
				j -= 1
			else:
				nums1[k] = nums1[i]
				i -= 1





# argv[1]
# print(Solution())
