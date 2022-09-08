"""
    Modified to use a sliding window
"""

from typing import List
from collections import deque, Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        total_concat_length = word_length * len(words)

        indices = []
        for i in range(word_length):
            needed = Counter(words)
            current = deque()

            for j in range(i, 1 + len(s) - word_length, word_length):
                word = s[j:j + word_length]
                current.append(word)
                if word not in words:
                    needed = Counter(words)
                    current = deque()
                elif needed[word]:
                    needed[word] -= 1
                else:
                    while current:
                        last = current.popleft()
                        if last == word:
                            break
                        else:
                            needed[last] += 1
                if len(current) == len(words):
                    indices.append(j - total_concat_length + word_length)

        return indices


print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))

