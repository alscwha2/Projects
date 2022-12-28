from bisect import bisect, bisect_left
from typing import List
"""
	* search for insertion spot
	* search for last overlapping interval
	* replace that slice with new interval
	* fix the boundaries of the new interval by combining
	* return
	
	cases to worry about: 
	(=, =)
	(>, =)
	(=, >)
	(>, >)
	
	if newInterval fits neatly in between two other intervals:
		insertionIndex, last_overlap_index = i, i
		therefore nothing will be deleted and it will just be inserted
		and 
			newInterval[beginning] = min(newInterval[beginning], intervals[insertion_index][beginning])
			will by definition be newInterval[beginning]
	
	if newInterval fits entirely inside another interval:
		insertion_index, last_overlap_index = i, i+1
		this is because insertion_index uses bisect_left and last_overlap_index uses bisect_right
		
			newInterval[beginning] = min(newInterval[beginning], intervals[insertion_index][beginning])
	
			newInterval[end] = max(newInterval[end], intervals[last_overlap_index-1][end])
			
			these both will expand to encompass the original interval
			therefore the original interval will just be replaced with itself.
	"""


class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		BEGINNING, END = 0, 1
		
		# find the indices where newInterval will be inserted, and where it will end
		insertion_index = bisect_left(intervals, newInterval[BEGINNING], key=lambda interval: interval[END])
		index_after_end = bisect(intervals, newInterval[END], key=lambda interval: interval[BEGINNING])
		
		# merge with overlapping intervals
		if insertion_index < len(intervals):
			newInterval[BEGINNING] = min(newInterval[BEGINNING], intervals[insertion_index][BEGINNING])
		if index_after_end > insertion_index:
			newInterval[END] = max(newInterval[END], intervals[index_after_end-1][END])
		
		# replace overlapping intervals and insert newInterval
		intervals[insertion_index:index_after_end] = [newInterval]
		return intervals
