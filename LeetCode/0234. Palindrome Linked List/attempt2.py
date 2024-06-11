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
        return all(sequence[i] == sequence[len(sequence)-1-i] for i in range(len(sequence)//2))
