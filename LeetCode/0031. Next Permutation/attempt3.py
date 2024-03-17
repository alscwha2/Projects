from typing import List
from sys import argv as argv

"""
    walk from the back of the array
    once the number dips down:
        swap it with the next highest number that was found
            binary search to find the number to replace it with
            do a simple swap
        reverse the tail of the array
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # note that if the array is already in descending order, i will go to -1
        #   and the comparison will be if nums[-1] < nums[0]. This will evaluate
        #   to True since nums[-1] is the end of the array and we know already 
        #   that the array is in descending order. So i will be -1 at the end
        for i in range(len(nums)-2, -2, -1):
            if nums[i] < nums[i+1]:
                break
        # now i should either be pointing at the first number that went down
        # OR it should be at -1

        def swap_with_next_highest_number_in_tail(n: int):
            firstnum = nums[n]
            target = firstnum + 1

            # find next highest number in tail
            i, j = n + 1, len(nums) - 1
            while  i <= j:
                k = i + (j-i) // 2

                if nums[k] >= target:
                    i = k + 1
                elif nums[k] < target:
                    j = k - 1

            # swap
            nums[n], nums[j] = nums[j], nums[n]


        def reverse_array_until_end(i: int):
            j = len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


        if i > -1:
            swap_with_next_highest_number_in_tail(i)

        reverse_array_until_end(i+1)

        return nums
