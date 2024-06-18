from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        def wordList_to_graph(wordList):
            wordSet = set(wordList)
            graph = defaultdict(set)
            for word in wordSet:
                for i, char in enumerate(word):
                    for j in range(1, 26):
                        new_char = chr((ord(char) - 97 + j) % 26 + 97)
                        new_word = word[:i] + new_char + word[i+1:]
                        if new_word in wordSet:
                            graph[word].add(new_word)
            return graph

        graph = wordList_to_graph(wordList)

        def bfs(beginWord, endWord, graph):
            seen = set()
            stack = [beginWord]
            aux_stack = []
            sequence_length = 1
            while stack:
                for node in stack:
                    if node == endWord:
                        return sequence_length
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            aux_stack.append(neighbor)
                        seen.add(neighbor)
                stack = aux_stack
                aux_stack = []
                sequence_length += 1
            return 0

        return bfs(beginWord, endWord, graph)
