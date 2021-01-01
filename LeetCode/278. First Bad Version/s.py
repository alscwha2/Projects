from typing import List
from sys import argv as argv

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i,j = 0,n-1
		while i<=j:
			k = i + (j-i)//2
			if isBadVersion(k):
				j = k-1
			else:
				i = k+1
		return i

# argv[1]
# print(Solution())
