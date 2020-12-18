from typing import List
from sys import argv as argv

'''
	The result could have:
		more intervals:
			if the interval I'm inserting doesn't everlap with the existing ones
		same amount:
			if it only overlaps with one
		less:
			if it overlaps with many

	time:
		easily in O(N)
		maybe possible in log(N)?
	space
		can do it in constant space, since we will only use at most one more slot than we were given
'''

class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		begin,end = newInterval
		combined = 0
		intervalslot = -1

		# binary serach to find the slot that it should go in

		i, j = 0, len(nums)-1
		while i <= j:
			k = i + (j-i)//2
			num = nums[k]
			if num > begin:
				j = k-1
			elif num < begin:
				i = k+1
			else:
				intervalslot = k
				break
		if intervalslot != -1:
			intervalslot = j



		for interval, i in enumerate(intervals):
			didcombine = False
			if newInterval[0] <= interval[0] <= newInterval[1]:
				newInterval[1] = max(newInterval[1], interval[1])
				didcombine = True
			if interval[0] <= newInterval[0] <= interval[1]:
				newInterval[0] = min(newInterval[0], interval[0])
				didcombine = True
			if didcombine:
				combined += 1
				if combined == 1:
					intervalslot = i
		intervals[i] = newInterval
		if combined == 0:
			i,j = 0,len(nums-1)
			while i <= j:
				k = i + (j-1)//2
				num = nums[k][0]
				if num < newInterval[0]:
					i = k+1
				elif num > newInterval[0]:
					j = k-1
				else:
					pass # shouldn't happen because we caught the overlap
				#insert it over here

		return nums[:i+1] + nums[(i+1)+(combined-1):]



# argv[1]
# print(Solution())
