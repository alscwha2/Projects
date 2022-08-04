from typing import List
from sys import argv as argv
from collections import defualtdict

'''
	Linear time:
		One pass through String
		One pass through fixed-size dict

	Constant space:
		dict can only be 26 entries long
		groups also can only be a maximum of 26 entries long

	I really like the solution on the solution doc. But he does two loops through the string and O(N) calls to the dict.
	Here's his code, I changed variable names and moved stuff around to make it more clear:

		class Solution(object):
		    def partitionLabels(self, S):
		        lastOccurance = {letter: i for i, letter in enumerate(S)}

		        groups = []
		        beginningOfInterval = endOfInterval = 0
		        for i, letter in enumerate(S):
		            endOfInterval = max(endOfInterval, lastOccurance[letter])
		            if i == endOfInterval:
		                groups.append(i - beginningOfInterval + 1)
		                beginningOfInterval = i + 1
		            
		        return groups
'''

class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		# keep track of the interavals needed for each letter
		i = 0
		letters = defualtdict(lambda :[i,i])
		for i,letter in enumerate(S):
			letters[letter][1] = i

		groups = []

		# find all of the overlapping intervals and combine them
		# add the sizes of all of the disjoint interavals to the groups list
		beginningOfInterval, endOfInterval = 0, 0
		for start,end in letters.values():
			if start > endOfInterval:
				groups.append(endOfInterval - beginningOfInterval + 1)
				beginningOfInterval, endOfInterval = start, end
			else:
				endOfInterval = max(endOfInterval, end)

		# you will always be left with one unprocessed interval at the end of iteration
		#    unless S is the empty string
		if S:
			groups.append(endOfInterval - beginningOfInterval + 1)

		return groups

# argv[1]
# print(Solution())
