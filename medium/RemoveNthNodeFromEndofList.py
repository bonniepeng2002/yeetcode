# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # fast pointer maintains gap of n between itself and slow
        # when fast reaches the end, slow will be right before the node to delete
        if head == None or head.next == None:
            return None
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if (fast == None):
            head = slow.next
            del slow
            return head
        while (fast.next != None):
            slow = slow.next
            fast = fast.next
        tmp = slow.next
        slow.next = tmp.next
        del tmp
        return head
