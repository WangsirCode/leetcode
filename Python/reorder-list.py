# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def reorderList2(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or head.next == None or head.next.next == None:
            return
        prev = ListNode(0)
        prev.next = head
        cur = head
        while cur.next != None:
            prev = cur
            cur = cur.next
        
        cur.next = head.next
        prev.next = None
        head.next = cur

        self.reorderList(cur.next)

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

if __name__ == "__main__":
    cur, cur.next, cur.next.next, cur.next.next.next = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    Solution().reorderList(cur)
    print(cur)
        