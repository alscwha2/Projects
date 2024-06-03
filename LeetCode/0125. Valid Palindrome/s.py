from curses import ascii

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(ascii.isalnum, s)).lower()
        return s == s[::-1]
