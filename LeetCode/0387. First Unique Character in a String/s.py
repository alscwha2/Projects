"""
    here are other solutions on LC

    class Solution:
        def firstUniqChar(self, s: str) -> int:
            for key, val in Counter(s).items():
                if val == 1:
                    return s.index(key)
            return -1

    class Solution:
        def firstUniqChar(s: str) -> int:
            char_count = Counter(s)
            return next((i for i, char in enumerate(s) if char_count[char] == 1), -1)

    apparently the "next" function takes a default parameter. The more you know.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = dict()
        for index, char in enumerate(s):
            lookup[char] = -1 if char in lookup else index
        for index in lookup.values():
            if index != -1:
                return index
        return -1
