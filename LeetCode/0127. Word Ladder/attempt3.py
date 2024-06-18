from collections import defaultdict
from typing import List

"""
    Brilliant idea from someone in the commments
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def starred_words(word):
            for i in range(len(word)):
                yield word[:i] + '*' + word[i+1:]

        graph = defaultdict(set)
        for word in wordList:
            for starred_word in starred_words(word):
                graph[starred_word].add(word)

        def bfs(beginWord, endWord, graph):
            seen = set()
            stack = [beginWord]
            aux_stack = []
            sequence_length = 1
            while stack:
                for node in stack:
                    seen.add(node)
                    if node == endWord:
                        return sequence_length
                    for starred_word in starred_words(node):
                        aux_stack.extend(neighbor for neighbor in graph[starred_word] if neighbor not in seen)
                stack = aux_stack
                aux_stack = []
                sequence_length += 1
            return 0

        return bfs(beginWord, endWord, graph)
