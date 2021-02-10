from typing import List
from sys import argv as argv

class UnionFind:
	def __init__(self, n=0):
		self.group = [i for i in range(n)]
		self.numGroups = n

	def find(self,a):
		root = a
		while self.group[root] != root:
			root = self.group[root]
		while a != root:
			parent = self.group[a]
			self.group[a] = root
			a = parent
		return root

	def union(self,a,b):
		aroot, broot = self.find(a), self.find(b)
		if aroot != broot:
			self.group[aroot] = broot
			self.numGroups -= 1 


class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n = len(isConnected)
		uf = UnionFind(n)
		for i in range(n):
			for j in range(i):
				if isConnected[i][j]:
					uf.union(i,j)
		return uf.numGroups
		

# argv[1]
# print(Solution())
