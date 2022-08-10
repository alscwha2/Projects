"""

"""

from typing import List
import random

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		SMALLER, EQUAL, BIGGER = -1, 0, 1
		def binary_search(i, j, *, array, comparator):
			if i >= j: return None

			k = i + (j - i) // 2
			comparison = comparator(array, k)
			if comparison is EQUAL: return k
			elif comparison is BIGGER: j = k
			else: i = k + 1
			return binary_search(i,j,array=array, comparator=comparator)

		def search_second(x):
			# we want to find the element 


		def search_first(x):
			return lambda elem: EQUAL if array[k] == x else BIGGER if aray[k] > x else SMALLER

		return binary_search(0, len(nums1), array=nums1,comparator=)
		

sb
l = [num for num in range(0, random.randrange(1, 200), 5)]

print(f"i={Solution().findMedianSortedArrays(l,[4,5,6])}")