from functools import reduce

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if len(strs) == 0:
			return ''

		prefix = ''

		for index in range(len(strs[0])):
			char = strs[0][index]

			for str in strs:
				if len(str) <= index or str[index] != char:
					return prefix

			prefix += char

		return prefix
