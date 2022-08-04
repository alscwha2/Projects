from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head or not k:
			return head

		# find length and tail
		length = 1
		current = head
		while current.next:
			current.next.prev = current
			current = current.next
			length += 1
		tail = head.prev = current

		# find new head
		k %= length
		current = head
		for i in range(k):
			current = current.prev
		
		# if head neads to move, move it
		if k:
			tail.next = head
			current.prev.next = None
			head = current
		return head



inputlist = [1,2,3,4,5]
amount = 2
current = inputhead = ListNode(-1)
for num in inputlist:
	current.next = ListNode(num)
	current = current.next
inputhead = inputhead.next

current = inputhead
printstring = '['
while current:
	printstring += str(current.val) + ','
	current = current.next
print(printstring + ']')

solutionlist = Solution().rotateRight(inputhead, amount)

printstring = '['
while solutionlist:
	printstring += str(solutionlist.val) + ']'
	solutionlist = solutionlist.next
print(printstring + ']')