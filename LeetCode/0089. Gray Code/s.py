class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        previous = self.grayCode(n-1)
        return previous + [num + 2**(n-1) for num in reversed(previous)]
