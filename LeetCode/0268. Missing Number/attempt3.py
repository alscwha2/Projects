from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        for num in range(len(nums)+1):
            answer ^= num
        return answer
