from itertools import product
from typing import List


"""
Construct Adjacency List
keep track of seen nodes by changing the value of the matrix to the negative of
    the longest path rooted at that node. Since all of the values are positive,
    we can use the negative as a sign for a seen node. It also functions as the 
    cache to store our memo
    
def path_length:
    if value(cell) is negative:
        return -value(cell)
        
    length = 1 + max(path_length(neighbor) for neighbor in neighbors)
    
    value(cell) = -length
    
return max(path_length(cell) for cell in cells)

"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        ########################################################################
        ###################### MATRIX FUNCTIONS ################################
        ########################################################################

        def cells():
            return product(range(m), range(n))

        def value(coordinates) -> int:
            i, j = coordinates
            return matrix[i][j]

        def set_value(coordinates, val):
            i, j = coordinates
            matrix[i][j] = val

        ########################################################################
        ################# ADJACENCY LIST FUNCTIONS #############################
        ########################################################################

        def create_adjacency_lists():
            neighbors = [[None for _ in range(n)] for __ in range(m)]

            def potential_neighbors(cell):
                i, j = cell
                return [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]

            def set_neighbors(cell, _neighbors):
                i, j = cell
                neighbors[i][j] = _neighbors

            def within_matrix_bounds(coordinates):
                x, y = coordinates
                return (0 <= x <= m-1) and (0 <= y <= n-1)

            for cell in cells():
                val = value(cell)
                greater_neighbors = []
                for neighbor in potential_neighbors(cell):
                    if within_matrix_bounds(neighbor) and val > value(neighbor):
                        greater_neighbors.append(neighbor)
                set_neighbors(cell, greater_neighbors)

            return neighbors

        adjacency_lists = create_adjacency_lists()

        def children(cell):
            i, j = cell
            return adjacency_lists[i][j]

        ########################################################################
        ########################### APPLICATION LOGIC ##########################
        ########################################################################

        def path_length(cell):
            set_value(cell, -1)

            for child in children(cell):
                if value(child) >= 0:
                    path_length(child)
                if value(child) - 1 < value(cell):
                    set_value(cell, value(child) - 1)

            return -value(cell)

        return max(path_length(cell) for cell in cells() if value(cell) >= 0)


print(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
