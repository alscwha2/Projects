from typing import List
from sys import argv as argv

'''
	Instead of having two arrays with two pointers, just have one sorted array with all of the times, 
	but the entries are tuples. If it is a starting time then the entry is (time, +1), 
	if it's an ending time it's (time, -1). 
	Then just iterate through the array, adding up all of the +1s and -1s, 
	and the maximum number that you get will be the maximum number needed.

	This does run slower than the solution doc's implementation, 
	because we're doing more work by always keeping track of the current number of rooms and comparing it to the maximum seen. 
	The doc's implementation avoids this by only checking whether a meeting has ended when we want to start a new one. 
	But what we gain with my implementation is an easy to understand, clean and concise code, 
	that has the same algorithmic complexity.
'''

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		# construct the times array
		times = []
		for start,end in intervals:
			times.extend([(start,1),(end,-1)])
		times = sorted(times)
		
		# iterate through, keeping track of how many rooms are currently used and the maximum number of needed rooms so far
		needed = 0
		current = 0
		for time in times:
			current += time[1]
			needed = max(needed, current)
		return needed


# argv[1]
# print(Solution())
