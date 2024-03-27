from typing import List

'''
    Allowing the KeyError to be thrown in the first solution and ignoring it was
    very bad error handling. This version makes the intentions of the code much
    more explicit - only all union if both numbers are in the set
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        group = {num:num for num in nums}
        size = {num:1 for num in nums}

        def find(a):
            root = a
            while group[root] != root:
                root = group[root]
            while a != root:
                parent = group[a]
                group[a] = root
                a = parent
            return root

        def union(a,b):
            a_root, b_root = find(a), find(b)
            if a_root != b_root:
                group[a_root] = b_root
                size[b_root] += size[a_root]

        members = set(nums)
        for num in nums:
            if num-1 in members:
                union(num, num-1)
            if num+1 in members:
                union(num, num+1)

        return max(size.values(), default=0)
