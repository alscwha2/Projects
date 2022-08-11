'''
Straightfowrad solution with itertools
'''

from itertools import takewhile


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign, s = \
            (-1, s[1:]) if s.startswith('-') else\
            (1, s[1:]) if s.startswith('+') else\
            (1, s)
        ans = ''.join(takewhile(lambda x: x.isnumeric(), s))
        ans = 0 if not ans else sign * int(ans)
        ans = max(ans, -1 * pow(2, 31))
        ans = min(ans, pow(2, 31) - 1)
        return ans
