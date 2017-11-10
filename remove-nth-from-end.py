# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head = self.reverseListIterative(head)
        if n == 1:
            return self.reverseListIterative(head.next)
        prev, cur = None, head
        for i in range(n - 1):
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return self.reverseListIterative(head)
    
    def reverseListIterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev