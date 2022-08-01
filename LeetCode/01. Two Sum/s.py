from typing import List
from sys import argv as argv

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i,num in enumerate(nums):
        	needed = target-num
        	if needed in map:
        		return [map[needed], i]
        	else:
        		map[num] = i

# argv[1]
print(Solution())
