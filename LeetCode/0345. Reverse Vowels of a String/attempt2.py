class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        vowel_indices = [i for i, char in enumerate(s) if char in vowels]
        vowel_subsequence = [char for char in s if char in vowels]
        s = [char for char in s]
        vowel_subsequence.reverse()
        for i, char in zip(vowel_indices, vowel_subsequence):
            s[i] = char
        return ''.join(s)
