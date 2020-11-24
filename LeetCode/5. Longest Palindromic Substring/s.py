class Solution:
	def longestPalindrome(self, s: str) -> str:
		'''
			for each char
				scan left for duplicates
				treat as center
				compare right to left
				keep track of biggest
		'''
		
		biggestSeen = 0
		biggestIndex = 0
		
		# treat each character as if it can be the center
		i = 0		
		while i < len(s):

			# count the length of the center of the palindrome
			centerLength = 1
			while i+centerLength < len(s) and s[i+centerLength] == s[i]:
				centerLength += 1
			
			# compare left and right neighbors of the palindrome
			surroundingLength = 0
			while True:
				leftBound = i - (surroundingLength+1)
				rightBound = i + centerLength + surroundingLength
				
				# make sure they're in bounds
				if leftBound < 0 or rightBound >= len(s):
					break

				# make sure they match
				if s[leftBound] == s[rightBound]:
					surroundingLength += 1
				else:
					break
			
			# update biggest seen
			totalLength = centerLength + 2*surroundingLength
			if totalLength > biggestSeen:
				biggestSeen = totalLength
				biggestIndex = i - surroundingLength

			# we get to skip over all of the characters in the center of the palindrome
			i += centerLength
		
		return s[biggestIndex:biggestIndex+biggestSeen]
		