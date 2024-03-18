from typing import List
from sys import argv as argv
from collections import deque

'''
    Same as attempt2, except use a deque to keep track of the
        openers that you want to remove
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer = [char for char in s]
        last_openers = deque()
        ratio = 0
        for i, char in enumerate(s):
            if char == '(':
                ratio += 1
                last_openers.append(i)
            elif char == ')':
                if ratio == 0:
                    answer[i] = ''
                else:
                    ratio -= 1
                    last_openers.popleft()

        for i in last_openers:
            answer[i] = ''

        return ''.join(answer)

print(Solution().minRemoveToMakeValid('))(('))
