'''
	I feel like this is not elegant enough. I wish I could get this to look nicer.
'''


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		overflow = 0
		sum_list = ListNode(val="sentinel")
		current = sum_list
		while l1 or l2:
			sum = overflow
			if l1: sum += l1.val
			if l2: sum += l2.val
			tens, ones = divmod(sum, 10)
			current.next = ListNode(ones)
			current = current.next
			overflow = tens
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
		if overflow:
			current.next = ListNode(overflow)
		return sum_list.next

def construct_list(l):
	current = header = ListNode(-1)
	for elem in l:
		current.next = ListNode(elem)
		current = current.next
	return header.next

l1 = construct_list([2,4,3])
l2 = construct_list([5,6,4])

def print_from_node(l):
	nodes = []
	while(l is not None):
		nodes.append(l.val)
		l = l.next
	print(nodes)

print_from_node(Solution().addTwoNumbers(l1, l2))