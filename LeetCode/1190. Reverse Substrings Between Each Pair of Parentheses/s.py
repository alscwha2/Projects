from typing import List
from collections import deque

'''
    keep track of the indicies of the openers.
    The last opener seen will the beginning point of the next swap
    A closer tells you to swap from the index of the last opener
    remember to remove the parens when you're done
'''

class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = [char for char in s]
        openers = []
        for current_index, char in enumerate(s):
            if char == '(':
                openers.append(current_index)
            if char == ')':
                last_opener = openers.pop()
                answer[last_opener+1:current_index] = answer[current_index-1:last_opener:-1]
                answer[current_index] = answer[last_opener] = ''
        return ''.join(answer)
