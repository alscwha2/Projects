from sys import argv
from typing import List

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		ref = {
			'2' : ['a', 'b', 'c'],
			'3' : ['d', 'e', 'f'],
			'4' : ['g', 'h','i'],
			'5' : ['j', 'k', 'l'],
			'6' : ['m', 'n', 'o'],
			'7' : ['p', 'q', 'r', 's'],
			'8' : ['t', 'u', 'v'],
			'9' : ['w', 'x', 'y', 'z']
		}

		list = []
		if len(digits) != 0:
			for letter in ref[digits[0]]:
				if len(digits) == 1:
					list.append(letter)
				else:
					for combination in self.letterCombinations(digits[1:]):
						list.append(letter + combination)
		return list

print(Solution().letterCombinations(argv[1]))