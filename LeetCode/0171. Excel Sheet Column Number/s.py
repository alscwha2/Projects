class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lookup = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", (i for i in range(1, 27))))
        return sum(26 ** i * lookup[char] for i, char in enumerate(columnTitle[::-1]))
