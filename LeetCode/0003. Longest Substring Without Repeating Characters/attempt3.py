class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		beginning_index = 0
		longest = 0
		seen = {}
		for i, char in enumerate(s):
			if char in seen and seen[char] >= beginning_index:
				longest = max(longest, i - beginning_index)
				beginning_index = seen[char] + 1
			seen[char] = i
		return max(longest, len(s) - beginning_index)