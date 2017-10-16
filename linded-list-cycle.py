# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution2(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head != None:
            cur = head.next
            while cur != None:
                if cur is head:
                    return True
                cur = cur.next
            head = head.next
        return False

if __name__ == '__main__':
    a = ListNode(5)
    b = ListNode(5)
    c = ListNode(9)
    d = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    d.next = None
    print(Solution().hasCycle(a))