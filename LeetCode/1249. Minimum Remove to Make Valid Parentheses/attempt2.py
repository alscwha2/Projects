from typing import List
from sys import argv as argv

'''
    The idea is to keep track of the ratio between openers and closers.
    If there are ever more closers than openers, remove the extra ones.
    If there are more openers than closers, iterate from the baack of the array
        and remove the openers that you find until you've removed enough.
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer = [char for char in s]
        ratio = 0
        for i, char in enumerate(s):
            if char == '(':
                ratio += 1
            elif char == ')':
                if ratio == 0:
                    answer[i] = ''
                else:
                    ratio -= 1

        print(ratio)
        i = len(s) - 1
        while ratio > 0:
            while answer[i] != '(':
                i -= 1
            answer[i] = ''
            ratio -= 1

        return ''.join(answer)

print(Solution().minRemoveToMakeValid('))(('))
