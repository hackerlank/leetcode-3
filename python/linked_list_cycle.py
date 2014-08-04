# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        step_one, step_two = head, head
        while step_two and step_two.next:
            step_one, step_two = step_one.next, step_two.next.next
            if step_one is step_two:
                return True
        return False
