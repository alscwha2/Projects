"""
    Got this from the LeetCode solution, recreated it step by step
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_char_match = s and (p[0] == s[0] or p[0] == '.')
        next_token_is_star = len(p) > 1 and p[1] == '*'

        if next_token_is_star:
            return self.isMatch(s, p[2:]) \
                or first_char_match and self.isMatch(s[1:], p)
        else:
            return first_char_match and self.isMatch(s[1:], p[1:])

Solution().isMatch('aa', 'a*')