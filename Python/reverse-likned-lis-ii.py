# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# Definition for singly-linked list.
# 1. 逗号输出与赋值
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for i in range(m - 1):
            prev = prev.next
        
        reverse = None
        cur = prev.next
        for i in range(n - m + 1):
            # next = cur.next
            # cur.next = reverse
            # reverse = cur
            # cur = next
            cur.next, reverse, cur = reverse, cur, cur.next 
            # reverse, cur, cur.next = cur, cur.next, reverse

        prev.next.next, prev.next = cur, reverse
        # prev.next.next = cur
        # prev.next = reverse
        return dummy.next

if __name__ == "__main__":
    cur, cur.next, cur.next.next, cur.next.next.next = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
    cur.next.next.next.next = ListNode(5)
    print(cur)
    print(Solution().reverseBetween(cur,2,4))