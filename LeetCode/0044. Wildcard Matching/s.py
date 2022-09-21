from functools import cache


class Solution:
	@cache
	def isMatch(self, s: str, p: str) -> bool:
		for i, (s_char, p_char) in enumerate(zip(s, p)):
			if p_char == '*':
				return self.isMatch(s[i:], p[i + 1:]) \
					or self.isMatch(s[i + 1:], p[i:])
			if s_char != p_char and p_char != '?':
				return False

		non_stars_remaining = set(p[len(s):]) - {'*'}
		return len(s) <= len(p) and not non_stars_remaining

a = "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
b = "***bba**a*bbba**aab**b"
ans = Solution().isMatch(a, b)
print(ans)