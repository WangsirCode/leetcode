# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Definition for singly-linked list.
# 1. l1 和 l2 不一定长度相同
# 2. 当carry == 1时也需要继续计算
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = l1.val + l2.val
        if answer >= 10:
            carry = 1
            answer = answer % 10
        else:
            carry = 0
        result = ListNode(answer)
        curruent = result
        while l1.next != None or l2.next != None or carry != 0:
            value1 = l1.next.val if l1.next != None else 0
            value2 = l2.next.val if l2.next != None else 0
            answer = value1 + value2
            answer += carry
            if answer >= 10:
                carry = 1
                answer = answer % 10
            else:
                carry = 0
            curruent.next = ListNode(answer)
            curruent = curruent.next
            l1 = l1.next if l1.next != None else l1
            l2 = l2.next if l2.next != None else l2
        return result

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b = ListNode(5)
    result = Solution().addTwoNumbers(b, a)
    c = ListNode(9)
    d = ListNode(9)
    result2 = Solution().addTwoNumbers(c,d)
    print(result2.val,result2.next.val)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))