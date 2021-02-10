from typing import List
from sys import argv as argv
from heapq import heappush, heappop

'''
	Sort intervals by starting time - O(nlogn)
	n heappushes, n heappops - O(nlogn), O(nlogn)

	Space - O(N) heap, O(N) sorted array
'''

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		if not intervals:
			return 0

		intervals = sorted(intervals)
		ongoing = [intervals[0][1]]
		needed = 1
		for i in range(1, len(intervals)):
			start,end = intervals[i]
			while ongoing and start >= ongoing[0]:
				heappop(ongoing)
			heappush(ongoing, end)
			needed = max(needed, len(ongoing))
		return needed



# argv[1]
# print(Solution())
