from typing import List
from sys import argv as argv

'''
	Union-Find

	Constant space solution, sort of. We're not making any more big data structures, but we are replacing ints in the grid
		with tuples. So there is a lot of object creation there. Theoretically unless the size of the grid were too large,
		we could use ints to represent the tuples and then it would really be constant space. Worst case scenario this is 
		linear space.
'''
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		self.numIslands = 0
		def union(a,b):
			a_root, b_root = find(a), find(b)
			if a_root != b_root:
				grid[a_root[0]][a_root[1]] = b_root
				self.numIslands -= 1
		def find(a):
			root = a
			while grid[root[0]][root[1]] != root:
				root = grid[root[0]][root[1]]
			while a != root:
				parent = grid[i][j]
				grid[i][j] = root
				a = parent
			return root

		m,n = len(grid), len(grid[0])

		for i in range(m):
			for j in range(n):
				if grid[i][j] == '1':
					grid[i][j] = (i,j)
					self.numIslands += 1
					if i != 0 and grid[i-1][j] != '0':
						union((i,j),(i-1,j))
					if j != 0 and grid[i][j-1] != '0':
						union((i,j),(i,j-1))

		answer, self.numIslands = self.numIslands, 0
		return answer


# argv[1]
# print(Solution())
