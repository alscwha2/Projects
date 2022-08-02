from .. import ListConstructor

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        sum_list = ListNode(val="sentinel")
        current = sum_list
        for pair in zip(l1, l2):
        	print(pair)
        	tens, ones = divmod(sum(pair) + overflow, 10)
        	current.next = ListNode(ones)
        	current = current.next
        	overflow = tens
        return sum_list.next

def to_list(l):
	current = head = ListNode(val="sentinel")
	for num in l:
		current.next = ListNode(num)
		current = current.next
	return head.next

l1 = construct_list([2,4,3])
l2 = construct_list([5,6,4])

print(Solution.addTwoNumbers(None, l1, l2))
