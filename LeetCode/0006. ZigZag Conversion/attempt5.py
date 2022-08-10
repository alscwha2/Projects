"""
Solution using itertools.
"""


from itertools import cycle


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        next_row = cycle(rows + rows[numRows - 2: 0: -1])
        for char in s:
            next(next_row).append(char)
        return "".join(["".join(row) for row in rows[:numRows]])


print(Solution().convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")
