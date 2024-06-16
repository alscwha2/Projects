class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        vowel_indices = []
        vowel_subsequence = []
        for i, char in enumerate(s):
            if char in vowels:
                vowel_indices.append(i)
                vowel_subsequence.append(char)
        vowel_subsequence.reverse()
        s = [char for char in s]
        for i, char in zip(vowel_indices, vowel_subsequence):
            s[i] = char
        return ''.join(s)
