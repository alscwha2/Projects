from typing import List

"""
First, put all positive integers in order in the array. Each positve integer num should occupy position num-1 (because array positions start from 0). This can be done in O(N) time.

Iterate through the array. When you encounter a number:
If it is out of bounds, just skip it.
If it is in bounds, put it in its proper position. You'll then have to take whatever number was sitting in that position and process that one as well. We accomplish this by simply swapping the two numbers and repeating the algorithm.
If that position already has the correct number, just skip it. (if you don't youll end up in an infinite loop)
Once all of the numbers are in order, just check to make sure that the entire array contains the numbers 1, ..., len(nums) in order.

If one is missing, that is the answer.
If none are missing, then the next positive integer is len(nums) + 1
Python trick - the enumerate function takes a second variable, which defines where to start counting from. By default we count from zero, but enumerate(nums, 1) will start counting from 1. That is perfect for us, because 1 is supposed to be in the first slot, 2 in the second, etc. So if we start counting from 1, we can just compare the number to its position to make sure that it's correct!
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def in_bounds(num):
            return 1 <= num <= len(nums)

        def put_nums_in_order():
            for i in range(len(nums)):
                while in_bounds(num := nums[i]) and num != nums[num - 1]:
                    swap(i, num - 1)

        put_nums_in_order()

        for expected, actual in enumerate(nums, 1):
            if expected != actual:
                return expected
        return len(nums) + 1


print(Solution().firstMissingPositive([3,4,-1,1]))