from typing import List
from sys import argv as argv

class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		if not s1:
			return s2 == s3
		if not s2:
			return s1 == s3
		if not s3:
			return False

		memo = dict()
		def backtrack(i=0,j=0):
			k = i+j
			if (i,j) in memo:
				return memo[(i,j)]
			elif i == len(s1):
				memo[(i,j)] = s2[j:] == s3[k:]
			elif j == len(s2):
				memo[(i,j)] = s1[i:] == s3[k:]
			elif k == len(s3):
				memo[(i,j)] = False
			elif s3[k] == s1[i]:
				if s3[k] == s2[j]:
					memo[(i,j)] = backtrack(i+1, j) or backtrack(i, j+1)
				else:
					memo[(i,j)] = backtrack(i+1, j)
			elif s3[k] == s2[j]:
				memo[(i,j)] = backtrack(i, j+1)
			else:
				memo[(i,j)] = False
			return memo[(i,j)]

		return backtrack()


# argv[1]
print(Solution().isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
