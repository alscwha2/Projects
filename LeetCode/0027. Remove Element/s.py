from typing import List
from sys import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vals = 0
        for i in range(len(nums)):
        	if nums[i] == val:
        		vals += 1
        	else:
        		nums[i - vals] = nums[i]
        return len(nums) - vals

sys.argv[1]
print(Solution())
