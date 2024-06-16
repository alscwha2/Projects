from collections import Counter

"""
    Someone had this awesome code on LC:

    class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return (Counter(ransomNote) - Counter(magazine)) == {}
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote, magazine = Counter(ransomNote), Counter(magazine)
        return all(magazine[letter] >= count for letter, count in ransomNote.items())
