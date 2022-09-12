"""
    The goal here was to merge and expand as you go along.
    I thought that this would be faster, but it turns out that it is slower
    Mutual Recursion
"""
from functools import reduce


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def matches(l: int, r: int) -> bool:
            return s[l] == '(' and s[r] == ')'

        def expand(l: int, r: int) -> tuple[int, int]:
            while l > 0 and r < len(s) - 1 and matches(l - 1, r + 1):
                l -= 1
                r += 1
            l, r = merge(l, r)
            return l, r

        def merge(l: int, r: int) -> tuple[int, int]:
            prev = substrings[-1]
            if l == prev[1] + 1:
                l = prev[0]
                substrings.pop()
                return expand(l, r)
            return l, r

        def string_length(bounds: tuple[int, int]) -> int:
            return bounds[1] - bounds[0] + 1

        substrings = [(-1, -2)]
        r = 1
        while r < len(s):
            l = r - 1
            if matches(l, r):
                l, r = expand(l, r)
                substrings.append((l, r))
            r += 1

        longest_substring_length = reduce(lambda length, string: max(length, string_length(string)), substrings, 0)
        return longest_substring_length


print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))
