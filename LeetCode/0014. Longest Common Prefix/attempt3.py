from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for chars in zip(*strs):
            if len(set(chars)) > 1:
                return result
            result += chars[0]
        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))