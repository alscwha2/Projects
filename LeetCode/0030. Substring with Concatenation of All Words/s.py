from typing import List
# from sys import argv as argv

'''
	Keep in mind that all of the words are of the same length

	1:
		create all possible concatenations
		for s in concats:
			find all instances in string

	2:
		for each char in string:
			seach all strings to see if it fits,
			for each one where it fits:
				see if it matches the whole word,
				if so:
					create duplicate set, delete entry
					repeat until set is empty
					add to list of indices
'''

class TrieNode:
	def __init__(self, val: str):
		self.val = val
		self.children = {}

class Solution:

	def findSubstring(self, s: str, words: List[str]) -> List[int]:
		combination_length = len(words[0]) * len(words)

		trie = self.construct_trie(words)
		for child in trie.children:
			print(child)
			self.printChildren(trie.children[child])
		combinations = self.construct_combinations(words)
		indices = []

		for i in range(len(s) - combination_length):
			current = trie
			is_valid = True
			for j in range(i, i + combination_length):
				if not s[j] in current.children:
					is_valid = False
					break
				current = current.children[s[j]]
			if is_valid:
				indices.append(i)

		return indices

	def printChildren(self, c: TrieNode):
		print(c.val)
		for t in c.children:
			self.printChildren(c.children[t])



	def construct_combinations(self, words: List[str]):
		# base case
		if len(words) == 1:
			return words

		# recurseive case
		combinations = []
		for word in words:
			copy = words.copy()
			copy.remove(word)
			for rest in self.construct_combinations(copy):
				combinations.append(word + rest)
		return combinations

	def construct_trie(self, combinations: List[str]) -> TrieNode:
		head = TrieNode(None)

		for string in combinations:
			current = head
			for char in string:
				if not char in current.children:
					current.children[char] = TrieNode(char)
				current = current.children[char]

		return head
		

# argv[1]
# print(Solution().construct_combinations(['1','2','3','4','5']))


print(Solution().findSubstring("barfoothefoobarman",["foo","bar"]))