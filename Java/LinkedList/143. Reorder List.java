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

 /**
 method 1
 0. use the fast and slow two pointer to find the last half part of Linked list
 1. reverse the last half part of Linked List

 1 -> 2 -> 3 -> 4
 i
 2 -> 1
 j

 2. two pointer
 3. traversal the two list and merge them

 method 2
 1. traversal the linked list and save the value into List
 2. use the List to make a new Linked list
 a. use the two pointer to traversal the list
 1  2  3  4
 i        j
 */

class Solution {
    public void reorderList(ListNode head) {
        /** corner case */
        if (head == null || head.next == null) return;

        /** find the last half of the Linked List*/
        ListNode s = head;
        ListNode f = head;
        while (f.next != null && f.next.next != null) {
            s = s.next;
            f = f.next.next;
        }

        /** cut */
        ListNode last_half = s.next;
        s.next = null;

        /** reverse the last half of the Linked List*/
        ListNode curr = last_half.next;
        last_half.next = null;
        while (curr != null) {
            ListNode temp = curr.next;
            curr.next = last_half;
            last_half = curr;
            curr = temp;
        }

        /** merge */
        curr = head;
        while (last_half != null) {
            ListNode next_half = last_half.next;
            last_half.next = curr.next;
            curr.next = last_half;
            curr = curr.next.next;
            last_half = next_half;

        }
        
    }
}