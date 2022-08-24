import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = nextnext


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__gt__ = lambda a, b: a.val > b.val

        lists = [l for l in lists if l]
        heapq.heapify(lists)
        sentinel = current = ListNode()
        while lists:
            current.next = heapq.heappop(lists)
            current = current.next
            if current.next:
                heapq.heappush(lists, current.next)
        return sentinel.next
