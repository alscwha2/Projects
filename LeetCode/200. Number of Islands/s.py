from typing import List
from sys import argv as argv

'''
	Union-Find
	N calls to add

'''

class UnionFind:
	numComponents = 0
	group = {}

	def union(self, a,b):
		if self.find(a) != self.find(b):
			self.group[self.find(a)] = self.find(b)
			self.numComponents -= 1

	def find(self, a):
		root = a
		while self.group[root] != root: 
			root = self.group[root]
		while a != root: 
			parent = self.group[a]
			self.group[a] = root
			a = parent
		return root

	def add(self, a):
		self.group[a] = a
		self.numComponents += 1

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		uf = UnionFind()
		m,n = len(grid), len(grid[0])

		for i in range(m):
			for j in range(n):
				if grid[i][j] == '1':
					uf.add((i,j))
					if i != 0 and grid[i-1][j] == '1':
						uf.union((i,j),(i-1,j))
					if j != 0 and grid[i][j-1] == '1':
						uf.union((i,j),(i,j-1))

		return uf.numComponents


# argv[1]
# print(Solution())
