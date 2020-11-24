from typing import List
from sys import argv as argv

'''
	Iterate through the string keeping track of the open/close ratio.
	keep track of max
	once it falls below zero, start over again
	^ this has the problem that it doesn't sense (()
	^ Revisited this in attempt2

	Another idea:
		find all of '()'
		then move outwards:
			if two are text to eachother, combine
			check if each group is surrounded by ()
			keep doing until entire string is done


'''
class Solution:
	def longestValidParentheses(self, s: str) -> int:
		def findAllPairs(s: str) -> List[tuple]:
			indices = []
			previousIsOpen = False
			for i in range(len(s)):
				c = s[i]
				if c == '(':
					previousIsOpen = True
				if c == ')':
					if previousIsOpen:
						indices.append((i-1, i))
					previousIsOpen = False
			return indices

		def findSurrounded(s: str, groups: List[tuple]) -> bool:
			madeChanges = False
			for i in range(len(groups)):
				group = groups[i]
				if group[0] - 1 < 0 or group[1] + 1 >= len(s):
					continue
				if s[group[0]-1] == '(' and s[group[1]+1] == ')':
					groups[i] = (group[0]-1, group[1]+1)
					madeChanges = True
					i -= 1
			return madeChanges

		def findNeighbors(groups: List[tuple]):
			madeChanges = False

			newgroups = groups[:1]

			while not groups == []:
				first = newgroups.pop()
				second = groups.pop(0)
				if first[1] == second[0]-1:
					newgroups.append((first[0], second[1]))
					madeChanges = True
				else:
					newgroups.append(first)
					newgroups.append(second)
			groups.extend(newgroups)
			return madeChanges

		# find all of he '()' substrings
		groups = findAllPairs(s)
		if groups == []:
			return 0

		# keep on checking whether any of the groups are enclosed by parens or next to each other
		foundMore = True
		while foundMore:
			foundMore = findSurrounded(s, groups)
			foundMore = foundMore or findNeighbors(groups)

		# find the largest group
		longest = 0
		for group in groups:
			length = group[1]+1 - group[0]
			longest = length if length > longest else longest

		return longest





		
print(Solution().longestValidParentheses('(()()()()(()))'))


'''
biggestSeen = 0
beginningIndex = 0
remainingToClose = 0

for i in range(len(s)):
	c = s[i]
	if c == '(':
		remainingToClose += 1
	if c == ')':
		remainingToClose -= 1
	if remainingToClose == 0:
		currentStreak = (i+1) - beginningIndex
		biggestSeen = max(currentStreak, biggestSeen)
	if remainingToClose < 0:
		remainingToClose = 0
		beginningIndex = i + 1
return biggestSeen

'''