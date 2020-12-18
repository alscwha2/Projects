from typing import List
from sys import argv as argv

'''
	Same thing but opposite direction
'''

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		paths = [[-1 for i in range(n)] for j in range(m)]

		def findPaths(a,b):
			if paths[a][b] != -1:
				return paths[a][b]
			if obstacleGrid[a][b]:
				return 0
			if a == m-1 and b == n-1:
				return 1
			answer = 0
			if a < m-1:
				answer += findPaths(a+1,b)
			if b < n-1:
				answer += findPaths(a,b+1)
			paths[a][b] = answer
			return answer

		return findPaths(0,0)


# argv[1]
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))