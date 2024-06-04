from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        has_odd = False
        for val in counter.values():
            if val % 2:
                has_odd = True
        values = [val for val in counter.values() if val >= 2]
        values = [val-1 if val % 2 else val for val in values]
        total = sum(values)
        if has_odd:
            total += 1
        return total
