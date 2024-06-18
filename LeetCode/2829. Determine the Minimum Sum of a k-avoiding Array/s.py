class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        less_than_k = k // 2
        more_thank_k = n - less_than_k
        if more_thank_k < 0:
            less_than_k = n
            more_thank_k = 0
        return less_than_k * (less_than_k + 1) // 2 + (k-1) * more_thank_k + more_thank_k * (more_thank_k + 1) // 2
        # return sum(range(1, less_than_k+1)) + sum(range(k, k+more_thank_k))


