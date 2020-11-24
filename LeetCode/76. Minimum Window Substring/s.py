from typing import List
from sys import argv as argv
from math import inf as inf

class Solution:
	def minWindow(self, s: str, t: str) -> str:
		# make sure every character is present
		copy = [c for c in s]
		for c in t:
			if c not in copy:
				return ''
			copy.remove(c)

		# record indices
		indices = []

		for i in range(len(s)):
			c = s[i]
			if c in t:
				indices.append(i)

		# set up data structures to keep track of current window
		freq = {c : 0 for c in t}
		amount = {c : 0 for c in t}
		for c in t:
			amount[c] += 1
		needed = [c for c in t]

		# keep track of current shortest window
		shortestLength = inf
		bounds = (-1, -1)

		left = 0
		right = -1
		# start sliding 
		while right < len(indices)-1 or len(needed) == 0:
			if len(needed) == 0:
				leftchar = s[indices[left]]
				freq[leftchar] -= 1
				if freq[leftchar] < amount[leftchar]:
					needed.append(leftchar)
				left += 1
			else:
				right += 1
				rightchar = s[indices[right]]
				freq[rightchar] += 1
				if rightchar in needed:
					needed.remove(rightchar)
			# check if this window broke a record
			if len(needed) == 0:
				windowlength = indices[right] - indices[left] + 1
				if windowlength < shortestLength:
					shortestLength = windowlength
					bounds = (indices[left], indices[right]+1)

		return s[bounds[0] : bounds[1]]

print(Solution().minWindow("bba","ab"))
