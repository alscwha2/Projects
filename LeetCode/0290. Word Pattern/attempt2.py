from collections import defaultdict
from itertools import count


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def rename_unique_elements(iterable):
            counter = count()
            lookup = defaultdict(counter.__next__)
            return [lookup[elem] for elem in iterable]
        return rename_unique_elements(pattern) == rename_unique_elements(s.split(' '))
