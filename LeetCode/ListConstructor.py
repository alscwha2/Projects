# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct(l):
	current = header = ListNode(-1)
	for elem in l:
		current.next = ListNode(elem)
		current = current.next
	return header.next

def printList(head):
	l = []
	while head:
		l.append(head.val)
		head = head.next
	print(l)