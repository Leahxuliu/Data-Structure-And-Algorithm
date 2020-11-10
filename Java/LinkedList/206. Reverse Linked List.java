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

/**
 * 注意 明确函数return的是reversed之后的head
 * 当作黑匣子处理
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode curr = head.next;
        ListNode end = head.next;
        head.next = null;
        ListNode reverse = reverseList(curr);
        end.next = head;
        return reverse;
    }
}


/** Iteration
* 1. 保留从第二个节点开始的linked list（curr）
* 2. 断开第一个节点，第一个节点是新linked list的起点
* 3. 每次保留curr第二个以后的Linked list，断开curr的第一个节点
* 4. 断开的节点与new head相连，再把new head移到最头部的节点
*/

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ListNode curr = head.next;
        head.next = null;

        while (curr != null) {
            ListNode next_curr = curr.next;
            curr.next = head;
            head = curr;
            curr = next_curr;
        }
        return head;
    }
}