from collections import defaultdict
from typing import List

"""
    Brilliant idea from someone in the commments
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        wordLength = len(beginWord)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(wordLength):
                new_word = word[:i] + '*' + word[i+1:]
                graph[word].append(new_word)
                graph[new_word].append(word)

        def bfs(beginWord, endWord, graph):
            seen = set()
            stack = [beginWord]
            aux_stack = []
            sequence_length = 0
            while stack:
                for node in stack:
                    if node == endWord:
                        return sequence_length // 2 + 1
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            aux_stack.append(neighbor)
                        seen.add(neighbor)
                stack = aux_stack
                aux_stack = []
                sequence_length += 1
            return 0

        return bfs(beginWord, endWord, graph)
