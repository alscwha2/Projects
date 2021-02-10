from typing import List
from sys import argv as argv
from heapq import heappush, heappop, heapreplace

'''
	Basically the same solution, with the optimization pointed out by the doc that you don't need to keep track of how 
	many meetings are going on currently, rather just whether there is one meeting that has currently ended so that you
	don't have to increase the size of the heap by adding another meeting
'''

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		if not intervals:
			return 0

		intervals = sorted(intervals)
		rooms = [intervals[0][1]]
		for i in range(1, len(intervals)):
			start,end = intervals[i]
			if start >= rooms[0]:
				heapreplace(rooms, end)
			else:
				heappush(rooms, end)
		return len(rooms)



# argv[1]
# print(Solution())
