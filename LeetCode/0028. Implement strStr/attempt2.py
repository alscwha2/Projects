class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(1 + (len(haystack) - len(needle))):
            if needle == haystack[i : i + len(needle)]:
                return i
        return -1
