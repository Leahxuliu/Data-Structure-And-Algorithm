/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 /** 
 * 1. make a dummy node, and connect with the Linked List
 * 2. travesal the linked list to find m - 1,make (end)
 * 3. reverse the linked list from m to n
        a. mark second node
        b. cut the first node(dummy, last)
        c. travesal the linked list form m+1 to n (curr)
        b. connect the first node in the removed Linked list with new_head
    4. end.next = dummy, last.next = curr
    5. return head
 */

class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        int temp = m;
        while (temp > 1) {
            dummy = dummy.next;
            temp -= 1;
        }

        ListNode end = dummy;
        dummy = dummy.next;
        end.next = null;
        ListNode curr = dummy.next;
        dummy.next = null;
        ListNode LAST = dummy;

        int times = n - m + 1;
        while (times > 1 && curr != null) {
            ListNode next_head = curr.next;
            curr.next = null;
            curr.next = dummy;
            dummy = curr;
            curr = next_head;
            times -= 1;
        }

        end.next = dummy;
        LAST.next = curr;
        /** 易错，注意从第一个节点就开始置换的情况*/
        if (m == 1) {
            return end.next;
        } else {
            return head;
        }
    }
}

/** 上述方法可优化
 * 优化成双指针，头插法
 * dummyHead -> 1 -> 2 -> 3 -> 4 ->5
 *              x    y
 * dummyHead -> 1 -> 3 -> 2 -> 4 ->5
 *              x         y 
 * dummyHead -> 1 -> 4 -> 3 -> 2 ->5
 *              x              y
 */


 // 链接：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/

/** recursion*/
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == 1) {
            return reverse(head, n);
        }
        head.next = reverseBetween(head.next, m - 1, n - 1);
        return head;
    }

    ListNode unreversedHead = null;
    public ListNode reverse(ListNode head, int n) {
        if (n == 1) {
            unreversedHead = head.next;
        }

        if (head == null || head.next == null || n == 1) {
            return head;
        }
        
        ListNode end = head.next;
        ListNode reversedHead = reverse(head.next, n - 1);
        end.next = head;
        head.next = unreversedHead;
        return reversedHead;

    }
}