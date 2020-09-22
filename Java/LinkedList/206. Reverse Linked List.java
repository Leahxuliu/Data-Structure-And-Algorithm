/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */


/** reverseByRecursion
 * the function return the head of the new linkedlist 
 * each time save the end of reversed linkedlist (which mean the last node of the reversed linkedlist)
 *   5  ->  10  ->  2  ->  6
 * curr    end            reversed
 *   6  ->  2  ->  10  ->  5
 *  reversed       end    curr
*/
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode end = head.next;
        ListNode reversed = reverseList(head.next);
        end.next = head;
        head.next = null;
        return reversed;
    }
}

/** reverseByIteration */