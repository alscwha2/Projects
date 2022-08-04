from typing import List
from sys import argv as argv
from heapq import heappush, nsmallest

'''
	O(nlogn) time
	O(n) space


	I would like to do an implementation with a fixed size heap (as someone ins the leetcode comments pointed out)
	but it is not built into heapq. If there were a way to pop the largest element it would be trivial to implement

	As the solution doc points out, you can use the square of the distance by not using sqrt because it is all relative
	and square keeps relative orderings (for positive numbers)
'''

class Solution:
	def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

		def distance(point):
			x,y = point
			return x*x + y*y

		heap = []
		for point in points:
			heappush(heap, (distance(point), point))
		return [point[1] for point in nsmallest(K, heap)]

# argv[1]
print(Solution().kClosest([[1,3],[-2,2]], 1))