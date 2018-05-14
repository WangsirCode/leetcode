# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head

        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palindrome = True
        while reverse:
            is_palindrome = is_palindrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next
        return is_palindrome

if __name__ == "__main__":
    cur, cur.next, cur.next.next, cur.next.next.next = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
    cur.next.next.next.next = ListNode(5)
    # cur.next.next.next.next.next = ListNode(6)
    print(Solution().isPalindrome(cur))