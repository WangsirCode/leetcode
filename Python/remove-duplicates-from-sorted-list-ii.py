# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
# Definition for singly-linked list.
# Time:  O(n)
# Space: O(n)
import collections
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev, cur = head, head.next
        duplicate = collections.defaultdict(int)
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                duplicate[prev.val] = 1
            else:
                prev = cur
            cur = cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if duplicate[cur.val]:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next
