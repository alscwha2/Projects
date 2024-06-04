from itertools import zip_longest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def replace_with_numbers(s):
            order = dict(zip_longest(s, [None]))
            lookup = dict(zip(order, range(len(order))))
            return [lookup[char] for char in s]
        return replace_with_numbers(s) == replace_with_numbers(t)
