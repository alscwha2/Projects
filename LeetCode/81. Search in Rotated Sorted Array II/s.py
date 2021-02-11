from typing import List
from sys import argv as argv

'''
	LETS CALL THIS ATTEMPT A FAILURE FOR NOW

	Appraoch 1-
		binary search to find smallest element
		fix indicies
		binary search to find element
	Approach 2- 
		Find a way to binary search while accounting for the rotation in one pass
'''


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        first find the pivot point
        compare beginning to middle:
            if middle is smaller, you know pivot point is in between those
            if bigger you know its in the second half of the array
            if equal no info, have to repeat for both halves
        '''

        # search in [i,j], return index of smallest value, or -1 if they're all equal
        def find_pivot(i, j):
            if i >= j:
                return -1

            k = i + (i+j)//2
            if nums[k] > nums[i]:
                pivot = find_pivot(k, j)
                return pivot if pivot != -1 else
                return find_pivot(k, j)
            elif nums[k] < nums[i]:
                return find_pivot(i, k)
            else:
                return find_pivot(i, k) or find_pivot(k, j)

        '''
            after finding the pivot point, convert indicies, and do binary search
            '''


# argv[1]
print(Solution().search([1, 3, 1, 1, 1], 3))

