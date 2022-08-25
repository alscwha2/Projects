"""
    Trying to minimize recursion here
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        string_index = 0
        pattern_index = 0

        # Helper Functions
        def next_char_match():
            return s[string_index] == p[pattern_index] or p[pattern_index] == '.'

        def next_token_is_star():
            return pattern_index + 1 < len(p) and p[pattern_index + 1] == '*'

        def rest_of_pattern_matches_empty_string():
            for char in p[pattern_index + 1 :: 2]:
                if char != '*':
                    return False
            return pattern_index == len(p) or p[-1] == '*'


        while string_index < len(s) and pattern_index < len(p):
            if next_token_is_star():
                if self.isMatch(s[string_index:], p[pattern_index + 2:]):
                    return True
                elif not next_char_match():
                    return False
                else:
                    string_index += 1
            else:  # i.e. not next_token_is_star()
                if not next_char_match():
                    return False
                string_index += 1
                pattern_index += 1

        if string_index == len(s):  # If we've matched the entire string
            if rest_of_pattern_matches_empty_string():
                return True
        return False


print(Solution().isMatch("aab", "c*a*b"))
