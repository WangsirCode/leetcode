class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)
    
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
    
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
    #     Given a linked list, remove the nth node from the end of list and return its head.

    # For example,

    #    Given linked list: 1->2->3->4->5, and n = 2.

    #    After removing the second node from the end, the linked list becomes 1->2->3->5.
    # Note:
    # Given n will always be valid.
    # Try to do this in one pass.
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
            

    def reorderList(self, head):
        if not (head and head.next):
            return
        
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        mid = p1.next
        p1.next = None
        mid = self.reverseListIterative(mid)
        self.mergeTwoList(head,mid)


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

    def mergeTwoList(self, head1, head2):
        p1 = head1
        p2 = head2
        while head1 and head2:
            head1 = head1.next
            head2 = head2.next
            p1.next = p2
            p2.next = head1
            p1 = head1
            p2 = head2