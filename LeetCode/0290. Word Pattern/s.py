from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(' ')):
            return False
        lookup = defaultdict(set)
        lookup2 = defaultdict(set)
        for letter, word in zip(pattern, s.split(' ')):
            lookup[letter].add(word)
            if len(lookup[letter]) > 1:
                return False
            lookup2[word].add(letter)
            if len(lookup2[word]) > 1:
                return False
        return True
