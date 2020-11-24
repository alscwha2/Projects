from typing import List
from sys import argv as argv
from collections import deque as deque


'''
	I really don't understand why this was listed as a hard problem on Leetcode

'''
class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

		# -------------------------------- FUNCTION ----------------------------------------------
		# function to turn tokens into properly formatted line
		def lineify(words: deque, spaces: int):
			if len(words) == 1:
				word = words[0]
				return word.ljust(len(word)+spaces)

			gaps = len(words)-1
			spacesPer = spaces//gaps + 1
			numExtra = spaces % gaps

			line = words.popleft()

			for i in range(numExtra):
				line = line.ljust(len(line) + spacesPer + 1) + words.popleft()
			for i in range(gaps-numExtra):
				line = line.ljust(len(line) + spacesPer) + words.popleft()
			return line
		
		#--------------------------- CODE STARTS HERE --------------------------------------------

		lines = []
		tokens = deque([words.pop(0)])
		spaceLeft = maxWidth - len(tokens[0])

		for word in words:
			length = len(word)

			# if you can't fit this on the current line
			if spaceLeft - (length+1) < 0:
				lines.append(lineify(tokens,  spaceLeft))
				tokens = deque([word])
				spaceLeft = maxWidth-length
			# if you can fit it on current line
			else:
				tokens.append(word)
				spaceLeft -= (length+1)

		# last line is just left justified
		lines.append(' '.join(tokens).ljust(maxWidth))

		return lines

		
lines = Solution().fullJustify(argv[1].split(' '),int(argv[2]))
for line in lines:
	print(line, len(line))