'''
	Only thing that I changed here is the way that currentLength is stored. 
	Not sure if this is better
'''

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		longestLength = 0
		
		seen = dict()
		
		startingIndex = 0
		currentLength = 0
		for i in range(len(s)):
			c = s[i]
			if c in seen and seen[c] >= startingIndex:
				startingIndex = seen[c] + 1
				currentLength = i - startingIndex + 1
			else:
				# see if it's the biggest
				currentLength += 1
				if currentLength > longestLength:
					longestLength = currentLength
			seen[c] = i
		
		return longestLength