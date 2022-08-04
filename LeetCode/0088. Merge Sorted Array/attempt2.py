from typing import List
from sys import argv as argv

'''
	This is linear time linear space.
	But the problem presumably wanted constant space...
	
'''

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		nums3 = []
		i,j = 0,0
		while i < m and j < n:
			if nums1[i] <= nums2[j]:
				nums3.append(nums1[i])
				i += 1
			else:
				nums3.append(nums2[j])
				j += 1

		if i == m:
			for k in range(j,n):
				nums3.append(nums2[k])
		elif j == n:
			for k in range(i,m):
				nums3.append(nums1[k])

		nums1[:] = nums3




# argv[1]
# print(Solution())
