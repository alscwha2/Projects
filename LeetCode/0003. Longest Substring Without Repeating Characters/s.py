'''
	Iterate through
	if you haven't seen char before, put in dictionary with index
	if you have seen it before:
		if it's before current starting index, doesn't matter, as if you haven't seen it before
		if it's not:
			we then have to start the current string after that character
				i.e. change starting index to seen[c]+1
	if you haven't seen it before:
		length++
		if it's the biggest, save it
'''

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		longestLength = 0

		seen = dict()
		
		startingIndex = 0
		for i in range(len(s)):
			c = s[i]
			if c in seen and seen[c] >= startingIndex:
				startingIndex = seen[c] + 1
			else:
				# see if it's the biggest
				currentLength = i - startingIndex + 1
				if currentLength > longestLength:
					longestLength = currentLength
			seen[c] = i
		
		return longestLength