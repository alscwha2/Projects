class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        return n * (n+1) // 2 + max(0, n - k // 2) * (k - k // 2 - 1)
