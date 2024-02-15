'''
    I tried to use a defaultdict instead and it didn't work.
    The case that fails if you use defualtdict is in the case where the string
    is only one character long. Since the current index is 0 an the index of
    that character in the map is 0 by defualt, that evaulates the current length
    to be 0.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurences = {}
        longest_length = 0
        current_length = 0

        for index, letter in enumerate(s):
            current_length += 1
            if letter in occurences:
                current_length = min(index - occurences[letter], current_length)
            longest_length = max(longest_length, current_length)
            occurences[letter] = index
        return longest_length