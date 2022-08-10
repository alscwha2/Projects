class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        rows = [[] for _ in range(numRows)]
        rows += rows[numRows - 2: 0: -1]

        for i, char in enumerate(s):
            row = i % (numRows * 2 - 2)
            rows[row].append(char)

        return "".join(["".join(row) for row in rows[:numRows]])


print(Solution().convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")
