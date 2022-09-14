from typing import List
from sys import argv as argv

'''
	Well this was straightforward...
	Note that I accidentally used 'i' twice in two nested loops. but it still works because I didn't 
		need the first one anymore. sooo....
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for i in range(9)]
        boxes = None
        for i, row in enumerate(board):
            if i % 3 == 0:
                boxes = [set() for i in range(3)]
            seen = set()
            for i, n in enumerate(row):
                if n == ".": continue
                box = boxes[i // 3]
                column = columns[i]
                if n in seen or n in box or n in column:
                    return False
                seen.add(n)
                box.add(n)
                column.add(n)
        return True


# argv[1]
print(Solution())
