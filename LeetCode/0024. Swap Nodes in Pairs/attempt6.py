from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            * link to the previous
            * link to the first
            * link to the second
        '''
        sentinel = ListNode()
        sentinel.next = head
        prev = sentinel
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
        return sentinel.next
