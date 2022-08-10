"""
Solution jumping around to visit each character in order.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        zigzag = ''
        cycle_length = 2 * numRows - 2

        # first row
        for offset in range(0, len(s), cycle_length):
            zigzag += s[offset]
        # middle rows
        for row in range(1, numRows - 1):
            index = row
            while index < len(s):
                # add element on the column
                zigzag += s[index]

                # add element on the zig
                next_index = index + ((numRows-1)-row) * 2
                if next_index < len(s):
                    zigzag += s[next_index]

                # go to next column
                index += cycle_length

        # last row
        for offset in range(numRows - 1, len(s), cycle_length):
            zigzag += s[offset]

        return zigzag


print(Solution().convert("PAYPALISHIRING", 3))
print("PAHNAPLSIIGYIR")
