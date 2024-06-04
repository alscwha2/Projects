class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        pairs = set(zip(s, t))
        keys = [pair[0] for pair in pairs]
        values = [pair[1] for pair in pairs]
        return len(keys) == len(set(keys)) and len(values) == len(set(values))
