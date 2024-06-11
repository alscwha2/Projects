from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sequence = []
        while head:
            sequence.append(head.val)
            head = head.next
        return sequence == sequence[::-1]
