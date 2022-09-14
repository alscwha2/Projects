from typing import List

"""
    * Since we are looking for the lowest int > 0 that is not present,
        the answer must be 1 <= answer <= len(nums) + 1, since nums can only 
        contain len(nums) numbers.
    * We can re-order the array in place, storing the positive integers in order
        from the beginning of the array
    * This means that each positive integer will be in position num-1. 
        Alternatively, if we index the array starting from index 1, each number
        will be position num. 
        
    Algorithm:
    1) Put the array in order in linear time.
        a) iterate through the array
        b) at each position, if it is a positive integer, but that integer into
            its proper position. We will then have to take the number that was
            in that position and add process it as well. Repeat until 
                i) you find the right number for the current array position
                ii) or the number that you find is not a positive integer, or
                    is too big to have a position in the array
                iii) or the number that you would be swapping with is the same
                    number that you have right now
    2) Search through the array for the first position that does not have its
        proper number stored inside
        a) return the missing number
        b) if no number is missing, return the next possible positive integer, 
            which is len(nums) + 1
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= (num := nums[i]) <= len(nums) and num != nums[num - 1]:
                nums[i], nums[num - 1] = nums[num - 1], nums[i]

        for expected, actual in enumerate(nums, 1):
            if expected != actual:
                return expected
        return len(nums) + 1


print(Solution().firstMissingPositive([3,4,-1,1]))