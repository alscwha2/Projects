"""
    Using recursion. O(N) speed, O(N ** 2) space


"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            if len(p) >= 2 and p[1] == '*':
                return self.isMatch(s, p[2:])
            else:
                return False

        def first_char_matches():
            return s[0] == p[0] or p[0] == '.'

        if len(p) > 1 and p[1] == '*':
            if self.isMatch(s, p[2:]):
                return True
            if first_char_matches():
                return self.isMatch(s[1:], p)

        if first_char_matches():
            return self.isMatch(s[1:], p[1:])
        return False

print(Solution().isMatch('aaa','a*'))
