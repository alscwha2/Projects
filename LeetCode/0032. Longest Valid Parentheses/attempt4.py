from typing import List
from functools import reduce


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        def find_middles(s: str) -> List[List[int]]:
            middles = []
            for i in range(1, len(s)):
                if s[i - 1] == '(' and s[i] == ')':
                    middles.append([i - 1, i])
            return middles

        def expand_middles(middles: List[List[int]]) -> List[List[int]]:
            expanded_middles = []
            for l, r in middles:
                while       l > 0 \
                        and r < len(s) - 1 \
                        and s[l - 1] == '(' \
                        and s[r + 1] == ')':
                        l -= 1
                        r += 1
                expanded_middles.append([l, r])
            return expanded_middles

        def merge_middles(middles: List[List[int]]) -> List[List[int]]:
            merged_middles = []
            if middles:
                prev = middles[0]
                for current in middles[1:]:
                    if prev[1] + 1 == current [0]:
                        prev[1] = current[1]
                    else:
                        merged_middles.append(prev)
                        prev = current
                merged_middles.append(prev)
            return merged_middles

        middles = find_middles(s)
        middles = expand_middles(middles)
        merged_middles = merge_middles(middles)
        while merged_middles != middles:
            middles = expand_middles(merged_middles)
            merged_middles = merge_middles(middles)

        return reduce(lambda longest, string: max(longest, string[1]-string[0]+1), middles, 0)


print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))
