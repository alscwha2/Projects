from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class Trie:
            def __init__(self, dictionary):
                self.lookup = {'present':False}
                for word in dictionary:
                    self.insert(word)

            def insert(self, word: str) -> None:
                lookup = self.lookup
                for letter in word:
                    if not letter in lookup:
                        lookup[letter] = {'present':False}
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
