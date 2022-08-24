from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the end
        # Be able to keep track of Nth from the end
        # Take out that node
        if head is None or n is 0:
            return None

        end = head
        for _ in range(n-1):
            end = end.next
            if end is None:
                return None

        prev = ListNode()
        prev.next = head

        while end.next is not None:
            end = end.next
            prev = prev.next

        if prev.next is head:
            return head.next

        prev.next = prev.next.next
        return head
