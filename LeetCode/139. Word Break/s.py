from typing import List
from sys import argv as argv
from collections import defaultdict

'''
	for this one I would like a TRIE

        It seems that this is never going to work because of time limit
        Have to find a new strategy
'''


class Trie:
    def __init__(self, exists=False, wordDict=None):
        self.exists = exists
        self.neighbors = defaultdict(Trie)

        if wordDict:
            for word in wordDict:
                current = self
                for letter in word:
                    current = current.neighbors[letter]
                current.exists = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie(wordDict=wordDict)

        def helper(index):
            current = trie
            i = index
            for i in range(index, len(s)):
                letter = s[i]
                if letter not in current.neighbors:
                    return False
                current = current.neighbors[letter]
                if current.exists and helper(i+1):
                    return True
            return current.exists

        return helper(0)


# argv[1]
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", [
      "a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
