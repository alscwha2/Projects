from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        total = 0

        rows = [sum(row) for row in mat]
        columns = [sum(column) for column in zip(*mat)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and columns[j] == 1:
                    total += 1
        return total


print(Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
