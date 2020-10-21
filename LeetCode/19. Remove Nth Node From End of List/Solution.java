/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

/*
    This whole thing was rediculous
*/
class Solution {
    class DListNode extends ListNode {
        DListNode previous;
        ListNode node;
        DListNode(ListNode node) { this.node = node; }
        DListNode(ListNode node, DListNode previous) { this.node = node; this.previous = previous;}
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        DListNode dprevious = new DListNode(head);
        DListNode dcurrent = new DListNode(dprevious.node.next, dprevious);
        ListNode previous = head;
        ListNode current = head.next;

        while(current != null) {
            dprevious = dcurrent;
            dcurrent = new DListNode(current.next, dprevious);
            previous = current;
            current = current.next;
        }

        dcurrent = dprevious;

        while(n > 1) {
            dcurrent = dcurrent.previous;
            n--;
        }

        if(dcurrent.node == head) return head.next;
        dcurrent.previous.node.next = dcurrent.node.next;
        return head;
    }
}   