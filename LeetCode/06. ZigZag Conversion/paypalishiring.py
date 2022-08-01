class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows is 1:
            return s
        
        str = ""
        columnSpacer = 2 * numRows - 2;
        for row in range(numRows):
            index = row
            column = 1
            while index < len(s):
                str += s[index]
                nextColumn = row + column * columnSpacer
                index = nextColumn - (2 * row) if (index - row) % columnSpacer == 0 and row != numRows - 1 else nextColumn
                if index == nextColumn:
                    column = column + 1;
        
        return str

print(Solution.convert(1, "PAYPALISHIRING", 3))