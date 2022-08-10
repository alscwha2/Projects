"""
Solution using itertools.
"""


from itertools import cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        row_cycle = cycle(rows + rows[numRows - 2: 0: -1])
        for char in s:
            next(row_cycle).append(char)
        return "".join(["".join(row) for row in rows])


print(Solution().convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")
