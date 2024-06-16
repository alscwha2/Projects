from typing import List
from heapq import heappush, heappushpop


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        for num in set(nums):
            if len(heap) < 3:
                heappush(heap, num)
            else:
                heappushpop(heap, num)
        return max(heap) if len(heap) < 3 else min(heap)
