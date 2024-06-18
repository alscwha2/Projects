class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        less_than_k, more_than_k = (k //2, n - k // 2) if (n >= k // 2) else (n, 0)
        return less_than_k * (less_than_k+1) // 2 + more_than_k * (more_than_k+1) // 2 + more_than_k * (k-1)
