import sys
from typing import List

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

'''
	problems with the previous method:
		lots of repeated strings, needing a set
		repeated string slicing and concatonation. doesn't just produce the results straight

	what is possible with this problem:
		each string is going to be of length 2n
		impossible to get better than O(n^2)

	
	Had this idea. gave me a lot of trouble because I was trying to do dynamic programming
		I was trying to make a dictionary outside the scope of the function and use it
		to store all of the previously computed values
		for some reason that didn't work at all!

	Also this has a lot of duplicates and you still need the set badly
	as it is now it runs a lot slower...
'''
# dp = {}
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		if n is 0: return ['']
		if n is 1: return ['()']
		# if n in dp: return dp[n]
		n -= 1

		triplets = []
		for i in range(n+1):
			for j in range(n+1):
				if n-i-j >= 0:
					triplets.append([i, j, n-i-j])

		stringset = set()
		for triplet in triplets:
			for before in self.generateParenthesis(triplet[0]):
				for middle in self.generateParenthesis(triplet[1]):
					for end in self.generateParenthesis(triplet[2]):
						stringset.add(before + '(' + middle + ')' + end)

		# dp[n] = list(stringset)
		# print(n, dp[n])
		return list(stringset)

print(Solution().generateParenthesis(int(sys.argv[1])))