from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        cookie_index = 0
        child_index = 0
        while cookie_index < len(s) and child_index < len(g):
            if s[cookie_index] >= g[child_index]:
                child_index += 1
            cookie_index += 1
        return child_index
