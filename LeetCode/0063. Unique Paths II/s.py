from typing import List
from sys import argv as argv

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])

		paths = [[-1 for i in range(n)] for j in range(m)]

		def findPaths(m,n):
			if paths[m][n] != -1:
				return paths[m][n]
			if obstacleGrid[m][n]:
				return 0
			if not m and not n:
				return 1
			answer = 0
			if m-1 >= 0:
				answer += findPaths(m-1,n)
			if n-1 >= 0:
				answer += findPaths(m,n-1)
			paths[m][n] = answer
			return answer

		return findPaths(m-1,n-1)


# argv[1]
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))