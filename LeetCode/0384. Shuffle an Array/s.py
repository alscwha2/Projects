from random import randint
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        copy = self.nums.copy()
        for last_index in range(len(copy) - 1, -1, -1):
            next_index = random.randint(0, last_index)
            copy[next_index], copy[last_index] = copy[last_index], copy[next_index]
        return copy


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()pass
