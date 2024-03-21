from typing import List
'''
    much cleaner
    uses an additional O(N) space
'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List [int]:
        depths = [0] * len(seq)

        current_depth = 0
        for i, char in enumerate(seq):
            if char == '(':
                current_depth += 1
            depths[i] = current_depth
            if char == ')':
                current_depth -= 1

        return [0 if depth > max(*depths)//2 else 1 for depth in depths]
