'''
Now rewritten with a while loop
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_indices = (0, 0)
        center = 0
        while center < len(s):
            char = s[center]
            center_end = center
            while center_end + 1 < len(s) and s[center_end + 1] == char:
                center_end += 1

            beginning, end = center, center_end
            while beginning - 1 >= 0 and end + 1 < len(s) and s[beginning - 1] == s[end + 1]:
                beginning, end = beginning - 1, end + 1
            if end - beginning > longest_indices[1] - longest_indices[0]:
                longest_indices = (beginning, end)
            center = center_end + 1
        return s[longest_indices[0]:longest_indices[1]+1]


print(Solution().longestPalindrome("aaaaaasdfghjklkjhgfdsa"))