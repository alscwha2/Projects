"""
Took inspiration from someone on leetcode to use enumerate
to cut down the code further
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = -1
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return strs[0][: i + 1]

print(Solution().longestCommonPrefix(["flower","flow",""]))