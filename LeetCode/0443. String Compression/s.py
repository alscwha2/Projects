from typing import List
from sys import argv as argv

'''
	First I kept a running counter of the group length. Other solutions on LeetCode instead kept track of the starting index
		of the current sequence. That is more efficient so I switched to that.

	Even though this is the same method that is the official solution, it's not running so well. whatever.
'''

class Solution:
	def compress(self, chars: List[str]) -> int:
		self.writeHead = 0
		startIndex = 0
		prev = chars[0]

		def write(char, grouplength):
			chars[self.writeHead] = char
			self.writeHead += 1
			if grouplength > 1:
				for n in str(grouplength):
					chars[self.writeHead] = n
					self.writeHead += 1

		for i,char in enumerate(chars):
			if char != prev:
				write(prev, i-startIndex)
				startIndex = i
				prev = char

		write(prev, len(chars)-startIndex)

		return self.writeHead


# argv[1]
print(Solution().compress(["a","a","b","b","c","c","c"]))
