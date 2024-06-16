from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0,1]
        while len(bits) < n+1:
            bits = bits + [bit+1 for bit in bits]
        return bits[:n+1]
