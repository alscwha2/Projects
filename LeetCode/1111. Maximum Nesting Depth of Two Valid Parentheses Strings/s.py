from typing import List

'''
    first find the max depth of the sequence
    put any part of the sequence that exceeds max_depth // 2 into its own group
'''


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List [int]:
        max_depth = 0
        current_depth = 0
        for char in seq:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        target = max_depth // 2

        current_depth = 0
        answer = [0 for _ in range(len(seq))]
        for i, char in enumerate(seq):
            if char == '(':
                current_depth += 1
            if current_depth > target:
                answer[i] = 1
            if char == ')':
                current_depth -= 1

        return answer
