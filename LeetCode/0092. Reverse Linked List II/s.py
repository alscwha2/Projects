from typing import List
from sys import argv as argv
from ListConstructor import ListNode, construct, printList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        header = ListNode(-1, head)

        # find the first node to be reversed and the one before it
        prev = current = header
        for _ in range(m):
            prev = current
            current = current.next

        # iterate through reversing the links
        tail, next = current, current.next
        for _ in range(n-m):
            temp = next.next
            next.next = current
            current, next = next, temp

        # attach the first section to the beginning of the reversed section
        #  and the end of the reversed section to the end section
        prev.next = current
        tail.next = next
        return header.next


# argv[1]
printList(Solution().reverseBetween(construct([3, 5]), 1, 2))

