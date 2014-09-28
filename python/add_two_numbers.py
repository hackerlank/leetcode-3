# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr, carry = dummy, 0
        while l1 or l2:
            res = carry
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            carry, res = res / 10, res % 10
            curr.next = ListNode(res)
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(1)
        return dummy.next
