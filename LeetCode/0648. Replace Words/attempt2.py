from typing import List
from collections import defaultdict

"""
    Just overcomplicating things by using a defaultdict
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class Trie:
            def __init__(self, dictionary):
                def factory():
                    return defaultdict(factory, {'present': False})

                self.lookup = defaultdict(factory, {'present': False})
                for word in dictionary:
                    self.insert(word)

            def insert(self, word: str) -> None:
                lookup = self.lookup
                for letter in word:
                    lookup = lookup[letter]
                lookup['present'] = True

            def min_prefix(self, word: str) -> str:
                prefix = ''
                lookup = self.lookup
                for letter in word:
                    if letter in lookup:
                        lookup = lookup[letter]
                        prefix += letter
                        if lookup['present']:
                            return prefix
                    else:
                        break
                return word

        trie = Trie(dictionary)
        return ' '.join(trie.min_prefix(word) for word in sentence.split(' '))
