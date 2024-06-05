from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        while headA or headB:
            if headA:
                if headA in seen:
                    return headA
                seen.add(headA)
                headA = headA.next
            if headB:
                if headB in seen:
                    return headB
                seen.add(headB)
                headB = headB.next
