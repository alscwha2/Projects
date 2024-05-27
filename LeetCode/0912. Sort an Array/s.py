from functools import lru_cache
from typing import List

'''
    Time: O(NlogN)
    Space: O(1) (no recursion)
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)

        if length < 2:
            return nums

        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        @lru_cache(maxsize=1)
        def parent(i):
            return (i+1) // 2 - 1

        @lru_cache(maxsize=1)
        def first_child(i):
            return (i+1) * 2 - 1

        @lru_cache(maxsize=1)
        def second_child(i):
            return (i+1) * 2

        def is_in_array_bounds(i):
            return i < length

        def sink(i):
            while is_in_array_bounds(first_child(i)):
                bigger_child =  second_child(i) \
                                    if is_in_array_bounds(second_child(i)) \
                                    and nums[second_child(i)] > nums[first_child(i)]\
                                else first_child(i)

                if nums[bigger_child] > nums[i]:
                    swap(i, bigger_child)
                    i = bigger_child
                else:
                    return

        def heapify():
            for i in range(len(nums) - 2, -1, -1):
                sink(i)

        def heapsort():
            heapify()
            nonlocal length
            for length in range(length, 1, -1):
                swap(0, length-1)
                length -= 1
                sink(0)

        heapsort()
        return nums
