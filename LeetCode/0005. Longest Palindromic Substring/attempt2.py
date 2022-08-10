"""
Solution:
for char in string:
    treat char as center of palindrome
    is palindrome bigger than the biggest palindrome we've seen?

Optimization: if you have a long string of the same letter in the center of the
palindrome this code still tests each one. Ideally you would skip them. You can
do that with a while loop, but it wouldn't be as clean
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_indices = (0, 0)
        for center, char in enumerate(s):
            center_end = center
            while center_end + 1 < len(s) and s[center_end + 1] == char:
                center_end += 1

            while center - 1 >= 0 and center_end + 1 < len(s) \
                    and s[center - 1] == s[center_end + 1]:
                center -= 1
                center_end += 1
            if center_end - center > longest_indices[1] - longest_indices[0]:
                longest_indices = (center, center_end)
        return s[longest_indices[0]:longest_indices[1] + 1]


print(Solution().longestPalindrome("aaaaaasdfghjklkjhgfdsa"))
