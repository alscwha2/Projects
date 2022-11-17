from collections import defaultdict
from itertools import pairwise, chain, zip_longest
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # find the letter order edges from the word list
        edges = []
        for word1, word2 in pairwise(words):
            for letter1, letter2 in zip_longest(word1, word2):
                if letter1 != letter2:
                    if letter2 is None:
                        return ''
                    elif letter1 is not None:
                        edges.append((letter1, letter2))
                    break

        letters = set(chain(*words))
        sources = letters.copy()

        # turn the word ordering edges into adjacency list and transpose
        adjacency_list = defaultdict(set)
        transpose = defaultdict(set)

        # build adjacency list and transpose
        # if a letter is a child then it is not a source
        for a, b in edges:
            adjacency_list[a].add(b)
            transpose[b].add(a)
            sources.discard(b)

        sources = list(sources)

        order = []

        # kahn's algorithm
        while sources:
            letter = sources.pop()
            order.append(letter)
            for child in adjacency_list[letter]:
                transpose[child].remove(letter)
                if not transpose[child]:
                    sources.append(child)

        # if we haven't managed to use all of the letters then there must be a
        #   cycle and it is impossible
        return ''.join(order) if set(order) == letters else ''


print(Solution().alienOrder(["ac","ab","zc","zb"]))
