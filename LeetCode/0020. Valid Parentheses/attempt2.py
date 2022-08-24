from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        openers = ("(", "{", "[")
        closer = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            try:
                if char in openers:
                    stack.append(char)
                elif char is not closer[stack.pop()]:
                    return False
            except IndexError:
                return False
            except KeyError:
                raise ValueError(
                    "Only the following characters are allowed in a string:(){}[]")

        return len(stack) is 0
