/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

 //	THAT WAS RECORD TIME! I WROTE THAT IN LIKE A MINUTE AND A HALD AND IT WORKED THE FIRST TRY!
var removeNthFromEnd = function(head, n) {
	let previous = head;
	let current = head.next;

	while(current) {
		current.previous = previous;
		previous = current;
		current = current.next;
	}

	current = previous;
	while(n > 1) {
		current = current.previous;
		n--;
	}

	if (current === head) return head.next;

	current.previous.next = current.next;
	return head;
    
};