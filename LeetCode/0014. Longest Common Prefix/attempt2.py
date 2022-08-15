from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for chars in zip(*strs):
            char = chars[0]
            for next_char in chars:
                if next_char != char:
                    return result
            result += char
        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))