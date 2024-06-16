class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        vowel_subsequence = [char for char in s if char in vowels]
        return ''.join(char if char not in vowels else vowel_subsequence.pop() for char in s)
