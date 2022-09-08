"""
* Are there repeat words?
* There will be no substring words, because they're all the same size
* I don't have to deal with what to do with the empty string
* I don't have to deal with what to do with an empty array

* I want O(LogN) find, and O(1) deletion

* What I really need is a Red-Black tree. I need to be able to keep track
    of which words were already used and whether I used all of them.
    In order to do that I would like to have O(N) lookup, O(1) deletion.
    That is a balanced binary tree.
    Creation would cost O(NlogN).
    So total time complexity would be O(N**2logN)

* Well, turns out that using Hashing was a better alternative, since that
    provides O(1) lookup, O(N) creation, and O(1) deletion.
* So this is now O(N**2), since we're doing N O(1) lookups / deletions
    for each character in the string
"""


from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        total_concat_length = word_length * len(words)

        indices = []
        for i in range(1 + (len(s) - total_concat_length)):
            counter = Counter(words)
            for j in range(len(words)):
                next_word = s[i + j * word_length: i + j * word_length + word_length]
                occurences = counter[next_word]
                if occurences == 1:
                    del counter[next_word]
                elif occurences:
                    counter[next_word] = occurences - 1
                else:
                    break
            if not counter:
                indices.append(i)

        return indices


print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
