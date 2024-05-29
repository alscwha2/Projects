from typing import List
"""
    We are going to change the problem a bit. The Array will be an array of heights
    Treat a 1 and going up 1 level and 0 as going down one level. 
    Convert the array to be an array of the current height based on the ascentions and descentions
    Now the new question is: what are the furthest pair of two equal number?
    If two numbers are equal that means that there was an equal number of ascents and descents between them
    We can find the furthest pair of equal numbers by using a hashmap to map the first sight
    of a number with its index.


    1 = step up
    0 = step down
    convert array into heights
    find two equal heights that are furthest from eachother
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        def convert_array():
            nonlocal nums
            current = 0
            for i, num in enumerate(nums):
                current = (current + 1) if num == 1 else (current - 1)
                nums[i] = current

            nums = [0] + nums

        convert_array()

        longest = 0
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                longest = max(longest, i - seen[num])
            else:
                seen[num] = i
        return longest
