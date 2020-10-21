from sys import argv
from typing import List

"""
This was the first working solution. It is kind of brute forcing it. 
I don't like this solution and it isn't so fast.
The only hard part of this problem is how to deal with the star.
The way that I dealt with that in this attempt was that whenever a star was encountered 
	it would check if the string was accepted with 0 matches
	then 1 match. 2 match. etc. calling itself recursively


Trivially easy as long as there is no non-determinism
non-determinism in this problem happens only when you have a*a or .*a where a is any char
* consumes any amount of a single character in a row
	Assume the worst, go to the end of the string of the starred character
	start matching backwards

What are the cases?
	a*.
	.*.
	.*a
	a*a
	a*..
	.*..
	.*aa
	a*aa
	etc


class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		tokens = p.split('*')


	def simpleMatch(self, s: str, p: str) -> bool:
		s = list(s)
		p = list(p)
		while s != [] and p != []:
			if not self.charMatch(s.pop(0), p.pop(0)):
				return False
		return s == [] and p == []


	def charMatch(self, s: str, p: str) -> bool:
		return s == p or p == '.'



"""


class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		s = list(s)
		p = list(p)

		while s != [] and p != []:
			schar = s.pop(0)
			pchar = p.pop(0)

			if len(p) > 0:
				if p[0] == '*':
					s.insert(0, schar)
					p.pop(0)
					if self.isMatch(str(''.join(s)), str(''.join(p))):
						return True
					while s != [] and self.charMatch(s.pop(0), pchar):
						if self.isMatch(str(''.join(s)), str(''.join(p))):
							return True

					return False

			if not self.charMatch(schar, pchar):
				return False
		if s == [] and p != []:
			return self.acceptsEmpty(p)

		return s == [] and p == []

	def charMatch(self, s: str, p: str) -> bool:
		return s == p or p == '.'

	def acceptsEmpty(self, p: List[str]) -> bool:
		if len(p) % 2 == 1:
			return False
		for i in range(0, len(p), 2):
			if p[i + 1] != '*':
				return False
		return True


print(Solution().isMatch(argv[1], argv[2]))