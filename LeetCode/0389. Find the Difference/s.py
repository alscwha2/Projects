from collections import Counter

"""
    Someone else's code:

    class Solution:
        def findTheDifference(self, s: str, t: str) -> str:
            return chr(reduce(operator.xor, map(ord, s + t)))

    Very cool. The ord function maps ASCII to it's integer value, and chr maps the 
    integer value back to ASCII
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]
