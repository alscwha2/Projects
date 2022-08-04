from typing import List
from sys import argv as argv

'''
	compare each word to the word before it

	Time: O(N)
	Space: Depends on implementation of iter function, could either be O(1) or O(N)
'''

class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		order = {char:i for i,char in enumerate(order)}
		def isSorted(w1, w2):
			for pair in zip(w1,w2):
				placement = order[pair[0]] - order[pair[1]]
				if placement > 0:
					return False
				elif placement < 0:
					return True
			return len(w1) <= len(w2)

		for i in range(1, len(words)):
			if not isSorted(words[i-1], words[i]):
				return False
		return True

# argv[1]
# print(Solution())
